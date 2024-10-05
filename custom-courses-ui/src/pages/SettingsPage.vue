<template lang="pug">
  q-page.flex.justify-evenly(padding='')
    q-card(style='width: 100%')
      q-card-section.row
        q-icon(name='account_circle', color='teal', size='2rem')
        .text-h6.text-teal.q-ml-sm Account
      q-card-section.q-pa-sm.column
        .row.q-pb-xs
          q-btn(
            flat,
            icon='person',
            label='user profile ',
            color='teal',
            @click="this.$router.push('/profile')"
          )
        .row.q-pb-xs
          q-btn(
            flat,
            icon='lock',
            label='Change Password',
            color='teal',
            :disable='true'
          )
      q-separator
      q-card-section.row
        q-icon(name='tune', color='teal', size='2rem')
        .text-h6.text-teal.q-ml-sm General
      q-card-section.q-pa-sm.column
        .row.q-pb-xs
          q-btn(
            flat,
            label='Notifications',
            icon='notifications',
            color='teal',
            :disable='true'
          )
        .row.q-pb-xs
          q-btn(
            flat,
            label='Privacy',
            icon='privacy_tip',
            color='teal',
            :disable='true'
          )
      q-separator
      q-card-section.row
        q-icon(name='help', color='teal', size='2rem')
        .text-h6.text-teal.q-ml-sm Support & Feedback
      q-card-section.q-pa-sm.column
        .row.q-pb-xs
          q-btn(
            flat,
            label='Help',
            icon='contact_support',
            color='teal',
            :disable='true'
          )
        .row.q-pb-xs
          q-btn(
            flat,
            label='Feedback',
            icon='feedback',
            color='teal',
            :disable='true'
          )
</template>
<script setup>
defineOptions({
  name: 'SettingsPage',
});
</script>
