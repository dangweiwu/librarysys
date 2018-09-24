<template>
    <div class="layout">
        <Layout>
            <Header>
                <Menu mode="horizontal" theme="dark" active-name="1">
                    <div class="layout-logo" style='color:#fff;line-height: 30px;text-align: center;font-size: 20px;width: 140px'>
                      书籍借还系统
                    </div>
                    <div class="layout-nav">
                        <MenuItem :name="i+1" v-for='(v,i) in $router.options.routes' :key='i' :to='v.path'>
                            <Icon :type="v.icon"></Icon>
                            {{v.mname}}
                    
                        </MenuItem>
                    </div>
                </Menu>
            </Header>
            <Content :style="{padding: '0 10px','min-height':'650px'}">
              <router-view></router-view>
            </Content>
            <Footer class="layout-footer-center">2011-2016 &copy; lambdang</Footer>
        </Layout>
    </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  mounted:function(){
    this.$router.push('/borrow')
    console.log(this.$router)
    console.log(this.$router.options.routes)
    console.log(this.$routes)
  }
}
</script>

<style>


*{
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
}
.layout{
    border: 1px solid #d7dde4;
    background: #f5f7f9;
    position: relative;
    border-radius: 4px;
    overflow: hidden;
    min-width: 1000px;
}
.layout-logo{
    width: 100px;
    height: 30px;
    background: #5b6270;
    border-radius: 3px;
    float: left;
    position: relative;
    top: 15px;
    left: 20px;
}
.layout-nav{
    width: 210px;
    margin: 0 auto;
    margin-right: 20px;
}
.layout-footer-center{
    text-align: center;
}


</style>
