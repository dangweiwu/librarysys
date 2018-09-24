<template>
    <div>
          <x-dialog v-model="show" hide-on-blur :dialog-style="{'max-width': '100%', width: '100%', height: '50%', 'background-color': 'transparent'}" @click="showDialogStyle = false">
              
              
        <div style='background: #fff;padding: 10px;margin:0 15px'>
        <p style='text-align: left'><span style='color:red;padding-right: 5px'>编号:</span><span>{{tmp.sn}}</span></p>
        <p style='text-align: left'><span style='color:red;padding-right: 5px'>书名:</span><span>{{tmp.title}}</span></p>
        <p style='text-align: left'><span style='color:red;padding-right: 5px'>作者:</span><span>{{tmp.authors}}</span></p>
        <p style='text-align: left'><span style='color:red;padding-right: 5px'>出版社:</span><span>{{tmp.publisher}}</span></p>
        <p style='text-align: left'><span style='color:red;padding-right: 5px'>借书日期:</span><span>{{tmp.time}}</span></p>
        <p style='text-align: left'><span style='color:red;padding-right: 5px'>还书日期:</span><span>{{tmp.back_time}}</span></p>

        </div>
          </x-dialog>
        <group title='个人信息维护'>
            <x-input title="昵称" v-model='username' class="weui-vcode">
                <x-button slot="right" type="primary" mini @click.native='set_username'>修改</x-button>
            </x-input>
            <x-input title="密码" class="weui-vcode" v-model='passwrod'>
                <x-button slot="right" type="primary" mini @click.native='set_password'>修改</x-button>
            </x-input>


        </group>
        <group title='借书记录查询' style='font-size: 14px'>
            <cell-box >

                <flexbox >
                    <flexbox-item>
                        <span style='color:red'>书名</span>
                    </flexbox-item>
                    <flexbox-item>
                        <span style='color:red'>还书日期</span>
                    </flexbox-item>
                </flexbox>
                
            </cell-box>
            <cell-box v-for='(v,i) in results' :key='i' style='font-size: 14px;' @click.native='get_info(v)'>

                <flexbox >
                    <flexbox-item>
                        {{v.books.title}}
                    </flexbox-item>
                    <flexbox-item>
                        <span v-if='v.back_time'>{{ v.back_time }}</span>
                        <span v-else>未还</span>

                    </flexbox-item>
                </flexbox>
                
            </cell-box>
            <cell-box v-if='next' @click='get_more_history()' >
                <div style='margin: 0 auto;color:#999;font-size: 14px'>点击加载更多...</div>
            </cell-box>
            <cell-box >
                <div style='margin: 0 auto;color:#999;font-size: 14px'> 没有更多数据</div>
               
            </cell-box>
        </group>

        
    </div>
</template> 

<script>
        import http from '@/http'
    import { Group,XInput,XButton,CellBox,Flexbox, FlexboxItem,XDialog } from 'vux'
    export default{
      components: {
        XInput,XButton,Group,CellBox,Flexbox, FlexboxItem,XDialog
      },

        name:'my',
        data:function(){return{
            username:'',passwrod:'',next:'',results:[],show:false,tmp:{}


            }},
        methods:{
            set_username(){
                var self = this
                http.post('/user/',{'username':this.username}).then((r)=>{

                    this.$vux.alert.show({title:'提示',content:'修改成功'})
                    localStorage.setItem('token','')
                    this.$router.push({path:'/message'})

                }).catch((e)=>{

                    try{
                       self.$vux.alert.show({'title':'提示',content:e.response.data[0],onHide:()=>{
                        localStorage.setItem('token','')
                        this.$router.push({path:'/'})
                    } })

                    }catch(e){
                        self.$vux.alert.show('修改失败')
                    }
                })    
            },
            set_password(){
                http.post('/user/',{'password':this.passwrod}).then(r=>{
                    this.$vux.alert.show({title:'提示',content:'修改成功',onHide:()=>{
                        localStorage.setItem('token','')
                        this.$router.push({path:'/message'})
                    }})})
                    .catch(e=>{
                        console.log('------------')
                        try{
                           this.$vux.alert.show({'title':'提示',content:e.response.data[0]})
                        console.log('------------1')

                        }catch(e){
                            this.$vux.alert.show('修改失败')
                        console.log('------------2')

                        }
                    })

                
            },
            get_borrow_history(){
                http.get('/borrow').then(response=>{
                    this.next = response.data.next
                    this.results = response.data.results
                    // console.log(response.data)
                })
            },
            get_more_history(){
                http.get(this.next).then(response=>{
                    this.next = response.data.next
                    this.results = this.results.concat(response.data.results)
                })
            },
            get_info(v){
                this.tmp = v.books
                this.tmp.time = v.time
                this.tmp.back_time = v.back_time

                this.show = true
            }

        },
        mounted:function(){
            if(this.$store.state.TAB != 2){
                this.$store.commit('go_tab',2)
            }
            this.username = localStorage.getItem('username')
            this.get_borrow_history()
        }

    }
</script>  
<style>
    
</style>