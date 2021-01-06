<template lang="pug">
    nav.sidebar
        .sidebar-header
            a.sidebar-brand(href='#') STA可視化
               span.ml-1 
                i.far.fa-star 
            .sidebar-toggler.not-active
                    span
                    span
                    span
        .sidebar-body
            ul.nav
                li.nav-item(v-for="item in menu" )
                     
                    router-link(:to="item.link" ).nav-link
                        span(:class="{ 'active' : $route.name.includes(item.page) }")
                            i(:class="item.class") 
                            span()  {{item.name}}           
                    
                        
</template>

<script>
export default {
     name: "sidebar",
     data(){
       return{
          menu: [
              {name:"ホームページ",class:"fa fa-home",link:"/",page:"home"},
             // {name:"ATC率",class:"fa fa-shopping-cart",link:""},
             // {name:"滞在率",class:"fa fa-hourglass-start",link:""},
             // {name:"遷移率",class:"fa fa-external-link",link:""},
              {name:"トレンド",class:"fa fa-user-o",link:"/dorento" ,page: "dorento"},
              {name:"Q振り返り",class:"fa fa-bar-chart",link:"/qhurikae",page:"qhurikae"}
          ]
       }  
     },
     


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
        background-image: linear-gradient(to right, #434343 0%, #070d19 100%);
        border-bottom: #000;
            
      }
      .sidebar-body{
           background-image: linear-gradient(to right, #434343 0%, #070d19 100%);
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
      .title{
        position: absolute;
        left: 2em;
        line-height: 1em;
        list-style: none;
      }
      span.active{
        background: #fff;
        color: #000;
        padding: 10px;
        width: 80%;
        border-radius: 5px;
        display: flex;
        justify-content: center;
        i{
            font-size: 1.5em;
            opacity: 1; 
            margin-right: 5px;
        }
        
      }
     

  }
    
     
</style>
