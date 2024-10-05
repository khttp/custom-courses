<template lang="pug">
q-layout(container style="height: 100vh" )
  q-header.bg-teal
    q-toolbar
      q-icon(name="school" size="2rem")
      q-toolbar-title Custom Courses
      q-avatar(size='50px')
        img(
          src="icons/boy.png"
        )
      .text-h6 abooh {{ username }}
  q-page-container
    div
      q-splitter(v-model="splitterModel" style="height: 100vh")
        template(v-slot:before)
          q-tabs(
            vertical
            class="text-teal"
          )
            q-route-tab(to='/dashboard',icon="dashboard" label='dashboard')
            q-route-tab(to='/public-courses',icon="book" label='public courses')
            q-route-tab(to='/create-course',icon="add" label='create course')
            q-route-tab(to='/settings',icon="settings" label='settings')
        template(v-slot:after)
            router-view 
</template>
<script>
export default {
  data() {
    return {
      search: '',
    };
  },
};
</script>
