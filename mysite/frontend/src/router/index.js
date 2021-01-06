import Vue from 'vue'
import Router from 'vue-router'

import LOGIN from '@/components/page/login'
import INDEX from '@/components/page/index'

import HOME from '@/components/page/home'
//menu 
import SIDEBAR from '@/components/menu/sidebar'
import TOPBAR from '@/components/menu/topbar'
//DORENTO 
import DORENTO from '@/components/page/dorento/dorento'
import DORENTOCROS from '@/components/page/dorento/dorento-cros'
import DORENTOFB from '@/components/page/dorento/dorento-fb'
import DORENTOLINE from '@/components/page/dorento/dorento-line'
// qhurikae
import QHURIKAE from '@/components/page/qhurikae/qhurikae'
import QHURIKAECROS from '@/components/page/qhurikae/qhurikae-cros'
import QHURIKAEFB from '@/components/page/qhurikae/qhurikae-fb'
import QHURIKAELINE from '@/components/page/qhurikae/qhurikae-line'


// FB 
import FB  from '@/components/page/fb/fb'
import FBDATA  from '@/components/page/fb/fb-data'

// LINE
import LINE from '@/components/page/line/line'
import LINEDATA  from '@/components/page/line/line-data'

// filter
import DORENTOFILTER from '@/components/filter/dorento-filter'
import QHURIKAEFILTER from '@/components/filter/qhurikae-filter'
import FACEBOOKFILTER from '@/components/filter/fb-filter'
import LINEFILTER from '@/components/filter/line-filter'

Vue.use(Router)



export default new Router({
  routes: [
    {
      path: "*",
      redirect: "login"
    },
    {
      path: '/login',
      name: 'login',
      components: {
        default: LOGIN ,
      }
    },
    {
      path: '/',
      name: 'home',
      components: {
        default: HOME ,
        sidebar: SIDEBAR,
        filter: DORENTOFILTER,
       
      },children:[
         {
          path:"/", 
          name: "home",
          meta: { requiresAuth: true }
         }
      ]
    },
    {
      path: '/dorento',
      components: {
        default: DORENTO ,
        sidebar: SIDEBAR,
        filter: DORENTOFILTER,
        meta: { requiresAuth: true }
        
      },
      children:[
        {
          name:"dorento-cros",
          path:"/",
          component: DORENTOCROS,
          meta: { requiresAuth: true }
        },
        {
          name:"dorento-fb",
          path:"fb",
          component: DORENTOFB,
          meta: { requiresAuth: true }
        },
        {
          name:"dorento-line",
          path:"line",
          component: DORENTOLINE,
          meta: { requiresAuth: true }
        },
      ]
    },
    {
      path: '/qhurikae',
      components:{
        default: QHURIKAE ,
        sidebar: SIDEBAR,
        filter: QHURIKAEFILTER,
        
       
      },
      children:[
        {
          name:"qhurikae-cros",
          path:"/",
          component: QHURIKAECROS,
          meta: { requiresAuth: true }
        },
        {
          name:"qhurikae-fb",
          path:"fb",
          component: QHURIKAEFB,
          meta: { requiresAuth: true }
        },  
        {
          name:"qhurikae-line",
          path:"line",
          component: QHURIKAELINE,
          meta: { requiresAuth: true }
        },

      ]
    },
    {
      path: '/fb-page',
      components:{
        default: FB ,
        sidebar: SIDEBAR,
        filter: FACEBOOKFILTER,
      },
      children:[
        {
          path:"/", 
          name: 'fb-page',
          component: FBDATA
        }
       
       ]

    },
    {
      path: '/line-page',
      components:{
        default: LINE ,
        sidebar: SIDEBAR,
        filter: LINEFILTER,
      },
      children:[
        {
          path:"/", 
          name: 'line-page',
          component: LINEDATA
        }
       
       ]

    }
  ]
})
