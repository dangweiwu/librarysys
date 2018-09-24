<template>
 <div>
     <Row >
          <Col span="6"  class='box'>
            <Row>
              <Col span='24' class='title'>
                借书记录生成
              </Col>
            </Row>
            <Row style='border-bottom: 1px solid #ddd'>
                <div class='item'>
                    <div class='mname'>学号:</div><div class='mvalue'>{{ok_user.sn}}</div>  
                </div>
                <div class='item'>
                    <div class='mname'>姓名:</div><div class='mvalue'>{{ok_user.name}}</div>
                </div>
                <div class='item'>
                    <div class='mname'>班级:</div><div class='mvalue'>{{ok_user.classx}}</div>
                </div>
            </Row>
            <Row v-for='(v,i) in list' style='border-bottom: 1px solid #ddd;padding: 10px 0;'>
                <Col span='24'>
                    <div class='item'>
                        <div class='mname'>编号</div><div class='mvalue'>{{v.sn}}</div>
                    </div>
                    <div class='item'>
                        <div class='mname'>书名</div><div class='mvalue'>{{v.title}}</div>
                    </div>
                    <div class='item' style='margin-bottom: 10px'>
                        <Button type="info" size='small' @click='delete_book(v,i)'>删除</Button>                                            
                    </div>
                </Col>
            </Row> 
            <Row>
              <br>
              <div style='text-align: center'>
                 <Button type="info" @click='borrow_book'>提交</Button>
                
              </div>
              
            </Row> 
          </Col>
          <Col span="18" class='box'>
            <Row style='border-bottom: 1px solid #ccc'>
                <Row>
                  <Col span='24' class='title'>
                    学生信息检索
                  </Col>
                </Row>
                <Row>
                  <Col span='24'>
                  <div style='float: left'>
                  <Input v-model='input' search enter-button placeholder="输入学号" style="width: 400px" @on-search='search'/>
                      
                  </div>
                  <div style='float: left;padding-left: 20px' >
                  <Button type="primary" @click='add_user'>添加</Button>                                            
                  </div>

                  </Col>
                 </Row>
                 <Row>

                  <Col span='24' style='padding-top: 10px;'>
                    <div class='item'>
                        <div class='mname'>学号:</div><div class='mvalue'>{{user.sn}}</div>  
                    </div>
                    <div class='item'>
                        <div class='mname'>姓名:</div><div class='mvalue'>{{user.name}}</div>
                    </div>
                    <div class='item'>
                        <div class='mname'>班级:</div><div class='mvalue'>{{user.classx}}</div>
                    </div>
                    <div class='item'>
                        <div class='mname'>可借数量:</div><div class='mvalue'>{{user.borrow_num}}</div>
                    </div>
                  </Col>  
                </Row> 
            </Row>
            <Row>

                <Row>
                    <Col span='24' class='title' style='margin-top: 10px;'>
                书籍信息检索
                    </Col>
                </Row>
                <Row>
                  <Col span='24'>
                  <div style='float: left'>
                  <Input v-model='book_input' search enter-button placeholder="输入编号" style="width: 400px" @on-search='search_book'/>
                      <br>
                  </div>
                  <div style='float: left;padding-left: 20px' >
                                                            
                  </div>
                  </Col>
                 </Row>


                 <Row >
                    <Table :columns="col_name" :data="book.results" stripe></Table>
                  </Row> 
                  <Row>
                    <br>
                    <Page :total="book.count" show-total :page-size='10' @on-change='page_change'/>
                  </Row> 
                
            </Row>
              
            
          </Col>
      </Row>
 </div>   
</template>

<script>
  import http from './http.js'
