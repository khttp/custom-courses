<template lang="pug">
q-page(style="display: flex; align-items: center; justify-content: center; min-height: 100vh;")
  q-card(style="width:30rem")
    q-card-section
      .text-h5.text-center Login

    q-form(@submit="onSubmit")
      q-input(
        filled
        v-model="email"
        label="Email"
        type="email"
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
        q-btn(label="register for new account",flat,size="12px",color="teal",@click="this.$router.push('/register')")
</template>
  
<script>
export default {
  name: 'LoginPage',
  data() {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    onSubmit() {
      // Your login logic here
    }
  }
};
</script>
