import Vue from 'vue'
import moment from 'moment'

Vue.filter('formatDate', function(date) {
    if (!date) return 'なし'
    return moment(date).format('YYYY/MM/DD')
})
