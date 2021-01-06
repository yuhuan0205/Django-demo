<template lang="pug">
    nav.navbar
        a.sidebar-toggler(href='#')
            i(data-feather='menu')
        li.title {{toptitle}}  
        .navbar-content  
            ul.navbar-nav 
                li.nav-item.dropdown.filter-apps(@click="filter_open")
                    button.logout
                        i.fas.fa-th-large#filter_open
                        span.ml-2(@click="filter_open") 検索条件 
                li.nav-item.dropdown.ml-3
                    buttpn.logout(@click.prevent="sign_out")
                        i.fas.fa-sign-out-alt.mr-1
                        span  ログアウト
 

    </template>
<script scr="@/assets/js/main.js"></script>
<script>
export default {
  props:['toptitle'],
  data:function(){
      return{
          newUrl: this.toptitle
      }
  },
  methods:{
      filter_open(){
         // const vm = this;
         // alert(vm.$route.name);
          this.$store.dispatch('actFilter',true);
      },
      sign_out(){
          const api = `${process.env.APIPATH}/client/log_out`;
          const vm =  this;
             this.$http.get(api).then((res) => {
                if(res.data.success){
                    vm.$router.push('/login');
                }
              })
      }
  }
}
</script>

<style scoped lang="scss">
    nav{
       position: fixed;
       top: 0;
       z-index: 10000000000; 
    }
   .title{
        position: absolute;
        left: 2em;
        line-height: 1em;
        list-style: none;
    }
  
   .logout{
       transition: 0.5s;
       border: none;
       background: none;
       color:#fff;
        &:hover{
         background: #fff;
         color: #000;
         padding: 5px;
         border-radius: 3px;
         vertical-align:middle;
      }
      i,span{
          cursor: url('/static/images/click.ico') ,auto !important;
          font-size: 1em;
          vertical-align:middle;
      }
   }
   
</style>