import Borrow from './views/borrow.vue'
import Back from './views/back.vue'

export default[
  { path: '/borrow', component: Borrow ,mname:'借书',icon:'ios-paper'},
  { path: '/back', component: Back ,mname:'还书',icon:'ios-analytics'},
]
