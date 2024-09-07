<template lang="pug">
q-page(style="display: flex; align-items: center; justify-content: center; min-height: 100vh;")
  q-card(style="width:30rem")
    q-card-section
      .text-h5.text-center Register

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

      q-input(
        filled
        v-model="confirmPassword"
        label="Confirm Password"
        type="password"
        hint="Re-enter your password"
        lazy-rules
        :rules="[val => !!val || 'Confirm Password is required']"
        class="q-mb-md"
      )

      q-checkbox(v-model="termsAccepted" label="I accept the terms and conditions" class="q-mb-md")

      div.text-center
        q-btn(label="Register" type="submit" color="teal")
</template>
  
<script>
export default {
  name: 'RegisterPage',
  data() {
    return {
      email: '',
      password: '',
      confirmPassword: '',
      termsAccepted: false
    };
  },
  methods: {
    onSubmit() {
      // Your registration logic here
    }
  }
};
</script>
  