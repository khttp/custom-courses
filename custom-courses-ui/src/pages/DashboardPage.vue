<template lang="pug">
div.text-h3.text-center.text-teal your courses
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
export default {
  name: 'HomePage',
  data() {
    return {
      courses: [],
    };
  },
  mounted() {
    this.ensure_access_token();
    this.fetchCourses();
  },
  methods: {
    async ensure_access_token() {
      const formData = new URLSearchParams();
      formData.append('username', 'string'); 
      formData.append('password', 'string'); 
      try {
        const response = await axios.post(
          'http://localhost:8000/auth/login',
          formData,
          {
            headers: {
              'Content-Type': 'application/x-www-form-urlencoded',
            },
          }
        );

        const accessToken = response.data.access_token; // Modify this based on your backend response structure
        localStorage.setItem('access_token', accessToken);

        console.log('Access token:', accessToken);
        return accessToken;
      } catch (error) {
        console.error('Error getting access token:', error);
        throw error;
      }
    },
    async fetchCourses() {
      const token = localStorage.getItem('access_token');
      const response = await axios.get(
        'http://localhost:8000/users/me/courses',
        {
          headers: {
            Authorization: `Bearer ${token}`, // Include the token as a Bearer token
          },
          params: {
            current_user_id: '3fa85f64-5717-4562-b3fc-2c963f66afa6',
          },
        }
      );
      this.courses = response.data;
    },
    async delete_course(courseID){
      
      const token = localStorage.getItem('access_token');
      try{
        await axios.delete(`http://localhost:8000/courses/${courseID}`,
        {headers:{
          Authorization: `Bearer ${token}`,
        }}
      )
      this.courses = this.courses.filter(course => course.id !== courseID);
      
      Notify.create({
        message: 'course deleted successfully!',
        color: 'green',
        position: 'bottom',
        timeout: 3000,
      });
    }catch(error){
      console.log(error)
    }    
  },
    async edit_course_name(courseID,newName) {
      const token = localStorage.getItem('access_token');
      await axios.put(
        `http://localhost:8000/courses/${courseID}`,{name:newName},
        {headers: {
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
    }
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
