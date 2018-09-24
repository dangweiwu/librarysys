<template>
 <div style='padding: 20px;max-width: 1000px '>

    <Row> 
            <Input v-model='input' search enter-button placeholder="输入学号" style="width: 400px" @on-search='search'/>
    </Row>
    <Row style='border-bottom: 1px solid #ddd'>
        <div class='item'>
            <div class='mname'>学号:</div><div class='mvalue'>{{user.sn}}</div>  
        </div>
        <div class='item'>
            <div class='mname'>姓名:</div><div class='mvalue'>{{user.name}}</div>
        </div>
        <div class='item'>
            <div class='mname'>班级:</div><div class='mvalue'>{{user.classx}}</div>
        </div>
    </Row>
    <Row>
        <Col span='24'>
            <div v-for='(v,i) in books' style='border-bottom: 1px solid #ddd;padding:10px 0;'>

                <div class='item'>
                    <div class='mname'>编码:</div><div class='mvalue'>{{v.books.sn}}</div>  
                </div>
                <div class='item'>
                    <div class='mname'>书名:</div><div class='mvalue'>{{v.books.title}}</div>
                </div>
                <div class='item'>
                    <div class='mname'>借书日期:</div><div class='mvalue'>{{v.time}}</div>
                </div>
                <div class='item' style='margin-bottom: 10px'>
                        <Button type="primary" @click='back_book(v)'>还书</Button>                                            
                    
                </div>
                
            </div>


        </Col>
    </Row> 
 </div>   
</template>

<script>
  import http from './http.js'

export default{
    data:function(){return{
        input:'',
        user_back:'',
        user:{
            name:'',
            sn:'',
            classx:''
        },
        books:[]
    }},
    methods:{
         search:function(){
          var self = this
          http.get(HOST+'/user/',{params:{
            key:self.input,
          }}).then(function(response){
       
            var data = response.data
            if(!data.sn){
                self.$Message.error('该学号不存在');
                return
              }
              self.user_back = data.sn
                self.user = data
                self.get_book_info()
          }).catch(function(error){
              try{
                self.$Message.error(error.response.data[0])
              }catch(error){
                self.$Message.error('获取用户数据失败');

              }

          })},
        get_book_info:function(){
            // 查询未还书籍
            var self = this
            http.get(HOST + '/borrow/',{params:{user_sn:self.user_back}}).then(function(response){
                self.books = response.data.results
            }).catch(function(error){
            try{
                self.$Message.error(error.response.data[0])
              }catch(error){
                self.$Message.error('获取书籍数据失败');

              }
            })
                     
        },
        back_book:function(row,i){
            var self = this
            http.post(HOST+'/circulate/',{'tag':'back','book_sn':row.books.sn,'user_sn':self.user_back})
            .then(function(response){
                self.books.splice(i,1)
                self.$Message.info('还书成功')

            })
            .catch((error)=>{
                self.$Message.error('还书失败')
            })
            
        },
    }
}
</script>

<style scoped>
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
</style>