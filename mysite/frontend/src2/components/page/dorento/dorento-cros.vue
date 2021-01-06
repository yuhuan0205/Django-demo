<template lang="pug">
div.all         
    .row 
      .col-xl-6.grid-margin.stretch-card
        .col-sm-12.ml-3
            .card.card2
                .card-body
                    h6.card-title 購入者數
                    i.fas.fa-eye(@click="$chart_scale('card2')")
                    .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading") 
                    canvas#chartjsLine2 
      .col-xl-6.grid-margin.stretch-card
        .col-sm-12
            .card.card3
                .card-body
                    h6.card-title 売上金額
                    i.fas.fa-eye(@click="$chart_scale('card3')")
                    .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
                    canvas#chartjsLine3                
    .row
      .col-xl-6.grid-margin.stretch-card
          .col-sm-12.ml-3
              .card.card5
                  .card-body
                      h6.card-title 客単価
                      i.fas.fa-eye(@click="$chart_scale('card5')")
                      .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
                      canvas#chartjsLine5
      .col-xl-6.grid-margin.stretch-card
          .col-sm-12
              .card.card6
                  .card-body
                      h6.card-title 新規 / 既存
                      i.fas.fa-eye(@click="$chart_scale('card6')")
                      .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
                      canvas#chartjsLine6
    .row
      .col-xl-6.grid-margin.stretch-card
          .col-sm-12.ml-3
              .card.card7
                  .card-body
                      h6.card-title 定期 / 都度
                      i(@click="$chart_scale('card7')").fas.fa-eye
                     
                      .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
                      canvas#chartjsLine7 
    keep-alive                  
      CROSTABLE(:cros="cros_df"  v-if="sendNow" :clients="clients")
</template>

