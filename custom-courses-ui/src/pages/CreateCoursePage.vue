<template lang="pug">
div.q-pa-md(style="max-width: 400px")
  q-form(@submit="onSubmit" @reset="onReset" class="q-gutter-md")
    q-input( filled
      v-model="newCourse.name"
      label="Course name *"
      lazy-rules
      :rules="[ val => val && val.length > 0 || 'Please type something']"
    )

    q-input( filled
      v-model="newCourse.description"
      label="description *"
      lazy-rules
    )
    q-input( filled
      v-model="newCourse.imgUrl"
      label="img url *"
      lazy-rules
    )
    q-select(
  v-model="newCourse.visibility"
  :options="['private', 'public']"
  label="course type *"
  outlined
)
    div
      q-btn(label="Submit" type="submit" color="primary")
      q-btn(label="Reset" type="reset" color="primary" flat class="q-ml-sm")
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';
import {v4} from 'uuid';
export default {
  mounted(){

  },
  setup() {
    const newCourse =ref({
    name : '',
    description : '',
    imgUrl : '',
    visibility : 'private'
    })

    return {
      newCourse,

      async onSubmit() {
        const course={
          id:v4(),
          name: newCourse.value.name,
          description: newCourse.value.description,
          img_url: newCourse.value.imgUrl,
          course_type: newCourse.value.visibility,
          user_id:'3fa85f64-5717-4562-b3fc-2c963f66afa6'
        }
        try {
        const token = localStorage.getItem('access_token');
        console.log(token)
        const response = await axios.post('http://localhost:8000/users/me/courses', course,
        {
          headers: {
            Authorization: `Bearer ${token}`, // Include the token as a Bearer token
          },
          params: {
            user_id: '3fa85f64-5717-4562-b3fc-2c963f66afa6',
          },
        }
      )
        console.log('Data saved successfully:', response.data)
      } catch (error) {
        console.error('Error saving data:', error)
      }
      },

      onReset() {
        name.value = null;
        description.value = null;
        imgUrl.value = null;
      },
    };
  },
};
</script>
