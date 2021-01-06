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
                                th.pt-0(@click="orderBytable('all_profits')")
                                    span(:class="{'order-active' :order == 'all_profits' }") 売上金額 
                                th.pt-0(@click="orderBytable('all_unitprices')")
                                    span(:class="{'order-active' :order == 'all_unitprices' }") 客単価 
                                th.pt-0(@click="orderBytable('all_cvs')")
                                    span(:class="{'order-active' :order == 'all_cvs' }") 購入者数 
                                th.pt-0(@click="orderBytable('all_ordertypes_1')")
                                    span(:class="{'order-active' :order == 'all_ordertypes_1' }") 新規率
                                th.pt-0(@click="orderBytable('all_ordertypes_2')")
                                    span(:class="{'order-active' :order == 'all_ordertypes_2' }") 既存率
                                th.pt-0(@click="orderBytable('all_regulars_1')")
                                    span(:class="{'order-active' :order == 'all_regulars_1' }") 定期率
                                th.pt-0(@click="orderBytable('all_regulars_2')")
                                    span(:class="{'order-active' :order == 'all_regulars_2' }") 都度率
                        tbody
                            tr(v-for='(item,key) in crosTable')
                                td {{key+1}} 
                                td
                                    span(:class="{'order-spna' :order == 'client' }")  {{item.client}}
                                td
                                    span(:class="{'order-spna' :order == 'all_profits' }")  {{item.all_profits | $toCurrency}} 
                                td
                                    span(:class="{'order-spna' :order == 'all_unitprices' }")  {{ item.all_unitprices | $toCurrency }}
                                td
                                    span(:class="{'order-spna' :order == 'all_cvs' }")   {{item.all_cvs | $toCurrency}}
                                td
                                    span(:class="{'order-spna' :order == 'all_ordertypes_1' }")  {{ Math.round(item.all_ordertypes_1*100)/100}}%
                                td
                                    span(:class="{'order-spna' :order == 'all_ordertypes_2' }")  {{ Math.round(item.all_ordertypes_2*100) /100}}%
                                td
                                    span(:class="{'order-spna' :order == 'all_regulars_1' }")  {{ Math.round(item.all_regulars_1 *100)/100 }}%
                                td
                                    span(:class="{'order-spna' :order == 'all_regulars_2' }")  {{ Math.round(item.all_regulars_2 *100)/100 }}%      
</template>

