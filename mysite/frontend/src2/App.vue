<template lang="pug">
 #app
    .main-wrapper
      router-view(name="sidebar")
      TOPBAR(v-show="$route.name!= 'login'")
      div
        router-view(name="filter"  v-show="closeFilter")
      .page-wrapper.my-2
        .page-content(v-show="$route.name!= 'login'")
          .d-flex.justify-content-between.align-items-center.flex-wrap.grid-margin
            ul.dateChange(v-show="$route.name!= 'home'")
              label(@click="typeChang('q')" :class="{'date-active': dateType =='q' }") 季
              label(@click="typeChang('m')" :class="{'date-active': dateType =='m' }") 月
              label(@click="typeChang('')"  :class="{'date-active': dateType =='' }") 日
            .datepicker-group(v-show="$route.name!= 'home'")
                    input.datepicker_box(type='date' v-model="date2" @change="dateChange")
                    input.datepicker_box(type='date' v-model="date1" @change="dateChange" )
                    button.send-date(@click='sendDate')
                          | 檢索
                          i.fas.fa-search.ml-1         
                    .time-dorento-now.mt-2
                          span.time-title  時間範囲 
                          i.fas.fa-long-arrow-alt-right.ml-2
                          span.ml-2 {{date2}} 
                          span.ml-2  ～
                          span.ml-2 {{date1}}
                          
        transition(name="page" mode="out-in")                  
            keep-alive          
                router-view
              
</template>

<script>
import TOPBAR from '@/components/menu/topbar';
export default {
  name: 'App',
  components:{
    TOPBAR
  },
  data:function(){
    return{
       filter: false,
       dateType: "",
       date1: "", //時間用
       date2: "", //時間用
       send: 0,
    }
  },
  created(){
    this.filter_api = this.$route.path
    let theDay = new Date()   // 建立時間物件
    let changeDay = 30        // 設定要往前或往後幾天
    this.date1 = theDay.toISOString().substring(0,10);
    let timeStamp = theDay.setDate(theDay.getDate() - changeDay)      // theDay.getDate() 是用來取得今天是幾號
    this.date2 = theDay.toISOString().substring(0,10);
    let date1 = this.date1;
    let date2 = this.date2;
    this.$store.dispatch('dorento/getTime',{date1,date2}); 
    this.$store.dispatch('qhurikae/getTime',{date1,date2}); 
    
  },
  computed:{
     closeFilter(){
        return  this.$store.state.filter ;
     },
     
  },
  methods:{
    typeChang(type){
      this.dateType = type;
      this.$store.dispatch('dorento/timeType',type);
      this.$store.dispatch('qhurikae/timeType',type);
    },
    dateChange(){
      let date1 = this.date1;
      let date2 = this.date2;
      this.$store.dispatch('dorento/getTime',{date1,date2});
      this.$store.dispatch('qhurikae/getTime',{date1,date2});
    },
    sendDate(){
       //this.send ++;
      this.$store.dispatch('dorento/getCros');
      this.$store.dispatch('dorento/getFb');
      this.$store.dispatch('dorento/getLine');
      this.$store.dispatch('dorento/getData');

      this.$store.dispatch('qhurikae/getCros');
      this.$store.dispatch('qhurikae/getFb');
      this.$store.dispatch('qhurikae/getLine');
      this.$store.dispatch('qhurikae/getData');
    },
    




 },
 

}
</script>

<style lang="scss"> 
  @import '@/assets/all.scss' ;

</style>
