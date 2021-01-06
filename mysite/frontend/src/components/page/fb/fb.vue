<template lang="pug">
 div.qhurikae
    a(:href="download_api" download v-show="!isloading")   
          img(src="/static/images/download.svg" @click="download_loading"  ).download
    a(v-show="isloading")    
      .spinner-border.spinner-border-sm.download
    ul.tag-pagination.ml-5.nav.nav-tabs 
      li  カテゴリー選択 
          i.fas.fa-arrow-circle-right
      li.nav-item.ml-5(:class="{'active': $route.name =='qhurikae-cros'}")
        a.nav-link 産業別
      li.nav-item(:class="{'active': $store.state.fb.type_index =='cli'}") 
        a.nav-link クライアント
      li.nav-item(:class="{'active': $route.name =='qhurikae-fb'}") 
        a.nav-link 商品名 
    transition(name="page" mode="out-in")
        keep-alive
            router-view(:key="$route.path") 
</template>

<script>
export default {
  data(){
      return{
          isloading: false
      }
   },
   created(){  
          //this.$store.dispatch('fb/getFb'),
          //this.$store.dispatch('fb/getData')
          this.$store.dispatch('dorento/getFb');
          this.$store.dispatch('dorento/getData');
   },
    computed:{
     download_api(){
        return  this.$store.state.fb.download_api ;
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

