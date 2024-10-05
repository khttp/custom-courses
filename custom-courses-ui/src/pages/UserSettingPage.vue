<template lang="pug">
    q-page.flex.justify-evenly(padding='')
      div(
        style='width: 90%; padding: 1rem; overflow-wrap: break-word; word-break: break-word; border: 1px solid #e0e0e0; border-radius: 1rem; background-color: white'
      )
        .column.content-end
          q-btn(
            icon='edit',
            label='Edit',
            color='teal',
            style='width: 6.5rem',
            @click='editUserDialog = true'
          )
          q-dialog(v-model='editUserDialog')
            q-card(style="max-width:30rem ;width:100%")
              q-card-section
                q-card-title.text-h6.text-teal Edit Profile
                q-card-section
                  q-input(
                    v-model='user.name',
                    label='Name',
                    color='teal',
                    placeholder='Enter your name'
                  )
                  q-input(
                    v-model='user.mail',
                    label='Email',
                    color='teal',
                    placeholder='Enter your email'
                  )
                  q-input(
                    v-model='user.phone',
                    label='Phone',
                    color='teal',
                    placeholder='Enter your phone number'
                  )
                  q-input(
                    v-model='user.country',
                    label='Country',
                    color='teal',
                    placeholder='Enter your country'
                  )
                q-card-actions.text-teal(align='right')
                  q-btn(
                    label='Cancel',
                    color='teal',
                    flat,
                    @click='editUserDialog = false'
                  )
                  q-btn(
                    label='Save',
                    color='teal',
                    flat,
                    @click='editProfile;editUserDialog=false',
                  )
        .row.q-gutter-md
          .column.q-gutter-md
            q-avatar(size='10rem')
              q-img(src='icons/boy.png')
          .column.q-gutter-md
            .row.q-gutter-sm
              q-icon(name='person', size='1.8rem', color='teal')
              .col
                .text-h6.text-teal Name
                .text-h7 {{ user.name }}
            .row.q-gutter-sm
              q-icon(name='email', size='1.8rem', color='teal')
              .col
                .text-h6.text-teal Email
                .text-h7 {{ user.email }}

            .row.q-gutter-sm
              q-icon(name='phone', size='1.8rem', color='teal')
              .col
                .text-h6.text-teal Phone
                .text-h7  {{ user.phone }} 
            .row.q-gutter-sm
              q-icon(name='public', size='1.8rem', color='teal')
              .col
                .text-h6.text-teal Country
                .text-h7 {{ user.country }}
        .column
          br
    </template>
<script setup>
import { ref } from 'vue';
const editUserDialog = ref(false);
const user = ref({
  name: '',
  email: '',
  phone: '',
  country: '',
});
/* eslint-disable-next-line no-unused-vars */
const editProfile=()=>{
  user.value = this.user;
}
console.log(editUserDialog, user,editProfile);
</script>
