<template>
    <Task :task="task"></Task>
</template>

<script>
const axios = require('axios')

export default {
  asyncData({ params }){
    let url = `http://localhost:8000/api/get_task_detail/${params.id}`
    return axios.get(url)
      .then((res) => {
        return { task: res.data.task }
      })
  },
}
</script>
