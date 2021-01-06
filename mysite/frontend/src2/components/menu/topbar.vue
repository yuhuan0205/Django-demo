<template lang="pug">
    nav.navbar
        a.sidebar-toggler(href='#')
            i(data-feather='menu')
        li.title {{toptitle}}  
        .navbar-content
            ul.navbar-nav
                li.nav-item.dropdown.nav-apps
                    i.far.fa-compass#filter_open(@click="filter_open" v-show="$route.name!= 'home'")
                li.nav-item.dropdown
                    a#languageDropdown.nav-link.dropdown-toggle(href='#' role='button' data-toggle='dropdown' aria-haspopup='true' aria-expanded='false')
                        i.flag-icon.flag-icon-jp.mt-1
                        span.font-weight-medium.ml-1.mr-1 JAPAN
                    .dropdown-menu(aria-labelledby='languageDropdown')
                        a.dropdown-item.py-2(href='javascript:;')
                            i#jp.flag-icon.flag-icon-jp(title='jp')
                            span.ml-1  Japan 
                        a.dropdown-item.py-2(href='javascript:;')
                            i#tw.flag-icon.flag-icon-tw(title='tw')
                            span.ml-1  Taiwan 
                        a.dropdown-item.py-2(href='javascript:;')
                            i#de.flag-icon.flag-icon-de(title='de')
                            span.ml-1  German 
                        a.dropdown-item.py-2(href='javascript:;')
                            i#pt.flag-icon.flag-icon-pt(title='pt')
                            span.ml-1  Portuguese 
                        a.dropdown-item.py-2(href='javascript:;')
                            i#es.flag-icon.flag-icon-es(title='es')
                            span.ml-1  Spanish 
                li.nav-item.dropdown.nav-profile
                    a#profileDropdown.nav-link.dropdown-toggle(href='#' role='button' data-toggle='dropdown' aria-haspopup='true' aria-expanded='false')
                        img(src='/static/images/user.png' alt='profile')
                    .dropdown-menu(aria-labelledby='profileDropdown')
                        .dropdown-header.d-flex.flex-column.align-items-center
                            .figure.mb-3
                                img(src='https://via.placeholder.com/80x80' alt='')
                            .info.text-center
                                p.name.font-weight-bold.mb-0 Amiah Burton
                                p.email.text-muted.mb-3 amiahburton@gmail.com
                            .dropdown-body
                                ul.profile-nav.p-0.pt-3
                                    li.nav-item
                                        a.nav-link(href='pages/general/profile.html')
                                            i(data-feather='user')
                                            span Profile
                                    li.nav-item
                                        a.nav-link(href='javascript:;')
                                            i(data-feather='edit')
                                            span Edit Profile
                                    li.nav-item
                                        a.nav-link(href='javascript:;')
                                            i(data-feather='repeat')
                                            span Switch User
                                    li.nav-item
                                        a.nav-link(href='javascript:;')
                                            i(data-feather='log-out')
                                            span Log Out
                li.nav-item.dropdown
                    buttpn.logout(@click.prevent="sign_out") 登出
 

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
   i.far.fa-compass{
     font-size: 1.5em;
     cursor: url('/static/images/click.ico') ,auto !important;
   } 
   .logout{
       cursor: url('/static/images/click.ico') ,auto !important;
   }
   
</style>