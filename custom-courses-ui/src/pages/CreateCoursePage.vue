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
import { Notify } from 'quasar';
import axios from 'axios';
import { v4 } from 'uuid';
const user_id = localStorage.getItem('user_id');
const token = localStorage.getItem('access_token');
export default {
  mounted() {},
  setup() {
    const newCourse = ref({
      name: '',
      description: '',
      imgUrl: '',
      visibility: 'private',
    });
    const onReset = () => {
      newCourse.value.name = '';
      newCourse.value.description = '';
      newCourse.value.imgUrl = '';
      newCourse.value.visibility = 'private';
    };
    const onSubmit = async () => {
      const course = {
        id: v4(),
        name: newCourse.value.name,
        description: newCourse.value.description,
        img_url: newCourse.value.imgUrl,
        course_type: newCourse.value.visibility,
        user_id: '3fa85f64-5717-4562-b3fc-2c963f66afa6',
      };
      console.log(token);
      const response = await axios.post(
        'http://localhost:8000/users/me/courses',
        course,
        {
          headers: {
            Authorization: `Bearer ${token}`, // Include the token as a Bearer token
          },
          params: {
            user_id: user_id,
          },
        }
      );
      // console.log(response)
      Notify.create({
        message: `course ${response.data.name} created successfully! `,
        color: 'green',
        position: 'bottom',
        timeout: 3000,
      });
      onReset();
    };
    return {
      newCourse,
      onReset,
      onSubmit,
    };
  },
};
</script>
