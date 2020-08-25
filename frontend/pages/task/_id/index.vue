<template>
    <Task :task="task"></Task>
</template>

<script>
import axios from '~/plugins/axios'

export default {
  asyncData({ params }){
    let url = `/api/task/${params.id}`
    return axios.get(url)
      .then((res) => {
        return { task: res.data.task }
      })
  },
}
</script>
