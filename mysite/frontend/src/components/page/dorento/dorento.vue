<template lang="pug">
 div.dorento
    a(:href="download_api" download v-show="!isloading")   
          img(src="/static/images/download.svg" @click="download_loading"  ).download
    a(v-show="isloading")    
      .spinner-border.spinner-border-sm.download       
    ul.tag-pagination.nav.nav-tabs 
      router-link(to="/dorento/" )
        label(:class="{'active': $route.name =='dorento-cros'}" ) CROS 
      router-link(to="/dorento/fb"  )
        label(:class="{'active': $route.name =='dorento-fb'}" )  FB
      router-link(to="/dorento/line")  
        label(:class="{'active': $route.name =='dorento-line'}" ) LINE            
    transition(name="page" mode="out-in")
        keep-alive
            router-view(:key="$route.path") 

</template>

<script>
export default { 
   data(){
      return{
          isloading: false,
          data: -1,
      }
   },
   created(){
            this.$store.dispatch('dorento/getCros');
            this.$store.dispatch('dorento/getFb');
            this.$store.dispatch('dorento/getLine');
            this.$store.dispatch('dorento/getData');
   },
   computed:{
     download_api(){
        return  this.$store.state.dorento.download_api ;
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

<style lang="scss">

</style>