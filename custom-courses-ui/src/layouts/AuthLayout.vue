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
      
  q-page-container
    div
      q-splitter(v-model="splitterModel" style="height: 100vh")
        template(v-slot:before)
          q-tabs(
            vertical
            class="text-teal"
          )
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
