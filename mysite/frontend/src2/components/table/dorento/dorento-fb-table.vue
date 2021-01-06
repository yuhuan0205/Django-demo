<template lang="pug">
div
   TOPBAR
   .col-12.stretch-card.ml-3.mb-4
        .card
            .card-body
                .d-flex.justify-content-between.align-items-baseline.mb-2
                    h6.card-title.mb-0 
                      i.fas.fa-table.ml-1
                      span.ml-3 総表
                    span(v-show="(clients.length)>1") 順序調整
                        i.fas.fa-long-arrow-alt-right.ml-3
                        span.order-filter(:class="{'order-filter-active':lowhight == 'low'}" @click="lowhight ='low'") 低い
                        span.order-filter.mr-3(:class="{'order-filter-active':lowhight == 'high'}" @click="lowhight ='high'") 高い
                        span 変更
                    .dropdown.mb-2 
                        button#dropdownMenuButton7.btn.p-0(type='button', data-toggle='dropdown', aria-haspopup='true', aria-expanded='false')
                            i.icon-lg.text-muted.pb-3px(data-feather='more-horizontal')
                    .dropdown-menu.dropdown-menu-right(aria-labelledby='dropdownMenuButton7')
                        a.dropdown-item.d-flex.align-items-center(href='#')
                            i.icon-sm.mr-2(data-feather='eye')
                            span View
                        a.dropdown-item.d-flex.align-items-center(href='#')
                            i.icon-sm.mr-2(data-feather='edit-2')
                            span Edit
                        a.dropdown-item.d-flex.align-items-center(href='#')
                            i.icon-sm.mr-2(data-feather='trash')
                            span Delete
                        a.dropdown-item.d-flex.align-items-center(href='#')
                            i.icon-sm.mr-2(data-feather='printer')
                            span Print
                        a.dropdown-item.d-flex.align-items-center(href='#')
                            i.icon-sm.mr-2(data-feather='download')
                            span Download    
                .table-responsive
                    table.table.table-hover.mb-0
                        thead
                            tr
                                th.pt-0 番号
                                th.pt-0(@click="orderBytable('client')")
                                    span(:class="{'order-active' :order == 'client' }") クライアント
                                th.pt-0(@click="orderBytable('imp')")
                                    span(:class="{'order-active' :order == 'imp' }") imp
                                th.pt-0(@click="orderBytable('click')")  
                                    span(:class="{'order-active' :order == 'click' }") Click
                                th.pt-0(@click="orderBytable('ctr')") 
                                    span(:class="{'order-active' :order == 'ctr' }") CTR
                                th.pt-0(@click="orderBytable('cpc')") 
                                    span(:class="{'order-active' :order == 'cpc' }") CPC
                                th.pt-0(@click="orderBytable('cpm')") 
                                    span(:class="{'order-active' :order == 'cpm' }") CPM
                                th.pt-0(@click="orderBytable('cv')") 
                                    span(:class="{'order-active' :order == 'cv' }") CV
                                th.pt-0(@click="orderBytable('cvr')")  
                                    span(:class="{'order-active' :order == 'cvr' }") CVR
                                th.pt-0(@click="orderBytable('cpo')") 
                                    span(:class="{'order-active' :order == 'cpo' }") CPO
                                th.pt-0(@click="orderBytable('cost')")
                                    span(:class="{'order-active' :order == 'cost' }") Cost
                                
                        tbody
                            tr(v-for=" (item,key) in fbTable")
                                td {{key+1}}
                                td
                                    span(:class="{'order-spna' :order == 'client' }") {{item.client}}
                                td
                                    span(:class="{'order-spna' :order == 'imp' }") {{item.imp | | $toCurrency}}
                                td
                                    span(:class="{'order-spna' :order == 'click' }") {{item.clicks | | $toCurrency}}
                                td
                                    span(:class="{'order-spna' :order == 'ctr' }") {{ Math.round((item.clicks/item.imp)*10000)/100}}
                                td
                                    span(:class="{'order-spna' :order == 'cpc' }") {{ Math.round((item.cost/item.clicks)*100)/100 }}    
                                td
                                    span(:class="{'order-spna' :order == 'cpm' }") {{ Math.round(((item.cost / item.imp)*1000)*100)/100  |  $toCurrency }}
                                td
                                    span(:class="{'order-spna' :order == 'cv' }") {{item.cv | | $toCurrency}}
                                td
                                    span(:class="{'order-spna' :order == 'cvr' }") {{  Math.round((item.cv /item.clicks)*10000)/100 }}
                                td
                                    span(:class="{'order-spna' :order == 'cpo' }") {{ Math.round(item.cost/ item.cv)}}              
                                td
                                    span(:class="{'order-spna' :order == 'cost' }") {{ Math.round(item.cost*100)/100 | $toCurrency}}

</template>           

