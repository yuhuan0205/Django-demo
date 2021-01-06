// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue";
import Vuex from "vuex";
import App from "./App";
import router from "./router";
import axios from "axios"; //主要的ajax套件
import VueAxios from "vue-axios"; //將他轉為vue的套件 之後就可以用this的方法運行他
import Loading from "vue-loading-overlay"; //component
import "bootstrap";
import store from "./store";
Vue.component("Loading", Loading); // 全域元件
Vue.filter("$toCurrency", function(num) { 
  //轉換千分位 用於表格
  let new_num = num;
  var parts = new_num.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
});
Vue.prototype.$proCurrency = function(num){//   千分位函式 用於圖表 需要再研究
  
  let new_num = num;
  var parts = new_num.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
};
Vue.prototype.$chart_scale = function (card){
  console.log(card);
  const acard = document.querySelector(`.${card}`);
  screenfull.request(acard);
  if (screenfull) {
    screenfull.exit(acard);
  }
 };




Vue.use(VueAxios, axios); //轉為套件之後 再用ues的方式運行他
Vue.use(Vuex);
Vue.config.productionTip = false;

axios.defaults.withCredentials = true; // 把cookie打開
Vue.config.productionTip = false;

/*
router.beforeEach((to, from, next) => {
    if(to.meta.requiresAuth){
      const api = `${process.env.APIPATH}/client/check`;
      console.log(process.env.APIPATH);
      axios.get(api).then((res) => {
         console.log(res.data);
         if(res.data.success){
             next(); 
         }else{
             next({
                path: '/login',
             });
         }
       })  
    }else{
      next();
    }
    
})
/* eslint-disable no-new */
new Vue({
  el: "#app",
  router,
  store,
  components: { App },
  template: "<App/>"
});
