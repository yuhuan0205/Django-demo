<template lang="pug">
   div.home.col-12
      .row.ml-3
         .col-11.col-xl-11.stretch-card
            .row.flex-grow
               div(class="col-md-4 grid-margin stretch-card")
                     .card
                        .card-body.top-card
                           div(class="d-flex justify-content-between align-items-baseline")
                              h6.card-title.mb-0  {{clients[0]}}
                           .row   
                              div.col-10
                                 h1.mb-2    {{topcv[0]}}
                                 .d-flex.align-items-baseline  
                                    p.text-success
                                       span 売上金額 TOP1
                                       i.icon-sm.mb-1(data-feather="arrow-up")
                              div.col-2.position-relative 
                                 img(src="/static/images/medal.png").position-absolute      
               div(class="col-md-3 grid-margin stretch-card")
                     .card
                        .card-body
                           div(class="d-flex justify-content-between align-items-baseline")
                              h6.card-title.mb-0  {{clients[1]}}
                           .row
                              div(class="col-12 col-md-12 col-xl-12")
                                 h1.mb-2   {{topcv[1]}}
                                 .d-flex.align-items-baseline
                                    p.text-success
                                       span 売上金額 TOP2
                                       i.icon-sm.mb-1(data-feather="arrow-up")
               div(class="col-md-3 grid-margin stretch-card")
                     .card
                        .card-body
                           div(class="d-flex justify-content-between align-items-baseline")
                              h6.card-title.mb-0    {{clients[2]}}
                           .row
                              div(class="col-12 col-md-12 col-xl-12")
                                 h1.mb-2    {{topcv[2]}}
                                 .d-flex.align-items-baseline
                                    p.text-success
                                       span 売上金額 TOP3
                                       i.icon-sm.mb-1(data-feather="arrow-up")                                       
      .row.ml-1
         .col-xl-6.grid-margin.stretch-card
            .col-12
               .card.cardPROFIT
                     .card-body
                           h6.card-title 売上金額
                           i.fas.fa-eye(@click="$chart_scale('cardPROFIT')")
                           .spinner-border.spinner-border-sm.chart_loading(v-if="loading")
                           canvas#chartjsLinePROFIT
         .col-xl-6.grid-margin.stretch-card
            .col-12
               .card.cardUNITPRICE
                     .card-body
                           h6.card-title 客単価
                           i.fas.fa-eye(@click="$chart_scale('cardUNITPRICE')")
                           .spinner-border.spinner-border-sm.chart_loading(v-if="loading")
                           canvas#chartjsLineUNITPRICE                                            
      .row.ml-1.mb-3
         .col-xl-6.grid-margin.stretch-card
            .col-12
               .card.cardCV
                     .card-body
                           h6.card-title 購入者數
                           i.fas.fa-eye(@click="$chart_scale('cardCV')")
                           .spinner-border.spinner-border-sm.chart_loading(v-if="loading")
                           canvas#chartjsLineCV
         .col-xl-6.grid-margin.stretch-card
            .col-12
               .card.cardOrderType
                     .card-body
                           h6.card-title 新規 / 既存
                           i.fas.fa-eye(@click="$chart_scale('cardOrderType')")
                           .spinner-border.spinner-border-sm.chart_loading(v-if="loading")
                           canvas#chartjsLineOrderType 
      .row.ml-1.mb-3
         .col-xl-6.grid-margin.stretch-card
            .col-12
               .card.cardRegular
                     .card-body
                           h6.card-title 定期 / 都度
                           i.fas.fa-eye(@click="$chart_scale('cardRegular')")
                           .spinner-border.spinner-border-sm.chart_loading(v-if="loading")
                           canvas#chartjsLineRegular                                      
      keep-alive                  
         HOMETABLE(:cros="cros_df"  v-if="sendNow" :clients="clients")
</template>

