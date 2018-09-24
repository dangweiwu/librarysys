<template>
    <div>
        <x-dialog v-model="show" hide-on-blur :dialog-style="{'max-width': '100%', width: '100%', height: '50%', 'background-color': 'transparent'}" @click="showDialogStyle = false">
        <div style='background: #fff;padding: 10px;margin:0 15px'>
            

        <p style='text-align: left'><span style='color:red;padding-right: 5px'>编号:</span><span>{{tmp.sn}}</span></p>
        <p style='text-align: left'><span style='color:red;padding-right: 5px'>书名:</span><span>{{tmp.title}}</span></p>
        <p style='text-align: left'><span style='color:red;padding-right: 5px'>作者:</span><span>{{tmp.authors}}</span></p>
        <p style='text-align: left'><span style='color:red;padding-right: 5px'>出版社:</span><span>{{tmp.publisher}}</span></p>
        <p style='text-align: left'><span style='color:red;padding-right: 5px'>出版日期:</span><span>{{tmp.publication_date}}</span></p>
        <p style='text-align: left'><span style='color:red;padding-right: 5px'>存放房间:</span><span>{{tmp.category.room}}</span></p>
        <p style='text-align: left'><span style='color:red;padding-right: 5px'>存放位置:</span><span>{{tmp.category.site}}</span></p>

        <p style='text-align: left'><span style='color:red;padding-right: 5px'>类别:</span><span>{{tmp.category.name}}</span></p>
        <p style='text-align: left'><span style='color:red;padding-right: 5px'>是否借出:</span><span>{{tmp.status=='in'?'未借出':'已借出'}}</span></p>
        </div>

      </x-dialog>
      <search
      v-model="value"
      position="absolute"
      @on-submit="onSubmit"
      
      ref="search">
           <group>
            <cell-box v-for='(v,i) in list' @click.native='info(v)'>
             <span style='padding-right: 5px'>{{v.sn}}</span> <span>{{v.title}}</span>   
            </cell-box>
            <cell-box>
                        <load-more :show-loading="false" v-if='next' tip="点击查看更多数据" @click.native='get_more_book' background-color="#fbf9fe"></load-more>
        <load-more :show-loading="false"  v-if='!next' tip="没有更多数据"  background-color="#fbf9fe"></load-more>
            </cell-box>
           </group>    

      </search>
    </div>
</template> 

<script>
    import { XDialog,Search, Panel,CellBox,Group,LoadMore,Actionsheet} from 'vux'
    import http from '@/http'

    export default{
        components: {
         Search,
         Panel,
         CellBox,
         Group,
         LoadMore,
         Actionsheet,
         XDialog
        },
        name:'books',
        data:function(){return{
        
            show:false,
            tmp:{category:{}},
            next:'',
            value:'',
            results:[],
            list:[]
        }},
        methods:{
            onSubmit(){
                console.log(this.value)
                http.get('/book/',{params:{search:this.value}}).then((r)=>{
                    this.next = r.data.next
                    this.list = r.data.results
                })
            },
            info(v){
                this.tmp = v
                this.show = true
            },
            get_more_book(){
                http.get(this.next).then((r)=>{
                    this.next = r.data.next
                    this.list = this.list.concat(r.data.results)
                })
            }
        },
        mounted:function(){
            if(this.$store.state.TAB != 1){
                this.$store.commit('go_tab',1)
            }
        }
        
    }
</script>  
<style>
    
</style>