<script>
export default {
  props: ["fb","clients"],
  data(){
      return{
          fbTable:[],
          lowhight: 'low',
          order: "",
        
      }
  },
  watch:{
     fb(){
         this.orderBytable('imp');
        this.fbTable=[];
        this.CreatedTable();
       
     },
     lowhight(){
        this.orderBytable(this.order);
     }
  },
  created() {
    //表格製作
      this.CreatedTable();
      this.orderBytable('imp');
  },
  methods: {
    CreatedTable(){
         //表格製作
    const vm = this;
    for(let cli in vm.clients ){
       
       vm.fbTable.push({
          client: vm.clients[cli],
          imp: 0,
          clicks: 0,
          ctr: 0,
          cpc: 0,
          cpm: 0,
          cv: 0,
          cvr: 0,
          cpo: 0,
          cost: 0
       }); 
      vm.fb.forEach(function(item){
        if(item.clientname == vm.fbTable[cli].client){
        vm.fbTable[cli].imp += item.impressions;
        vm.fbTable[cli].clicks += item.clicks;
        vm.fbTable[cli].ctr += item.ctr;
        vm.fbTable[cli].cpc += item.cpc;
        vm.fbTable[cli].cpm += item.cpm;
        vm.fbTable[cli].cv += item.cv;
        vm.fbTable[cli].cvr += item.cvr;
        vm.fbTable[cli].cpo += item.cpo; 
        vm.fbTable[cli].cost += item.cost;
        }
      })  
              
    }; // cli  end
            

    } ,
    orderBytable(order_name) {
       const vm = this;  
        vm.order=order_name;
        let fb_new_table =[];
        for(let cli in vm.clients ){
       
       fb_new_table.push({
          client: vm.clients[cli],
          imp: 0,
          clicks: 0,
          ctr: 0,
          cpc: 0,
          cpm: 0,
          cv: 0,
          cvr: 0,
          cpo: 0,
          cost: 0
       }); 
      vm.fb.forEach(function(item){
        if(item.clientname == fb_new_table[cli].client){
          fb_new_table[cli].imp += item.impressions;
          fb_new_table[cli].clicks += item.clicks;
          fb_new_table[cli].ctr += item.ctr;
          fb_new_table[cli].cpc += item.cpc;
          fb_new_table[cli].cpm += item.cpm;
          fb_new_table[cli].cv += item.cv;
          fb_new_table[cli].cvr += item.cvr;
          fb_new_table[cli].cpo += item.cpo; 
          fb_new_table[cli].cost += item.cost;
        }
       
      })  
      
           
    }; // cli  end
       
      if(vm.lowhight == 'low'){
         switch(order_name){
           case 'client': 
           fb_new_table = fb_new_table.sort((a,b)=> a.client > b.client ? 1:-1);
           break;
           case 'imp': 
           fb_new_table = fb_new_table.sort((a,b)=> a.imp > b.imp ? 1:-1);
           break;
           case 'clicks': 
           fb_new_table = fb_new_table.sort((a,b)=> a.clicks > b.clicks ? 1:-1);
           break;
           case 'ctr': 
           fb_new_table = fb_new_table.sort((a,b)=> a.ctr > b.ctr ? 1:-1);
           break;
           case 'cpc': 
           fb_new_table = fb_new_table.sort((a,b)=> a.cpc > b.cpc ? 1:-1);
           break;
           case 'cpm': 
           fb_new_table = fb_new_table.sort((a,b)=> a.cpm > b.cpm ? 1:-1);
           break;
           case 'cv': 
           fb_new_table = fb_new_table.sort((a,b)=> a.cv > b.cv ? 1:-1);
           break;
           case 'cvr': 
           fb_new_table = fb_new_table.sort((a,b)=> a.cvr > b.cvr ? 1:-1);
           break;
           case 'cpo': 
           fb_new_table = fb_new_table.sort((a,b)=> a.cpo > b.cpo ? 1:-1);
           break;
           case 'cost': 
           fb_new_table = fb_new_table.sort((a,b)=> a.cost > b.cost ? 1:-1);
           break;
           
         } // switch end 
         
      }
      if(vm.lowhight == 'high'){
          switch(order_name){
           case 'client': 
           fb_new_table = fb_new_table.sort((a,b)=> a.client < b.client ? 1:-1);
           break;
           case 'imp': 
           fb_new_table = fb_new_table.sort((a,b)=> a.imp < b.imp ? 1:-1);
           break;
           case 'clicks': 
           fb_new_table = fb_new_table.sort((a,b)=> a.clicks < b.clicks ? 1:-1);
           break;
           case 'ctr': 
           fb_new_table = fb_new_table.sort((a,b)=> a.ctr < b.ctr ? 1:-1);
           break;
           case 'cpc': 
           fb_new_table = fb_new_table.sort((a,b)=> a.cpc < b.cpc ? 1:-1);
           break;
           case 'cpm': 
           fb_new_table = fb_new_table.sort((a,b)=> a.cpm < b.cpm ? 1:-1);
           break;
           case 'cv': 
           fb_new_table = fb_new_table.sort((a,b)=> a.cv < b.cv ? 1:-1);
           break;
           case 'cvr': 
           fb_new_table = fb_new_table.sort((a,b)=> a.cvr < b.cvr ? 1:-1);
           break;
           case 'cpo': 
           fb_new_table = fb_new_table.sort((a,b)=> a.cpo < b.cpo ? 1:-1);
           break;
           case 'cost': 
           fb_new_table = fb_new_table.sort((a,b)=> a.cost < b.cost ? 1:-1);
           break;
         } // switch end 
      } ;
        vm.fbTable = fb_new_table;
      
       
    } //orderBytable end 
  } // methods end
};
</script>


