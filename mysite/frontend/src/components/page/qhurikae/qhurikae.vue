<template lang="pug">
 div.qhurikae
    a(:href="download_api" download v-show="!isloading")   
          img(src="/static/images/download.svg" @click="download_loading"  ).download
    a(v-show="isloading")    
      .spinner-border.spinner-border-sm.download
    ul.tag-pagination.nav.nav-tabs
      router-link(to="/qhurikae/")
        label(:class="{'active': $route.name =='qhurikae-cros'}") CROS 
      router-link(to="/qhurikae/fb")
        label(:class="{'active': $route.name =='qhurikae-fb'}")  FB
      router-link(to="/qhurikae/line")  
        label(:class="{'active': $route.name =='qhurikae-line'}") LINE   
    transition(name="page" mode="out-in")
        keep-alive
            router-view( :key="$route.path") 
</template>

<script>
export default {
  data(){
      return{
          isloading: false
      }
   },
   created(){ 
            this.$store.dispatch('qhurikae/getCros');
            this.$store.dispatch('qhurikae/getFb');
            this.$store.dispatch('qhurikae/getLine');
            this.$store.dispatch('qhurikae/getData');

   },
    computed:{
     download_api(){
        return  this.$store.state.qhurikae.download_api ;
     }
   },
   methods:{
      download_loading(){
         this.isloading = !this.isloading;
         let api = this.download_api ; 
         this.$http.get(api).then((res) => {
                if(res){
                    this.isloading = !this.isloading;
                    alert('下載成功');
                }else{
                    return 
                }

           })
      }

   }
 
}
</script>

