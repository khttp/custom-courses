<template lang="pug">
q-input.q-pa-sm(
    v-model="search",
    placeholder="search..."
    style="width:20rem;"

  )
div.q-pa-md
  .flex
   div(v-for="course in courses" :key="course.id")
    q-card.my-card
      q-img(
        :src= "course.img_url"
        )
      q-card-section
        .text-h5 {{ course["name"] }}
          q-icon(name="edit",size="1rem")
            q-tooltip Click to edit section name
          q-popup-edit(
            v-model="course.name",
            v-slot='scope',
            touch-position
            auto-save,
            )
            q-input(
              v-model='scope.value',
              hint='Edit section name',
              dense,
              autofocus,
              counter,
              @keyup.enter='edit_course_name(course.id,scope.value);scope.cancel()',
              :rules='[(val) => !!val || "Field is required"]'
          )
        q-btn(label="navigate",text-color="teal", disable)
        q-btn(label="delete",text-color="teal",@click="delete_course(course.id)")
</template>
<script>
import axios from 'axios';
import { Notify } from 'quasar';
const token = localStorage.getItem('access_token');
const user_id = localStorage.getItem('user_id');
export default {
  name: 'HomePage',
  data() {
    return {
      courses: [],
    };
  },
  mounted() {
    this.fetchCourses();
  },
  methods: {
    async fetchCourses() {
      console.log('hi there i am using vue');
      const response = await axios
        .get('http://localhost:8000/users/me/courses', {
          headers: {
            Authorization: `Bearer ${token}`, // Include the token as a Bearer token
          },
          params: {
            current_user_id: user_id,
          },
        })
        .catch((error) => {
          if (error.response.status === 401) this.$router.push('/login');
        });
      this.courses = response.data;
    },
    async delete_course(courseID) {
      try {
        await axios.delete(`http://localhost:8000/courses/${courseID}`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        this.courses = this.courses.filter((course) => course.id !== courseID);

        Notify.create({
          message: 'course deleted successfully!',
          color: 'green',
          position: 'bottom',
          timeout: 3000,
        });
      } catch (error) {
        console.log(error);
      }
    },
    async edit_course_name(courseID, newName) {
      await axios.put(
        `http://localhost:8000/courses/${courseID}`,
        { name: newName },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      Notify.create({
        message: 'course updated successfully!\n refresh to see your changes',
        color: 'green',
        position: 'bottom',
        timeout: 3000,
      });
    },
  },
};
</script>
<style lang="sass" scoped>
.my-card
  margin:10px
  padding:10px
  width: 100vh
  max-width:20rem
.q-img
  height: 200px
  object-fit: cover
</style>