<script>
export default {
  props: ["cros","clients"],
  data(){
      return{
          crosTable:[],
          lowhight: 'low',
          name: 'all_profits',
          order: ""
      }
  },
  watch:{
     cros(){
        this.crosTable=[];
        this.reCreated();
     },
     lowhight(){
        this.orderBytable(this.order);
     }
  },
  created() {
     this.reCreated();
     this.orderBytable('all_profits');
  },
  methods: {
    reCreated(){
        const vm = this;
          for (let i = 0; i < vm.clients.length; i++) {
            vm.crosTable.push({
              client: vm.clients[i],
              all_profits: 0,
              all_unitprices: 0,
              all_cvs: 0,
              all_ordertypes_1: 0,
              all_ordertypes_2: 0,
              all_regulars_1: 0,
              all_regulars_2: 0,
              all_visitors: 0
            });
            vm.cros.forEach(function(item) {
              if (item.clientname == vm.crosTable[i].client) {
                vm.crosTable[i].all_cvs += item.cv;
                vm.crosTable[i].all_profits += item.profit;
                vm.crosTable[i].all_unitprices += item.unitprice;
                vm.crosTable[i].all_ordertypes_1 += item.ordertype[0];
                vm.crosTable[i].all_ordertypes_2 += item.ordertype[1];
                vm.crosTable[i].all_regulars_1 += item.regular[0];
                vm.crosTable[i].all_regulars_2 += item.regular[1];
                vm.crosTable[i].all_visitors += item.visitors;
              }
            });

            vm.crosTable[i].all_ordertypes_1 =
              vm.crosTable[i].all_ordertypes_1 / vm.crosTable[i].all_cvs;
            vm.crosTable[i].all_ordertypes_2 =
              vm.crosTable[i].all_ordertypes_2 / vm.crosTable[i].all_cvs;
            vm.crosTable[i].all_regulars_1 =
              vm.crosTable[i].all_regulars_1 / vm.crosTable[i].all_cvs;
            vm.crosTable[i].all_regulars_2 =
              vm.crosTable[i].all_regulars_2 / vm.crosTable[i].all_cvs;

          
          }
         
    } ,
    orderBytable(order_name) {
       const vm = this;  
        vm.order=order_name;
        let cros_new_table =[];
      
      for (let i = 0; i < vm.clients.length; i++) {
        cros_new_table.push({
          client: vm.clients[i],
          all_profits: 0,
          all_unitprices: 0,
          all_cvs: 0,
          all_ordertypes_1: 0,
          all_ordertypes_2: 0,
          all_regulars_1: 0,
          all_regulars_2: 0,
          all_visitors: 0
        }); //前置
        console.log('我在這3'+cros_new_table);
        vm.cros.forEach(function(item) {
          if (item.clientname == cros_new_table[i].client) {
            cros_new_table[i].all_cvs += item.cv;
            cros_new_table[i].all_profits += item.profit;
            cros_new_table[i].all_unitprices += item.unitprice;
            cros_new_table[i].all_ordertypes_1 += item.ordertype[0];
            cros_new_table[i].all_ordertypes_2 += item.ordertype[1];
            cros_new_table[i].all_regulars_1 += item.regular[0];
            cros_new_table[i].all_regulars_2 += item.regular[1];
            cros_new_table[i].all_visitors += item.visitors;
          }
        });
      } // one for end 
      
      if(vm.lowhight == 'low'){
          // 由低開始 
      switch(order_name){
        case 'client' :
        cros_new_table = cros_new_table.sort((a,b) => a.client  > b.client ? 1:-1);
        break;
        case 'all_profits' :
        cros_new_table = cros_new_table.sort((a,b) => a.all_profits  > b.all_profits ? 1:-1);
        break;
        case 'all_unitprices' :
        cros_new_table = cros_new_table.sort((a,b) => a.all_unitprices  > b.all_unitprices ? 1:-1);
        break;
        case 'all_cvs' :
        cros_new_table = cros_new_table.sort((a,b) => a.all_cvs  > b.all_cvs ? 1:-1);
        break;
       }
      }else if(vm.lowhight == 'high'){
        switch(order_name){
          case 'client' :
          cros_new_table = cros_new_table.sort((a,b) => a.client  < b.client ? 1:-1);
          break;
          case 'all_profits' :
          cros_new_table = cros_new_table.sort((a,b) => a.all_profits  < b.all_profits ? 1:-1);
          break;
          case 'all_unitprices' :
          cros_new_table = cros_new_table.sort((a,b) => a.all_unitprices  < b.all_unitprices ? 1:-1);
          break;
          case 'all_cvs' :
          cros_new_table = cros_new_table.sort((a,b) => a.all_cvs  < b.all_cvs ? 1:-1);
          break;
         }
      } // one if end    
      
        for(let i = 0; i < vm.clients.length; i++){
        cros_new_table[i].all_ordertypes_1 = cros_new_table[i].all_ordertypes_1 / cros_new_table[i].all_cvs;
        cros_new_table[i].all_ordertypes_2 = cros_new_table[i].all_ordertypes_2 / cros_new_table[i].all_cvs;
        cros_new_table[i].all_regulars_1 = cros_new_table[i].all_regulars_1 /  cros_new_table[i].all_cvs;
        cros_new_table[i].all_regulars_2 = cros_new_table[i].all_regulars_2 /  cros_new_table[i].all_cvs;
      }
      if(vm.lowhight == 'low'){
        switch(order_name){
          case 'all_ordertypes_1' :
          cros_new_table = cros_new_table.sort((a,b) => a.all_ordertypes_1  > b.all_ordertypes_1 ? 1:-1);
          break;
          case 'all_ordertypes_2' :
          cros_new_table = cros_new_table.sort((a,b) => a.all_ordertypes_2  > b.all_ordertypes_2 ? 1:-1);
          break;
          case 'all_regulars_1' :
          cros_new_table = cros_new_table.sort((a,b) => a.all_regulars_1 > b.all_regulars_1 ? 1:-1);
          break;
          case 'all_regulars_2' :
          cros_new_table = cros_new_table.sort((a,b) => a.all_regulars_2 > b.all_regulars_2 ? 1:-1);
          break;
        };
      }else if(vm.lowhight == 'high'){
        switch(order_name){
          case 'all_ordertypes_1' :
          cros_new_table = cros_new_table.sort((a,b) => a.all_ordertypes_1  < b.all_ordertypes_1 ? 1:-1);
          break;
          case 'all_ordertypes_2' :
          cros_new_table = cros_new_table.sort((a,b) => a.all_ordertypes_2  < b.all_ordertypes_2 ? 1:-1);
          break;
          case 'all_regulars_1' :
          cros_new_table = cros_new_table.sort((a,b) => a.all_regulars_1 < b.all_regulars_1 ? 1:-1);
          break;
          case 'all_regulars_2' :
          cros_new_table = cros_new_table.sort((a,b) => a.all_regulars_2 < b.all_regulars_2 ? 1:-1);
          break;
        };
      }
      
      for(let i = 0; i < vm.clients.length; i++){
        cros_new_table[i].all_ordertypes_1 =  toCurrency_round_2(cros_new_table[i].all_ordertypes_1);
        cros_new_table[i].all_ordertypes_2 = toCurrency_round_2(cros_new_table[i].all_ordertypes_2);

        cros_new_table[i].all_regulars_1 = toCurrency_round_2( cros_new_table[i].all_regulars_1);
        cros_new_table[i].all_regulars_2 = toCurrency_round_2( cros_new_table[i].all_regulars_2);

        cros_new_table[i].all_profits = toCurrency_round(cros_new_table[i].all_profits);
        cros_new_table[i].all_unitprices = toCurrency_round(cros_new_table[i].all_unitprices);
        cros_new_table[i].all_cvs = toCurrency_round(cros_new_table[i].all_cvs); 
      }
        
     
      
      function toCurrency_round(num){
        let new_num = Math.round(num);
        var parts = new_num.toString().split('.');
        parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',');
        return parts.join('.');
      }
      function toCurrency_round_2(num){
        let new_num = Math.round(num*10000)/100;
        var parts = new_num.toString().split('.');
        parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',');
        return parts.join('.');
      }
     vm.crosTable = cros_new_table;
    } //orderBytable end 
  } // methods end
};
</script>

<style lang="scss" scoped>
.order-active {
  background: #727cf5;
  color: #fff;
  padding: 10px;
  line-height: 1cm;
  border-radius: 2px;
  position: relative;
  transition: 0.3s;
}
.order-active::before {
  content: "";
  position: absolute;
  left: 40%;
  transform: translateX(-40%);
  bottom: -7px;
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 10px 10px 0 10px;
  border-color: #727cf5 transparent transparent transparent;
}
.order-spna {
  background-image: linear-gradient(135deg, #fdfcfb 0%, #e2d1c3 100%);
  padding: 2px 5px;
  color: #000;
}
.order-filter {
  color: #fff;
  opacity: 0.3;
  padding: 3px;
  margin-left: 1em;
  border-radius: 3px;
}
.order-filter-active {
  background: #eee;
  color: #000;
  opacity: 1;
}
</style>