export default{
    data:function(){return{
        input:'',
        book_input:'',
        book_search:'',
        user:{sn:'',
            name:'',
            classx:'',
            borrow_num:'',},

        ok_user:{
          sn:null,
          name:null,
          classx:null,
          borrow_num:null
        },

        book:{
          results:[]
        },
        col_name:[
          {title:'编号',key:'sn',},
          {title:'名称',key:'title'},
          {title:'作者',key:'authors'},
          {title:'出版社',key:'publisher'},
          {title:'出版日期',key:'publication_date'},
          {title:'是否借出',key:'status',render:(h,params)=>{
            let s = params.row.status == 'in'?'未借出':'已借出'
            return h('span',{},s)  
          }},
          {title:'简介',key:'desc'},
          {title:'操作',key:'action',render:(h,params)=>{
            return h('Button',{on:{click:()=>{this.click_add_book(params.row)}},
                             props: {type: 'info',size: 'small'}},'添加')
          }}
          
        ],
        list:[]
    }},
    methods:{
        search:function(){
          var self = this
          http.get(HOST+'/user/',{params:{
            key:self.input,
          }}).then(function(response){
       
            
              var data = response.data
              if(!data.sn){
                self.$Message.error('无数据');
                self.user = {sn:'',
                            name:'',
                            classx:'',
                            borrow_num:'',}
                self.ok_user = {}

              }else{
                if(data.borrow_num){
                  data.borrow_num = 3-data.borrow_num
                }else{
                  data.borrow_num = 3
                }
                self.user = data
              }
        
          }).catch(function(error){

      
              try{
                self.$Message.error(error.response.data[0])

              }catch(error){
                self.$Message.error('获取数据失败');

              }

              self.user = {sn:'',
                            name:'',
                            classx:'',
                            borrow_num:'',}
               self.ok_user = {}



          })            
        },
        add_user:function(){
          this.ok_user = this.user
        },
        page_change:function(p){
          // console.log(p)
          var self = this
          http.get(HOST+'/book/?page='+p+'&search='+this.book_search)
          .then(function(response){
            // console.log(response)
            self.book = response.data
            // console.log(self.book)
          }).catch(function(error){
            // console.log(error)
            self.$Message.error('获取书籍数据失败');
          })
        },
        search_book:function(){
          var self = this
          self.book_search = this.book_input
            http.get(HOST+'/book/?search='+this.book_search).then(function(response){
              self.book = response.data
            }).catch(function(error){
              // console.log(error)
                            try{
                self.$Message.error(error.response.data[0])
              }catch(error){
                self.$Message.error('获取书籍数据失败');

              }
                
            })
        },
        click_add_book:function(v){
          var self = this
          if(v.status == 'out'){
                self.$Message.error('该书已被借出');
                return
          }
          else{
            self.list.splice(0,0,v)
          }
        },
        delete_book:function(v,i){
          this.list.splice(i,1)
        },
        borrow_book:function(){
          var self = this
          var data = {user_sn:'',book_sn:[],tag:'borrow'}
          data.user_sn = self.ok_user.sn
          for(var i in self.list){
            data.book_sn.splice(0,0,self.list[i].sn)
          }

          http.post(HOST+'/circulate/',data)
          .then(function(response){
            self.list = []
            self.book = {}
            self.ok_user = {}
            self.user = {}
            self.$Message.info('成功借书 '+response.data.num + ' 本')
          })
          .catch(function(error){
              try{
                self.$Message.error(error.response.data[0])
              }catch(error){
                self.$Message.error('提交失败');

              }
          })

        }
    }
}
</script>

<style scoped>
.box{
  min-height: 600px;
  padding: 20px;
}
.box + .box{
  border-left:1px solid #ddd;
}

.title{
  color:#464c5b;
  font-weight: 600;
  font-size: 16px;
  padding-bottom: 10px;
}

.mname,.mvalue{
    float: left;
    padding-left: 5px;
    font-size: 16px;
    height: 20px;
    line-height: 20px;
}

.mname{
    color:#808695;
    width: 100px;
}
.item{
    height: 20px;
    /*padding:10px 0;*/
    margin: 10px 0;
}
.mvalue{
  max-width: 150px;
}
</style>