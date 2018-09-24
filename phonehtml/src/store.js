import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state:{
        TAB:0,
    },
    mutations:{
        go_tab(state,index){
            state.TAB = index
        }
    }
})