<template lang="pug">
    nav.sidebar
        .sidebar-header
            a.sidebar-brand(href='#') STA可視化
               span.ml-1 
                i.far.fa-star 
            .sidebar-toggler.not-active(@click="menu")
                    span
                    span
                    span
        .sidebar-body
            ul.nav
                li.nav-item.nav-category.h1 全体
                li.nav-item(v-for="item in home" ) 
                    router-link(:to="item.link" ).nav-link
                        span(:class="{ 'active' : $route.name.includes(item.page) }")
                            i(:class="item.class") 
                            span.link-title  {{item.name}} 
                li.nav-item.nav-category 営業
                li.nav-item(v-for="item in business" ) 
                    router-link(:to="item.link" ).nav-link
                        span(:class="{ 'active' : $route.name.includes(item.page) }")
                            i(:class="item.class") 
                            span.link-title {{item.name}} 
                li.nav-item.nav-category
                 // メディア
                li.nav-item(v-for="item in media" ) 
                    router-link(:to="item.link" ).nav-link
                        span(:class="{ 'active' : $route.name.includes(item.page) }")
                            i(:class="item.class" ) 
                            span.link-title  {{item.name}}                                 
                                   
</template>

<script>
export default {
     name: "sidebar",
     data(){
       return{
          home: [
              {name:"ホームページ",class:"fa fa-home",link:"/",page:"home"},
             // {name:"ATC率",class:"fa fa-shopping-cart",link:""},
             // {name:"滞在率",class:"fa fa-hourglass-start",link:""},
             // {name:"遷移率",class:"fa fa-external-link",link:""},
          ] ,
          business: [
              {name:"トレンド",class:"fa fa-user-o",link:"/dorento" ,page: "dorento"},
              {name:"Q振り返り",class:"fa fa-bar-chart",link:"/qhurikae",page:"qhurikae"}
          ],
          media:[   
             // {name:"FACEBOOK",class:"fab fa-facebook",link:"/fb-page",page:"fb-page"},
              //{name:"LINE",class:"fab fa-line",link:"/line-page",page:"line-page"}
          ] 
       }  
     },
     methods:{
         menu(){
             $(".active").css('bacground','none');
         }
     }
     

};
</script>
<style scoped lang="scss">
  nav.sidebar{
      .sidebar-toggler.not-active{
          cursor: url('/static/images/click.ico') ,auto ;
          span{
                cursor: url('/static/images/click.ico') ,auto ;
          }

      }
      .sidebar-header{
        
        border-bottom: #000;
      }
      .sidebar-body{
         
           ul{
               width: 100%;
           }
      }
      .nav-link{
          cursor: url('/static/images/click.ico') ,auto !important;
      }
      .nav-item{
          color:#fff;
          display: block;
          margin-top: 0.8em;
          
          span ,i{
             font-size: 1em;
             cursor: url('/static/images/click.ico') ,auto !important;
          }
      } 
      span.active{
        background: #fff;
        color: #000;
        padding: 10px;
        width: 100%;
        border-radius: 5px;
        display: flex;
       
        i{
            font-size: 1.5em;
            opacity: 1; 
         
        }
        span{
           
        }
        
      }
     

  }
    
     
</style>
