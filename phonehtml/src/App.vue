<template>
  <div id="app">
    <view-box ref="viewBox" body-padding-bottom=50px; v-if='islogin'>
        <router-view></router-view>

        <tabbar slot="bottom" style='position:fixed;'>
            
              <tabbar-item @on-item-click='change(0)' :selected='index==0'>
                <img slot="icon" src="./assets/favor.png">
                <img slot="icon-active" src="./assets/favor_fill.png">

                <span slot="label">消息</span>
              </tabbar-item>
              <tabbar-item @on-item-click='change(1)' :selected='index==1'>
                <img slot="icon" src="./assets/search.png">
                <img slot="icon-active" src="./assets/search_fill.png">

                <span slot="label">书籍查询</span>
              </tabbar-item>
              <tabbar-item @on-item-click='change(2)' :selected='index==2'>
                <img slot="icon" src="./assets/my.png">
                <img slot="icon-active" src="./assets/my_fill.png">
                <span slot="label">我的</span>
              </tabbar-item>
          
        </tabbar>
    </view-box>
    <view-box v-else>
        <div style='height: 50px'>
            
        </div>
        <!-- <group > -->
            <h3 style='text-align: center;height: 50px'>xx学院图书馆</h3>
        <!-- </group> -->
         <group >
          <x-input title="账号" name="username" placeholder="请输入账号"  v-model='user_sn'></x-input>
        </group>

        <div>
        </div>

   <group >
      <x-input title="密码" name="username" type='password' placeholder="请输入密码"  v-model='password'></x-input>
    </group>
    <div style='height: 100px;padding-top: 40px'>
        <x-button type="primary" @click.native='login'>登陆</x-button>
        
    </div>

        
    </view-box>
  </div>
</template>

<script>
    import { XInput, Group, XButton, Cell,ViewBox,Tabbar, TabbarItem} from 'vux'
    import http from '@/http.js'
    import qs from 'qs'

export default {
    components: {
    XInput,
    XButton,
    Group,
    Cell,
    ViewBox,
    Tabbar, TabbarItem
  },
  name: 'app',
  data:function(){return{
    // index:0,
    islogin:false,
    user_sn:null,
    password:null,
   }},

   methods:{
    login(){
        var self = this
        http.post('/login/',{
            username:this.user_sn,
            password:this.password
        },{    
            transformRequest: [function (data) {
                        // 对 data 进行任意转换处理
                        return qs.stringify(data)}],
        },).then((response)=>{
            localStorage.setItem('token',response.data.token)
            http.defaults.headers.common['Authorization'] = 'JWT '+response.data.token;
            localStorage.setItem('username',this.user_sn)
            this.islogin = true

        })
        .catch((error)=>{
                if(error.response.data.username){
                    self.$vux.alert.show({'title':'提醒',content:'账号不能为空'})
                }else if(error.response.data.password){
                    self.$vux.alert.show({'title':'提醒',content:'密码不能为空'})
                }else{
                    self.$vux.alert.show({'title':'提醒',content:'账号密码错误'})
                }

            this.user_sn = ''
            this.password = ''
        })
    },
    reflesh(){
        var self = this
        http.post('/refresh/',{token:localStorage.getItem('token')},{    
            transformRequest: [function (data) {
                        // 对 data 进行任意转换处理
                        return qs.stringify(data)}],
        }).then(response=>{
            localStorage.setItem('token',response.data.token)
            http.defaults.headers.common['Authorization'] = 'JWT '+response.data.token;
            this.islogin = true
            this.$router.push({path:'/message'})

        }).catch(error=>{
            this.user_sn = null
            this.password = null
            this.islogin = false
        })
    },
    change(i){
        if(i==0){
            this.$router.push({ path: `/message` })
        }
        else if(i==1){
            this.$router.push({path:`books`})
        }else if(i==2){
            this.$router.push({path:'my'})
        }
        this.$store.commit('go_tab',i)
    }
   },
    computed: {

    index:function(){
        return this.$store.state.TAB
        }
            
    },
   mounted(){
    // var token = localStorage.getItem('token')
    this.reflesh()
    // if(!token){
    //     this.islogin = false

    // }else{
    //     this.islogin = true
    // }

   },
}
</script>

<style lang="less">
@import '~vux/src/styles/reset.less';

body {
  background-color: #fbf9fe;
}
</style>
