<template>
  <TaskList :tasks="tasks"></TaskList>
</template>

<script>
import TaskList from '../components/TaskList.vue'
const axios = require('axios')

export default {
  asyncData(){
    let url = 'http://localhost:8000/api/get_tasks/'
    return axios.get(url)
      .then((res) => {
        return { tasks: res.data.tasks }
      })
  },
  components: {
    TaskList,
  }
}
</script>
