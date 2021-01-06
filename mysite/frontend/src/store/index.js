// 把vue給載進來
import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios' 
import dorento from './dorento'
import qhurikae from './qhurikae'
import fb from './fb'
import line from './line'

Vue.use(Vuex);

// 把環境建起來
export default new Vuex.Store({
    state:{
        filter: false , //篩選框狀態
      
    },
    actions:{
        actFilter(context,stats){  // 打開與關閉篩選框
            context.commit('setFilter', stats);
            $("html,body").scrollTop(0);
        },
       
    },
    mutations:{
        setFilter(state,stats){
            state.filter = stats ;
        },
    },
    modules:{
        dorento ,  
        qhurikae ,
        fb ,
        line
    }
    
});