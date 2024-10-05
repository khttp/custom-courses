<template lang="pug">
q-page(style="display: flex; align-items: center; justify-content: center; min-height: 100vh;")
  q-card(style="width:30rem")
    q-card-section
      .text-h5.text-center Login

    q-form(@submit="onSubmit")
      q-input(
        filled
        v-model="username"
        label="Email"
        type="text"
        hint="Enter your email"
        lazy-rules
        :rules="[val => !!val || 'Email is required']"
        class="q-mb-md"
      )

      q-input(
        filled
        v-model="password"
        label="Password"
        type="password"
        hint="Enter your password"
        lazy-rules
        :rules="[val => !!val || 'Password is required']"
        class="q-mb-md"
      )
      div.text-center
        q-btn(label="Login" type="submit" color="teal")
      q-btn(label="forget password ?",flat,size="12px",color="teal",disable)
    q-btn(label="register for new account",flat,size="12px",color="teal",@click="this.$router.push('/register')")
</template>

<script>
import axios from 'axios';
export default {
  name: 'LoginPage',
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    async onSubmit() {
      const formData = new URLSearchParams();
      formData.append('username', this.username);
      formData.append('password', this.password);
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
        localStorage.setItem('user_id', response.data.user_id);
        response.data.user_id;
        const accessToken = response.data.access_token; // Modify this based on your backend response structure
        localStorage.setItem('access_token', accessToken);
        this.$router.push('/dashboard');
      } catch (error) {
        console.error('Error getting access token:', error);
        throw error;
      }
    },
  },
};
</script>
