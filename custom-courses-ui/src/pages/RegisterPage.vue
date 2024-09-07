<template lang="pug">
q-page(style="display: flex; align-items: center; justify-content: center; min-height: 100vh;")
  q-card(style="width:30rem")
    q-card-section
      .text-h5.text-center Register

    q-form(@submit="onSubmit")
      q-input(
        filled
        v-model="name"
        label="Name"
        type="text"
        hint="Enter your name"
        lazy-rules
        :rules="[val => !!val || 'Email is required']"
        class="q-mb-md"
      )
      q-input(
        filled
        v-model="email"
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
import axios from 'axios';
import {v4} from'uuid'
import { Notify } from 'quasar';
export default {
  name: 'RegisterPage',
  data() {
    return {
      name:'',
      email: '',
      password: '',
      confirmPassword: '',
      termsAccepted: false
    };
  },
  methods: {
    async onSubmit() {
        if(this.password!=this.confirmPassword){
            Notify.create({
                message: 'passwords don\'t match!',
                color: 'red',
                position: 'bottom',
                timeout: 3000,
            });
        }
        if(this.termsAccepted==false){
            Notify.create({
                message: 'please accept our terms',
                color: 'red',
                position: 'bottom',
                timeout: 3000,
            });
        }
        await axios.post('http://localhost:8000/auth/register',
            {id:v4(),
             name:this.name,
             email:this.email,
             password:this.password
            })
        Notify.create({
            message:'thanks for registering to our site welcome aboard',
            color:'green',
            timeout:3000
        })
        this.$router.push('/login')
    },
  }
};
</script>
  