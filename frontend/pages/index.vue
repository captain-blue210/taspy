<template>
  <div>テスト：{{ test }}</div>
</template>

<script>
import Logo from '~/components/Logo.vue'
import VuetifyLogo from '~/components/VuetifyLogo.vue'

const axios = require('axios')

export default {
  asyncData(){
    let url = 'http://localhost:8000/api/get_person/'
    return axios.get(url)
      .then((res) => {
        return { test: res.data }
      })
  },
  components: {
    Logo,
    VuetifyLogo
  }
}
</script>
