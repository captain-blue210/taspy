<template>
  <TaskList :tasks="task"></TaskList>
</template>

<script>
import axios from '~/plugins/axios'

export default {
  asyncData(){
    let url = '/api/task/'
    return axios.get(url)
      .then((res) => {
        return { task: res.data.task }
      })
  },
}
</script>
