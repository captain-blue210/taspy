<template>
  <TaskList :tasks="tasks"></TaskList>
</template>

<script>
const axios = require('axios')

export default {
  asyncData(){
    let url = 'http://localhost:8000/api/get_tasks/'
    return axios.get(url)
      .then((res) => {
        return { tasks: res.data.tasks }
      })
  },
}
</script>
