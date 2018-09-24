<template>
    <div>
        <br>
    <div style='text-align: center'>
    <h4 style='margin: 0 auto;'>新闻.公告</h4>
        
    </div>
    <!-- <br> -->
        <panel :list="list" type="4"></panel>

        <load-more :show-loading="false" v-if='next' :tip="more" @click.native='get_more_message' background-color="#fbf9fe"></load-more>
        <load-more :show-loading="false"  v-if='!next' :tip="more"  background-color="#fbf9fe"></load-more>

    </div>
</template> 

<script>
    import http from '@/http'
    import { Panel, Group, Radio, LoadMore } from 'vux'
    export default{
          components: {
            Panel,
            Group,
            Radio,
            LoadMore
          },
        name:'message',
        data:function(){return{
            count:0,
            next:'',
            prev:null,
            more:'没有更多数据',
            list:[ 

            ]
        }},
        methods:{
            get_message(){
                http.get('/news/').then((response)=>{
                    let data = response.data
                    this.count = data.count
                    this.next = data.next
                    this.prev = data.previous
                    let tmp_data = []
                    let rd = data.results
                    for(var i in rd){
                        console.log(i)
                        tmp_data.push({
                            title:rd[i].title,
                            desc:rd[i].content,
                            meta:{date:rd[i].add_time,source:rd[i].author},
                        })


                    }
                    this.list = tmp_data
                    console.log(this.list)
                    if(this.next){
                        this.more = '点击加载更多数据'
                    }else{
                        this.more = '没有更多数据'
                    }
                })
            },
            get_more_message(){
                http.get(this.next).then((response)=>{
                    let data = response.data
                    this.count = data.count
                    this.next = data.next
                    this.prev = data.previous
                    let tmp_data = []
                    let rd = data.results
                    for(var i in rd){
                        console.log(i)
                        tmp_data.push({
                            title:rd[i].title,
                            desc:rd[i].content,
                            meta:{date:rd[i].add_time,source:rd[i].author},
                        })


                    }
                    this.list = this.list.concat(tmp_data)
                    console.log(this.list)
                    if(this.next){
                        this.more = '点击加载更多数据'
                    }else{
                        this.more = '没有更多数据'
                    }

                })
            }
        },
        mounted:function(){
            if(this.$store.state.TAB != 0){
                this.$store.commit('go_tab',0)
            }
            this.get_message()
        }
    }
</script>  
<style>
    
</style>