<template lang="pug">
div.text-h3.text-center.text-teal your courses
div.q-pa-md 
  .flex
   div(v-for="course in courses")
    q-card.my-card
      q-img(
        :src= "course.img_url"
        )
      q-card-section
        .text-h5 {{ course["name"] }}
        .text-subtitle2 {{ course["description"] }}
        q-btn(label="navigate",@click="ensure_access_token")
</template>
<script>
import axios from 'axios';
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
      const token = localStorage.getItem('access_token');
      const response = await axios.get('http://localhost:8000/courses/public', {
        headers: {
          Authorization: `Bearer ${token}`, // Include the token as a Bearer token
        },
      });
      this.courses = response.data;
    },
  },
};
</script>
<style lang="sass" scoped>
.my-card
  margin:10px
  padding:10px
  width: 100vh
  max-width:22rem
.q-img 
  height: 200px
  object-fit: cover
</style>