<script>
import HOMETABLE from '@/components/table/home-table';
export default {
   components:{
      HOMETABLE
   },
   data(){
      return{
          data:[],
          loading: 0,
          cros_df: "", // 表格
          sendNow: false, // 表格
          a_profit: profit ,
          a_unitprice: unitprice,
          a_cv: cv ,
          a_OrderType: OrderType,
          a_Regular: Regular,
          a_TOP1: TOP1 ,
          topCli: [],
          clients:[],
          topcv:[],
          
      }
   },
   
  methods:{
    
      getHOME(){  
          const vm = this; 
          vm.loading = 1;
          const api =`http://192.168.111.166:8070/client/top3_view`; 
          this.$http.get(api).then((res) => {
             
                if(res){
                   vm.data = res.data;
                   vm.loading = 0;
                   vm.creatChart();
                }
         　})
      },
      creatChart(){
          let timeBox =[];
          let topCli = [];
          const vm = this;
          let color_all = ["#f38181", "#fce38a", "#eaffd0"];
          let clients = vm.data[0].clients; //  
          vm.clients =  clients ;   
          vm.cros_df = vm.data[1];
          vm.sendNow=true;
          let home_charts=[[],[],[],[]];
          let OrderType =[
            //新規率 既存率 -
            {
               data: [],
               label: "新規",
               backgroundColor: "#f38181"
            },
            {
               data: [],
               label: "既存",
               backgroundColor: "#fce38a"
            }
            ]; //定期率+都度率
           let Regular = [
            {
               data: [],
               label: "定期",
               backgroundColor: "#f38181"
            },
            {
               data: [],
               label: "都度",
               backgroundColor: "#fce38a"
            }
            ];

           
          for(let cli in clients){
                 topCli.push({
                   name: clients[cli],
                   data: 0  
               });
               for(let charts in home_charts ){

                  home_charts[charts].push({
                    data: [],
                    label:  clients[cli],
                    borderColor: color_all[cli] || "#7ee5e5",
                    backgroundColor: "#fff",
                    fill: false
                  }) // 
                } // cros charts end 
            let [cvBox,profitBox,priceBox,top1Box] =  home_charts ;
               OrderType[0].data.push(
              {
                x:  clients[cli],
                y: 0
              },
              );
              OrderType[1].data.push(
                {
                  x:  clients[cli],
                  y:  0
                },
              );
              Regular[0].data.push(
                {
                  x:  clients[cli],
                  y: 0
                },
              );
              Regular[1].data.push(
                {
                  x:  clients[cli],
                  y:  0
                },
              );  
             

             vm.data[1].forEach(item=>{
                  if(item.clientname == topCli[cli].name){
                     topCli[cli].data +=  item.cv 
                  }   
                  if (item.clientname.includes(clients[cli]) == 1) 
                        timeBox.push(item.date);  
                  if(item.clientname == cvBox[cli].label)
                        cvBox[cli].data.push({
                          x: item.date,
                          y: item.cv 
                      });
                  if(item.clientname == profitBox[cli].label)
                        profitBox[cli].data.push({
                          x: item.date,
                          y: Math.round(item.profit * 100) /100 
                      }); 
                  if(item.clientname == priceBox[cli].label){
                     priceBox[cli].data.push({
                          x: item.date,
                          y: Math.round(item.unitprice * 100)/100 
                      }); 
                      
                  }
                 
                        
                  if(item.clientname == OrderType[0].data[cli].x)
                    OrderType[0].data[cli].y  +=  item.ordertype[0];
                  
                  if(item.clientname ==  OrderType[1].data[cli].x)
                    OrderType[1].data[cli].y   +=  item.ordertype[1];
                  if(item.clientname ==  Regular[0].data[cli].x){
                    Regular[0].data[cli].y  +=  item.regular[0];
                  }
                  if(item.clientname ==  Regular[1].data[cli].x){
                    Regular[1].data[cli].y  +=  item.regular[1];
                  } 
                 
                           
                
             })
            
             timeBox = timeBox.filter((item, key, arr) => arr.indexOf(item) == key);
             timeBox.sort( (a, b)=>  a > b ? 1 : -1); 
             vm.a_profit.labels = timeBox;
             vm.a_unitprice.labels = timeBox;
             vm.a_cv.labels = timeBox;
             vm.a_OrderType.labels = clients;
             vm.a_Regular.labels = clients;
             
             vm.a_profit.datasets = profitBox;
             vm.a_unitprice.datasets =priceBox;
             vm.a_cv.datasets = cvBox;
             vm.a_Regular.datasets = Regular;
             vm.a_OrderType.datasets = OrderType;
            
              
             
          } // cli end 
             
             vm.topCli = topCli.sort((a,b) => a.data < b.data ? 1:-1);
             vm.topcv = topCli.map(item =>  item.data);
             vm.clients = topCli.map(item =>  item.name);
             window.myBarPROFIT2.update();
             window.myBarUNITPRICE2.update();
             window.myBarCV2.update();
             window.myBarOrderType2.update();
             window.myBarRegular2.update();
             window.myBarTOP1.update();
      }
  },
  created:function(){
     this.getHOME();
     $(function(){
         if ($("#chartjsLinePROFIT").length) {
         (Chart.defaults.global.defaultFontFamily = "Noto Sans JP"),
            (window.myBarPROFIT2 = new Chart($("#chartjsLinePROFIT"), {
               type: "line",
               data:  profit
            }));
         } // CH END
         if ($("#chartjsLineUNITPRICE").length) {
         (Chart.defaults.global.defaultFontFamily = "Noto Sans JP"),
            (window.myBarUNITPRICE2 = new Chart($("#chartjsLineUNITPRICE"), {
               type: "line", 
               data:  unitprice
            }));
         } // CH END 
         if ($("#chartjsLineCV").length) {
         (Chart.defaults.global.defaultFontFamily = "Noto Sans JP"),
            (window.myBarCV2 = new Chart($("#chartjsLineCV"), {
               type: "line", 
               data:  cv
            }));
         } // CH END
         if ($("#chartjsLineOrderType").length) {
         (Chart.defaults.global.defaultFontFamily = "Noto Sans JP"),
            (window.myBarOrderType2 = new Chart($("#chartjsLineOrderType"), {
               type: "bar", 
               data:  OrderType
            }));
         } // CH END
         if ($("#chartjsLineRegular").length) {
         (Chart.defaults.global.defaultFontFamily = "Noto Sans JP"),
            (window.myBarRegular2 = new Chart($("#chartjsLineRegular"), {
               type: "bar", 
               data:  Regular
            }));
         } // CH END

         //top
         if ($("#chartjsLineTOP1").length) {
         (Chart.defaults.global.defaultFontFamily = "Noto Sans JP"),
            (window.myBarTOP1 = new Chart($("#chartjsLineTOP1"), {
               type: "line", 
               data:  TOP1
            }));
         } // top01 END
         
      

     }) // function end 
    
  }
  
  
} // vue end 
  var TOP1= {
    datasets: []
  }
  var profit = {
   labels: [],
   datasets: []
  };
  var unitprice = {
   labels: [],
   datasets: []
  };
  var cv = {
   labels: [],
   datasets: []
  }; 
  var OrderType = {
   labels: [],
   datasets: []
  };  
  var Regular = {
   labels: [],
   datasets: []
  };  
</script>

<style lang="scss" scoped>
  html,body{
      display: flex;
       align-items: start;
       justify-content: start;
       height: 100%;
  }
   div.home{
      position: relative;
      top: 0;
      margin-top: -2em;
      .line{
         width: 50px;
         height: 50px;
      }
   }
   .top-card{
      background:linear-gradient(top,#ECE9E6,#FFFFFF);
      border-radius: 18px;
      img{
         width: 80px;
         height: 80px;
         right: 20%;
         transform: translateX(-20%);
      }
      h6.card-title{
         color: #000;
      }
      h1{
         color: #000;
        
      }
   }
</style>