<script>
import CROSTABLE from '@/components/table/dorento/dorento-cros-table';
export default {
  components: {
    CROSTABLE 
  },
  data() {
    return {
      clients: [], // 表格
      sendNow: false, //表格
      cros_df: [], // 表格
      a_barChartVis: barChartVis,
      a_barChartCV: barChartCV,
      a_barChartProfit: barChartProfit,
      a_barChartCVR: barChartCVR,
      a_barChartPrice: barChartPrice,
      a_barChartOrderType: barChartOrderType,
      a_barChartRegular: barChartRegular
    }; //reurn end
  },
  computed:{
     isLoading(){
        return  this.$store.state.dorento.isLoading_cros;
     },
     new_data(){
        return  this.$store.state.dorento.cros; //  綁定傳送
     },
     dateType(){
        return  this.$store.state.dorento.dateType
     },
  },
  watch:{
     dateType(){
       const vm = this;
       vm.upDate();
     },
     new_data(){
       console.log(this.$store.state.dorento.cros);
        this.upDate(); 
     },
  
   
  },
  methods: {
  
    upDate(){
      
      const vm = this;
      let cros_df = this.$store.state.dorento.cros;
    
            vm.clients = cros_df[0].clients;
            vm.cros_df = cros_df[1];

            if(!this.$store.state.dorento.dateType){
              cros_df = cros_df[1];
            }
            if(this.$store.state.dorento.dateType == 'm'){
               cros_df = cros_df[2];  
            }
            if(this.$store.state.dorento.dateType == 'q'){
               cros_df = cros_df[3];  
            }
            vm.sendNow=true;
            let timeBox =[];
            let color_all = ["#f38181", "#fce38a", "#eaffd0", "#a8e6cf", "#fdffab", "#ffd3b6", "#ffaaa5", "#d4a5a5", "#ffecda", "#f9ffea", "#a6d0e4", "#ff6f3c", "#ff9a3c", "#ffc93c", "#17b978", "#a7ff83"];
            let cros_charts=[[],[],[]];
            let OrderType = [ //新規率 既存率 -
              {
                data: [],
                label: "新規",
                backgroundColor: "#f38181",
              },
              {
                data: [],
                label: "既存",
                backgroundColor: "#fce38a",
              }
             ]; //定期率+都度率
            let Regular = [
              {
                data: [],
                label: "定期",
                backgroundColor: "#f38181",
              },
              {
                data: [],
                label: "都度",
                backgroundColor: "#fce38a",
              }
            ]; //新規率+既存率
            for(let cli in vm.clients){
              
                for(let charts in cros_charts ){

                  cros_charts[charts].push({
                    data: [],
                    label:  vm.clients[cli],
                    borderColor: color_all[cli] || "#7ee5e5",
                    backgroundColor: "#fff",
                    fill: false
                  }) // 
                } // cros charts end 
             OrderType[0].data.push(
              {
                x:  vm.clients[cli],
                y: 0
              },
              );
              OrderType[1].data.push(
                {
                  x:  vm.clients[cli],
                  y:  0
                },
              );
              Regular[0].data.push(
                {
                  x:  vm.clients[cli],
                  y: 0
                },
              );
              Regular[1].data.push(
                {
                  x:  vm.clients[cli],
                  y:  0
                },
              );   
            let [cvBox,profitBox,priceBox] =  cros_charts ;

                cros_df.forEach(item=>{
                  if (item.clientname.includes(vm.clients[cli]) == 1) 
                        timeBox.push(item.date);  
                  if(item.clientname == cvBox[cli].label)
                        cvBox[cli].data.push({
                          x: item.date,
                          y: item.cv 
                      });
                  if(item.clientname == profitBox[cli].label)
                        profitBox[cli].data.push({
                          x: item.date,
                          y: item.profit 
                      }); 
                  if(item.clientname == priceBox[cli].label)
                        priceBox[cli].data.push({
                          x: item.date,
                          y: item.unitprice 
                      });   
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


                })  // cros_df end 
                timeBox = timeBox.filter((item, key, arr) => arr.indexOf(item) == key);
                timeBox.sort( (a, b)=>  a > b ? 1 : -1); // 

                vm.a_barChartCV.datasets = cvBox ;
                vm.a_barChartProfit.datasets = profitBox;
                vm.a_barChartPrice.datasets =  priceBox;
                vm.a_barChartOrderType.datasets = OrderType;
                vm.a_barChartRegular.datasets = Regular;
                vm.a_barChartCV.labels = timeBox ;
                vm.a_barChartProfit.labels = timeBox;
                vm.a_barChartPrice.labels = timeBox;
                vm.a_barChartOrderType.labels = vm.clients;
                vm.a_barChartRegular.labels = vm.clients;
                
              
            }//  cli end 
           
                window.myBar2.update();
                window.myBar3.update();
                window.myBar5.update();
                window.myBar6.update();
                window.myBar7.update(); 
    }, // upDate
    
   

  },
 
  activated: function() {
    // 圖表
    $(function() {
      if ($("#chartjsLine").length) {
        (Chart.defaults.global.defaultFontFamily = "Noto Sans JP"),
          (window.myBar1 = new Chart($("#chartjsLine"), {
            type: "line",
            data: barChartVis
          }));
      }

      if ($("#chartjsLine2").length) {
        window.myBar2 = new Chart($("#chartjsLine2"), {
          type: "line",
          data: barChartCV,
          options: {
            scales: {
              xAxes: {
                type: "time",
                distribution: "linear"
              }
            }
          }
        });
      }

      if ($("#chartjsLine3").length) {
        window.myBar3 = new Chart($("#chartjsLine3"), {
          type: "line",
          data: barChartProfit
        });
      }

      if ($("#chartjsLine4").length) {
        window.myBar4 = new Chart($("#chartjsLine4"), {
          type: "line",
          data: barChartCVR
        });
      }

      if ($("#chartjsLine5").length) {
        window.myBar5 = new Chart($("#chartjsLine5"), {
          type: "line",
          data: barChartPrice
        });
      }
      if ($("#chartjsLine6").length) {
        window.myBar6 = new Chart($("#chartjsLine6"), {
          type: "bar",
          data: barChartOrderType,
          options: {
            title: {
              display: false
            },
            tooltips: {
              mode: "index",
              intersect: false
            },
            responsive: true,
            scales: {
              xAxes: [
                {
                  stacked: true
                }
              ],
              yAxes: [
                {
                  stacked: true
                }
              ]
            }
          }
        });
      }
      if ($("#chartjsLine7").length) {
        window.myBar7 = new Chart($("#chartjsLine7"), {
          type: "bar",
          data: barChartRegular,
          options: {
            title: {
              display: false
            },
            tooltips: {
              mode: "index",
              intersect: false
            },
            responsive: true,
            scales: {
              xAxes: [
                {
                  stacked: true
                }
              ],
              yAxes: [
                {
                  stacked: true
                }
              ]
            }
          }
        });
      }

    }); //function end
      
      let mode = "";
          if(this.$route.name =='dorento-cros'){
              mode = "cros"; 
           }
           if(this.$route.name =='dorento-fb'){
              mode = "fb";  
           } 
            if(this.$route.name =='dorento-line'){
              mode = "line";  
           }   
        this.$store.dispatch('dorento/getMode',mode);   
        this.$store.dispatch('dorento/getData');
  },
  
};

var barChartVis = {
  labels: [],
  datasets: []
};

var barChartCV = {
  labels: [],
  datasets: []
};

var barChartProfit = {
  labels: [],
  datasets: []
};

var barChartCVR = {
  labels: [],
  datasets: []
};

var barChartPrice = {
  labels: [],
  datasets: []
};
var barChartOrderType = {
  labels: [],
  datasets: []
};
var barChartRegular = {
  labels: [],
  datasets: []
};
var barChartOrderType = {
  labels: [],
  datasets: []
};
var barChartRegular = {
  labels: [],
  datasets: []
};
</script>

<style lang="scss" scoped>
  
</style>