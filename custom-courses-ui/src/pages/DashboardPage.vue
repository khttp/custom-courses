<template lang="pug">
div.text-h3.text-center.text-teal your courses
div.q-pa-md 
  .flex
   div(v-for="course in courses")
    q-card.my-card
      img(src="https://cdn.quasar.dev/img/mountains.jpg")
      q-card-section
        .text-h5 {{ course["name"] }}
        .text-subtitle2 {{ course["description"] }}
        q-btn(label="navigate",text-color="teal",@click="ensure_access_token")
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
    this.ensure_access_token();
    this.fetchCourses();
  },
  methods: {
    async ensure_access_token() {
      const formData = new URLSearchParams();
      formData.append('username', 'string'); // Replace with actual username
      formData.append('password', 'string'); // Replace with actual password
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
  },
};
</script>
<style lang="sass" scoped>
.my-card
  margin:10px
  width: 100%
  max-width:22rem
</style>
