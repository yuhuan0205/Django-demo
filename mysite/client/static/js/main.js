

Vue.component('dorento-cros-pagination', {
  template: '#dCrosPage',
  props: ["crosTable"],
  data(){
     return{
       order: '',
       order_select: "low",
     }
  },
  methods: {
    new_clients(){
      this.$emit('aorder','');
      this.order = 'client';
    },
    new_profits(){
      this.order = 'all_profits';
      this.$emit('aorder',this.order,this.order_select);
      
    },
    new_unitprices(){
      this.order ='all_unitprices';
      this.$emit('aorder','all_unitprices',this.order_select);
      
    },
    new_cvs(){
      this.order ='all_cvs';
      this.$emit('aorder','all_cvs',this.order_select);
      
    },
    new_ordertypes_1(){
      this.order ='all_ordertypes_1';
      this.$emit('aorder','all_ordertypes_1',this.order_select);
      
    },
    new_ordertypes_2(){
      this.order ='all_ordertypes_2';
      this.$emit('aorder','all_ordertypes_2',this.order_select);
      
    },
    new_regulars_1(){
      this.order ='all_regulars_1';
      this.$emit('aorder','all_regulars_1',this.order_select);
      
    },
    new_regulars_2(){
      this.order ='all_regulars_2';
      this.$emit('aorder','all_regulars_2',this.order_select);
      
    },
    new_low(){
      const vm = this;
      vm.order_select= 'low';
      this.$emit('aorder',vm.order,'low',this.order_select);
    },
    new_high(){
      const vm = this;
      vm.order_select= 'high';
      this.$emit('aorder',vm.order,'high',this.order_select);
    },
    chart_scale(card){
      console.log(card);
      const acard = document.querySelector(`.${card}`);
      screenfull.request(acard);
      if (screenfull) {
        screenfull.exit(acard);
      }
    }


  },

})
Vue.component('dorento-fb-pagination', {
  template: '#dFbPage',
  
})
Vue.component('dorento-line-pagination', {
  template: '#dLinePage',
})




var app = new Vue({

  el: "#app",
  data: {
    cros: [], //總資料包扣除第一筆後
    cros_table: [], //crosn總表格用
    cros_one: "",  //第一筆資料包
    filterbox: false, // 樣式判別
    dorento_show: "dorento-cros-pagination",  //頁面切換用
    scale_chrat: false,//圖表放小判斷
    fliter3_show: false, //第三階段搜尋
    fliter2_show: false, //第二階段搜尋類別
    fliter1_show: true, //第一階段搜尋類別
    getfliter2_text: "進階搜尋",
    getfliter3_text: "GA搜尋",
    allSelected_ind: false, // 全選判斷
    allSelected_cli: false,
    allSelected_pro: false,
    allSelected_campaign: false,
    allSelected_ordertype: false,
    allSelected_regular: false,
    allSelected_paymethod: false,
    allSelected_media: false, //媒體別
    allSelected_link_type: false,
    allSelected_ga1: false,
    allSelected_ga2: false,
    allSelected_ga3: false,
    //總客戶數   => 表格用
    clients:[],
    // 條件篩選------------------------------
    filter: [], //篩選框用資料包
    ind: [],
    cli: [],
    pro: [],
    paymethod:[
      {
        name: "0",
        value: "0",
      },
      {
        name: "クレジットカード",
        value: "1",
      },
      {
        name: "代引",
        value: "2",
      },
      {
        name: "コンビニ",
        value: "5",
      },
      {
        name: "アフティ",
        value: "8",
      },
      {
        name: "LINE PAY",
        value: "9",
      },
      {
        name: "その他",
        value: "剩下的",
      }
    ],  //支払い
    ordertype: ["新規","既存"], //新規既存
    regular: ["定期","都度"], // 定都
    campaign: [],  //キャンペーン名
    media: [], //媒體別
    link_type: [], //リンク別
    
    ga1:[],
    ga2:[],
    ga3:[],
     // 條件篩選預設值
     ind_df: [],
     cli_df: [],
     pro_df: [],
     campaign_df: [],
     ordertype_df:[],
     regular_df:[],
     paymethod_df:[],
     ga1_df:[],
     ga2_df:[],
     ga3_df:[],
    // 搜尋框用
    ind_filter: "",
    cli_filter: "",
    pro_filter: "",
    campaign_filter: "",
    ordertype_filter:"",
    regular_filter:"",
    paymethod_filter:"",
    media_filter:"",
    link_type_filter:"",
    ga1_filter:"",
    ga2_filter:"",
    ga3_filter:"",
     //條件輸出值
     indshow: [],
     clishow: [],
     clikeep: [],
     proshow: [],
     campaignshow:[],
     ordertypeshow:[],
     regularshow:[],
     paymethodshow:[],
     mediashow:[],
     link_typeshow:[],
     ga1show:[],
     ga2show:[],
     ga3show:[],

     ga1_get:[],
     ga2_gat:[],
     ga3_get:[],
    // 條件篩選 end -------------------------------
   
    


    // 報表顯示
    time: [],

   



    date1: "",
    date2: "",

    a_barChartVis: barChartVis,
    a_barChartCV: barChartCV,
    a_barChartProfit: barChartProfit,
    a_barChartCVRate: barChartCVRate,
    a_barChartPrice: barChartPrice,
    a_barChartOrderType: barChartOrderType,
    a_barChartRegular: barChartRegular
  },
  methods: {
    scaleChrat(chrat_all){
      const vm= this;
      let newall = chrat_all;
      vm.scale_chrat = newall;
      console.log(vm.scale_chrat) ;
    },
    getfliter2(){  //此為進階或上一步的按鈕
      const vm = this; 
      vm.getCros();
      if(vm.fliter3_show){ //   當我點選時發現GA狀態是ture的時候
        vm.fliter3_show = false;    // GA會被消失
        vm.fliter2_show = true;  //  進階會被打開
        $("html,body").scrollTop(0);
        return ;
      }
      vm.fliter2_show = !vm.fliter2_show;
      vm.fliter1_show = !vm.fliter1_show;
     
      if(vm.getfliter2_text == "進階搜尋"){
        vm.getfliter2_text = "上一步";
      }else{
        vm.getfliter2_text ="進階搜尋";
      }
      $("html,body").scrollTop(0);
    },
    getfliter3(){
      const vm = this;
      vm.getCros();
      vm.fliter3_show = !vm.fliter3_show;
      vm.fliter2_show = !vm.fliter2_show;
      $("html,body").scrollTop(0);
    },
    allSend() {
      const vm = this;
      vm.filterbox = false;
      vm.getCros();
    },
    top() {
      const vm = this;
      $("html,body").scrollTop(0);
      vm.filterbox = !vm.filterbox;
    },
    Filter_ind_NULL() {
      const vm = this;
      vm.indshow = [];
      vm.ind = vm.ind_df;
      vm.cli = vm.cli_df;
      vm.pro = vm.pro_df;

      vm.allSelected_ind = false;
    },
    Filter_cli_NULL() {
      const vm = this;
      vm.clishow = [];
      vm.ind = vm.ind_df;
      vm.cli = vm.cli_df;
      vm.pro = vm.pro_df;
      vm.allSelected_cli = false;
    },
    Filter_pro_NULL() {
      const vm = this;
      vm.proshow = [];
      vm.ind = vm.ind_df;
      vm.cli = vm.cli_df;
      vm.pro = vm.pro_df;
      vm.allSelected_pro = false;
    },
    Filter_campaign_NULL() {
      const vm = this;
      vm.campaignshow = [];
      vm.allSelected_campaign = false;
    },
    Filter_ordertype_NULL() {
      const vm = this;
      vm.ordertypeshow = [];
      vm.allSelected_ordertype = false;
    },
    Filter_regular_NULL() {
      const vm = this;
      vm.regularshow = [];
      vm.allSelected_regular = false;
    },
    Filter_paymethod_NULL() {
      const vm = this;
      vm.paymethodshow = [];
      vm.allSelected_paymethod = false;
    },
    Filter_ga1_NULL() {
      const vm = this;
      vm.ga1show = [];
      vm.allSelected_ga1 = false;
    },
    Filter_ga2_NULL() {
      const vm = this;
      vm.ga2show = [];
      vm.allSelected_ga2 = false;
    },
    Filter_ga3_NULL() {
      const vm = this;
      vm.ga3show = [];
      vm.allSelected_ga3 = false;
    },


    Filter_ind_All() {
      const vm = this;
      vm.indshow = [];

      if (vm.allSelected_ind) {
        for (inds in vm.ind_filter_case) {
          vm.indshow.push(vm.ind_filter_case[inds]);
        }
      }
      vm.cli = vm.cli_df;
      vm.pro = vm.pro_df;
    },
    Filter_cli_All() {
      const vm = this;
      vm.clishow = [];

      if (vm.allSelected_cli) {
        for (clis in vm.cli_filter_case) {
          vm.clishow.push(vm.cli_filter_case[clis]);
        }
      }
      vm.ind = vm.ind_df;
      vm.pro = vm.pro_df;
    },
    Filter_pro_All() {
      const vm = this;
      vm.proshow = [];

      if (vm.allSelected_pro) {
        for (pros in vm.pro_filter_case) {
          vm.proshow.push(vm.pro_filter_case[pros]);
        }
      }
    },
    Filter_paymethod_All(){
      const vm = this;
      vm.paymethodshow=[];
      if (vm.allSelected_paymethod) {
        for (paymethods in vm.paymethod_filter_case) {
          vm.paymethodshow.push(vm.paymethod_filter_case[paymethods].value);
        }
      }
    },
    Filter_campaign_All(){
      const vm = this;
      vm.campaignshow=[];
      if (vm.allSelected_campaign) {
        for (campaigns in vm.campaign_filter_case) {
          vm.campaignshow.push(vm.campaign_filter_case[campaigns]);
        }
      }
      
    },
    Filter_ordertype_All(){
      const vm = this;
      vm.ordertypeshow=[];
      if (vm.allSelected_ordertype) {
        for (ordertypes in vm.ordertype_filter_case) {
          vm.ordertypeshow.push(vm.ordertype_filter_case[ordertypes]);
        }
      }
     
    },
    Filter_regular_All(){
      const vm = this;
      vm.regularshow=[];
      if (vm.allSelected_regular) {
        for (regulars in vm.regular_filter_case) {
          vm.regularshow.push(vm.regular_filter_case[regulars]);
        }
      }
    
    },

    Filter_media_All(){
      const vm = this;
      vm.mediashow=[];  
      if (vm.allSelected_media) {
        for (medias in vm.media_filter_case) {
          vm.mediashow.push(vm.media_filter_case[medias]);
        }
      }
    
    },
    Filter_link_type_All(){
      const vm = this;
      vm.link_typeshow=[];  
      if (vm.allSelected_link_type) {
        for (link_types in vm.link_type_filter_case) {
          vm.link_typeshow.push(vm.link_type_filter_case[link_types]);
        }
      }
    
    },
   
    Filter_ga1_All(){
      const vm = this;
      vm.ga1show=[];
      if (vm.allSelected_ga1) {
        for (ga1s in vm.ga1_filter_case) {
          vm.ga1show.push(vm.ga1_filter_case[ga1s]);
        }
      }
    },
    Filter_ga2_All(){
      const vm = this;
      vm.ga2show=[];
      if (vm.allSelected_ga2) {
        for (ga2s in vm.ga2_filter_case) {
          vm.ga2show.push(vm.ga2_filter_case[ga2s]);
        }
      }
    },
    Filter_ga3_All(){
      const vm = this;
      vm.ga3show=[];
      if (vm.allSelected_ga3) {
        for (ga3s in vm.ga3_filter_case) {
          vm.ga3show.push(vm.ga3_filter_case[ga3s]);
        }
      }
    },



    Filter_Ind() { 
      const vm = this;
      let new_cli = [];
      let new_pro = [];
      for (let i = 0; i < vm.filter.length; i++) {
        if (vm.indshow == 0) {
          new_cli = vm.cli_df;
          new_pro = vm.pro_df;
        }
        else if (vm.indshow.includes(vm.filter[i].industrytype) == 1) {
          new_cli.push(vm.filter[i].clientname);
          new_pro.push(vm.filter[i].productname);
        }

      }
      let new_cli2 = new_cli.filter((item, key, arr) => arr.indexOf(item) == key);
      let new_pro2 = new_pro.filter((item, key, arr) => arr.indexOf(item) == key);
      vm.cli = new_cli2;
      vm.pro = new_pro2;
      this.allSelected_ind = false;
    },
    Filter_Cli() {
      const vm = this;
      let new_pro = [];
      let new_ind = [];
      for (let i = 0; i < vm.filter.length; i++) {
        if (vm.clishow == 0) {
          new_pro = vm.pro_df;
          new_ind = vm.ind_df;
        }
        else if (vm.clishow.includes(vm.filter[i].clientname) == 1) {
          new_pro.push(vm.filter[i].productname);
          new_ind.push(vm.filter[i].industrytype);
        }

      }
      let new_ind2 = new_ind.filter((item, key, arr) => arr.indexOf(item) == key);
      let new_pro2 = new_pro.filter((item, key, arr) => arr.indexOf(item) == key);
      vm.pro = new_pro2;
      vm.ind = new_ind2;
      this.allSelected_cli = false;



    },
    Filter_Pro() {
      const vm = this;
      var new_cli = [];
      let new_ind = [];
      for (let i = 0; i < vm.filter.length; i++) {
        if (vm.proshow == 0) {
          new_cli = vm.cli_df;
          new_ind = vm.ind_df;
        }
        else if (vm.proshow.includes(vm.filter[i].productname) == 1) {
          new_cli.push(vm.filter[i].clientname);
          new_ind.push(vm.filter[i].industrytype);
        }

      }
      let new_cli2 = new_cli.filter((item, key, arr) => arr.indexOf(item) == key);
      let new_ind2 = new_ind.filter((item, key, arr) => arr.indexOf(item) == key);
      vm.cli = new_cli2;
      vm.ind = new_ind2;

      console.log(vm.proshow);
      this.allSelected_pro = false;

    },
    getFilter() {
      const vm = this;
      $.ajax({
        type: 'GET',
        url: `data.json`,
        dataType: 'json',
        success: function (response) {
          vm.filter = response;
          const newind = vm.filter.map(item => item.industrytype);
          const newcli = vm.filter.map(item => item.clientname);
          const newpro = vm.filter.map(item => item.productname);
          vm.ind = newind.filter((item, key, arr) => arr.indexOf(item) == key);
          vm.cli = newcli.filter((item, key, arr) => arr.indexOf(item) == key);
          vm.pro = newpro.filter((item, key, arr) => arr.indexOf(item) == key);
          vm.ind_df = newind.filter((item, key, arr) => arr.indexOf(item) == key);
          vm.cli_df = newcli.filter((item, key, arr) => arr.indexOf(item) == key);
          vm.pro_df = newpro.filter((item, key, arr) => arr.indexOf(item) == key);

        },
        error: function (xhr) {
          alert("發生錯誤");
        },
      });  // ajax end  

    },
    
    getCros() {
      const vm = this;
      vm.ga1_get = vm.ga1show;
      vm.ga2_get = vm.ga2show;
      vm.ga3_get = vm.ga3show;
      if(vm.allSelected_ga1){
        vm.ga1_get ="";
      }
      if(vm.allSelected_ga2){
        vm.ga2_get ="";
      }
      if(vm.allSelected_ga3){
        vm.ga3_get ="";
      }
      console.log(vm.paymethodshow);
      $.ajax({
        type: 'GET',
        url: `data2.json?date1=${vm.date1}&date2=${vm.date2}&clientname=${vm.clishow}&productname=${vm.proshow}&campaign=${vm.campaignshow}&ordertype=${vm.ordertypeshow}&regular=${vm.regularshow}&paymethod=${vm.paymethodshow}&media=${vm.mediashow}&link_type=${vm.link_typeshow}&ga1=${vm.ga1_get}&ga2=${vm.ga2_get}&ga3=${vm.ga3_get}`,
        //url: `http://192.168.111.43:8070/client/cros?date1=${vm.date1}&date2=${vm.date2}&clientname=${vm.clishow}&productname=${vm.proshow}&campaign=${vm.campaignshow}&ordertype=${vm.ordertypeshow}&regular=${vm.regularshow}&paymethod=${vm.paymethodshow}&media=${vm.mediashow}&link_type=${vm.link_typeshow}&ga1=${vm.ga1_get}&ga2=${vm.ga2_get}&ga3=${vm.ga3_get}`, //本地端網址或者有開放的cros api
        dataType: 'json',
        success: function (response) {
          //-- 總資料包處理
         
          let allcros = response;
          let fitst = allcros.shift(); //取出陣列第一筆 並移除
          vm.cros_one = fitst;   //篩選用資料
         
          
          //第二階段篩選資料
          vm.campaign = vm.cros_one.campaign;
          vm.media =  vm.cros_one.media;
          vm.link_type =  vm.cros_one.link_type;
          //GA篩選資料
          vm.ga1 = vm.cros_one.ga1.filter(function(e){return e}); //消除空值
          vm.ga2 =vm.cros_one.ga2.filter(function(e){return e});
          vm.ga3 =vm.cros_one.ga3.filter(function(e){return e});
         
          vm.clients = vm.cros_one.clients;
          const clients = vm.cros_one.clients; // 篩選用變數
          const  cros_new_table = [];  //總表格

          vm.cros = allcros;  // 總資料
          //--- 各個圖表的盒子
          let visBox = [];  //存放vis的盒子
          let CVBox = []; // 存放CV的盒子
          let ProfitBox = []; // 存放Profit的盒子
          let CVRateBox = []; //存放CVRate的盒子
          let PriceBox = [];
          let OrderType = [ //新規率 既存率 -ドレント　cros
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
          ]; //新規率+既存率
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
      
          
          const all_time = [];
         
          
          // 預設顏色
          let color_all = ["#f38181", "#fce38a", "#eaffd0", "#a8e6cf", "#fdffab", "#ffd3b6", "#ffaaa5", "#d4a5a5", "#ffecda", "#f9ffea", "#a6d0e4", "#ff6f3c", "#ff9a3c", "#ffc93c", "#17b978", "#a7ff83"];
          // 依據點選客戶產生二維空陣列
          
          for (let i = 0; i < clients.length; i++) {
             
            vm.cros.forEach(function(item){
              if(item.clientname.includes(clients[i]) == 1 ){
                   all_time.push(item.date);
              } 
            }); 
       

            OrderType[0].data.push(
              {
                x:  clients[i],
                y: 0
              },
            );
            OrderType[1].data.push(
              {
                x:  clients[i],
                y:  0
              },
            );
            Regular[0].data.push(
              {
                x:  clients[i],
                y: 0
              },
            );
            Regular[1].data.push(
              {
                x:  clients[i],
                y:  0
              },
            );

            cros_new_table.push(
              {
                client: clients[i],
                all_profits: 0,
                all_unitprices: 0,
                all_cvs: 0,
                all_ordertypes_1:0,
                all_ordertypes_2:0,
                all_regulars_1: 0,
                all_regulars_2: 0,
                all_visitors:0
              }
            );
            visBox.push(
              {
                data: [],
                label: clients[i],
                borderColor: color_all[i] || "#7ee5e5",
                backgroundColor: "#fff",
                fill: false
              },
            );
            CVBox.push(
              {
                data: [],
                label: clients[i],
                borderColor: color_all[i] || "#7ee5e5",
                backgroundColor: "#fff",
                fill: false
              },
            );
            ProfitBox.push(
              {
                data: [],
                label: clients[i],
                borderColor: color_all[i] || "#7ee5e5",
                backgroundColor: "#fff",
                fill: false
              },
            );
            CVRateBox.push(
              {
                data: [],
                label: clients[i],
                borderColor: color_all[i] || "#7ee5e5",
                backgroundColor: "#fff",
                fill: false
              },
            );
            PriceBox.push(
              {
                data: [],
                label: clients[i],
                borderColor: color_all[i] || "#7ee5e5",
                backgroundColor: "#fff",
                fill: false
              },
            );

          };

          for (let i = 0; i < clients.length; i++) {
            vm.cros.forEach(function (item) {
              if (item.clientname == visBox[i].label) {
                visBox[i].data.push(
                  {
                    x: item.date,
                    y: item.visitors
                  }

                );
              }
            });
            vm.cros.forEach(function (item) {
              if (item.clientname == CVBox[i].label) {
                CVBox[i].data.push(
                  {
                    x: item.date,
                    y: item.cv
                  }

                );
              }
            });
            vm.cros.forEach(function (item) {
              if (item.clientname == ProfitBox[i].label) {
                ProfitBox[i].data.push(
                  {
                    x: item.date,
                    y: item.profit
                  }

                );
              }
            });
            vm.cros.forEach(function (item) {
              if (item.clientname == CVRateBox[i].label) {
                CVRateBox[i].data.push(
                  {
                    x: item.date,
                    y: item.cvr
                  }

                );
              }
            });
            vm.cros.forEach(function (item) {
              if (item.clientname == PriceBox[i].label) {
                PriceBox[i].data.push(
                  {
                    x: item.date,
                    y: item.unitprice
                  }

                );
              }
            });
            
           vm.cros.forEach(function(item){
            
             if(item.clientname == OrderType[0].data[i].x){
              OrderType[0].data[i].y  +=  item.ordertype[0];
             }
             if(item.clientname ==  OrderType[1].data[i].x){
              OrderType[1].data[i].y   +=  item.ordertype[1];
            }
           

           });
           vm.cros.forEach(function(item){
            if(item.clientname ==  Regular[0].data[i].x){
              Regular[0].data[i].y  +=  item.regular[0];
            }
            if(item.clientname ==  Regular[1].data[i].x){
              Regular[1].data[i].y  +=  item.regular[1];
            }

           });
          
            
            vm.cros.forEach(function (item) {
              if (item.clientname == cros_new_table[i].client) {
                 cros_new_table[i].all_cvs  +=  item.cv;  
                 cros_new_table[i].all_profits +=  item.profit ;
                 cros_new_table[i].all_unitprices += item.unitprice;
                 cros_new_table[i].all_ordertypes_1 += item.ordertype[0];
                 cros_new_table[i].all_ordertypes_2 += item.ordertype[1];
                 cros_new_table[i].all_regulars_1 += item.regular[0];
                 cros_new_table[i].all_regulars_2 += item.regular[1];
                 cros_new_table[i].all_visitors += item.visitors;
              }
            });  

            let ordertypes_1 = cros_new_table[i].all_ordertypes_1 / cros_new_table[i].all_cvs;
            let ordertypes_2 = cros_new_table[i].all_ordertypes_2 / cros_new_table[i].all_cvs;
            let regulars_1 = cros_new_table[i].all_regulars_1 /  cros_new_table[i].all_cvs;
            let regulars_2 = cros_new_table[i].all_regulars_2 /  cros_new_table[i].all_cvs;

            cros_new_table[i].all_ordertypes_1 =  toCurrency_round_2(ordertypes_1);
            cros_new_table[i].all_ordertypes_2 = toCurrency_round_2(ordertypes_2);

            cros_new_table[i].all_regulars_1 = toCurrency_round_2( regulars_1);
            cros_new_table[i].all_regulars_2 = toCurrency_round_2( regulars_2);

            cros_new_table[i].all_profits = toCurrency_round(cros_new_table[i].all_profits);
            cros_new_table[i].all_unitprices = toCurrency_round(cros_new_table[i].all_unitprices);
            cros_new_table[i].all_cvs = toCurrency_round(cros_new_table[i].all_cvs);

          };
         
          

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
        
          // 放入表格
          vm.cros_table = cros_new_table;

          // 放入圖表
          vm.a_barChartVis.datasets = visBox;
          vm.a_barChartCV.datasets = CVBox;
          vm.a_barChartProfit.datasets = ProfitBox;
          vm.a_barChartCVRate.datasets = CVRateBox;
          vm.a_barChartPrice.datasets = PriceBox;
          vm.a_barChartOrderType.datasets = OrderType;
          vm.a_barChartRegular.datasets = Regular;
       
        
          vm.time = all_time.filter((item, key, arr) => arr.indexOf(item) == key);
          vm.time.sort(function(a, b){
            return a > b ? 1 : -1; // 
          });

          vm.a_barChartVis.labels = vm.time;
          vm.a_barChartCV.labels = vm.time;
          vm.a_barChartProfit.labels = vm.time;
          vm.a_barChartCVRate.labels = vm.time;
          vm.a_barChartPrice.labels = vm.time;

          vm.a_barChartOrderType.labels = clients;
          vm.a_barChartRegular.labels = clients;
          // 
          window.myBar1.update();
          window.myBar2.update();
          window.myBar3.update();
          window.myBar4.update();
          window.myBar5.update();
          window.myBar6.update();
          window.myBar7.update();


        },
        error: function (xhr) {
          alert("發生錯誤: ");
        }
      });


    },
    orderBytable(order_all,order_lowhight){
      const vm = this;
      let cros_new_table =[];
      for(let i = 0; i < vm.clients.length; i++){
            cros_new_table.push(
              {
                client: vm.clients[i],
                all_profits: 0,
                all_unitprices: 0,
                all_cvs: 0,
                all_ordertypes_1:0,
                all_ordertypes_2:0,
                all_regulars_1: 0,
                all_regulars_2: 0,
                all_visitors:0
              }
            ); //前置
            vm.cros.forEach(function (item) {
              if (item.clientname == cros_new_table[i].client) {
                 cros_new_table[i].all_cvs  +=  item.cv;  
                 cros_new_table[i].all_profits +=  item.profit ;
                 cros_new_table[i].all_unitprices += item.unitprice;
                 cros_new_table[i].all_ordertypes_1 += item.ordertype[0];
                 cros_new_table[i].all_ordertypes_2 += item.ordertype[1];
                 cros_new_table[i].all_regulars_1 += item.regular[0];
                 cros_new_table[i].all_regulars_2 += item.regular[1];
                 cros_new_table[i].all_visitors += item.visitors;
              }
            });  
          
      }
      
      if(order_lowhight == 'low'){
          // 由低開始 
      switch(order_all){
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
      }else if(order_lowhight == 'high'){
        switch(order_all){
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
      }
    
   
      for(let i = 0; i < vm.clients.length; i++){
        cros_new_table[i].all_ordertypes_1 = cros_new_table[i].all_ordertypes_1 / cros_new_table[i].all_cvs;
        cros_new_table[i].all_ordertypes_2 = cros_new_table[i].all_ordertypes_2 / cros_new_table[i].all_cvs;
        cros_new_table[i].all_regulars_1 = cros_new_table[i].all_regulars_1 /  cros_new_table[i].all_cvs;
        cros_new_table[i].all_regulars_2 = cros_new_table[i].all_regulars_2 /  cros_new_table[i].all_cvs;
      }
      if(order_lowhight == 'low'){
        switch(order_all){
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
      }else if(order_lowhight == 'high'){
        switch(order_all){
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
      
      vm.cros_table = cros_new_table ;
      
      
    } // table end 

  },
  computed: {
    creatdata() {
      const vm = this;
      let theDay = new Date()   // 建立時間物件
      let changeDay = 31        // 設定要往前或往後幾天
      vm.date1 = theDay.toISOString().substring(0,10);
      let timeStamp = theDay.setDate(theDay.getDate() + changeDay)      // theDay.getDate() 是用來取得今天是幾號
      vm.date2 = theDay.toISOString().substring(0,10);
    
      vm.getFilter();
    },
    ind_filter_case() {
      const vm = this;
      vm.allSelected_ind = false;

      return vm.ind.filter(function (item) {
        return item.toUpperCase().match(vm.ind_filter.toUpperCase());
      });
    },
    cli_filter_case() {
      const vm = this;
      return vm.cli.filter(function (item) {
        return item.toUpperCase().match(vm.cli_filter.toUpperCase());
      });
    },
    pro_filter_case() {
      const vm = this;
      return vm.pro.filter(function (item) {
        return item.toUpperCase().match(vm.pro_filter.toUpperCase());
      });
    }, // pro end 
    paymethod_filter_case(){
      const vm = this;
      return vm.paymethod.filter(function (item) {
        return item.name.toUpperCase().match(vm.paymethod_filter.toUpperCase());
      });
    }, //paymethod end 
    campaign_filter_case(){
      const vm = this;
      return vm.campaign.filter(function (item) {
        return item.toUpperCase().match(vm.campaign_filter.toUpperCase());
      });
    }, // Campaign end 
    ordertype_filter_case(){
      const vm = this; 
      return vm.ordertype.filter(function (item) {
        return item.toUpperCase().match(vm.ordertype_filter.toUpperCase());
      });
    },//ordertype end
    regular_filter_case(){
      const vm = this;
      return vm.regular.filter(function (item) {
        return item.toUpperCase().match(vm.regular_filter.toUpperCase());
      });
    },//regular end 
      media_filter_case(){
      const vm = this;
      return vm.media.filter(function (item) {
        return item.toUpperCase().match(vm.media_filter.toUpperCase());
      });
    },//regular end 
    link_type_filter_case(){
      const vm = this;
      return vm.link_type.filter(function (item) {
        return item.toUpperCase().match(vm.link_type_filter.toUpperCase());
      });
    },//regular end 
    ga1_filter_case(){
      const vm = this;
      return vm.ga1.filter(function (item) {
        return item.toUpperCase().match(vm.ga1_filter.toUpperCase());
      });
    },
    ga2_filter_case(){
      const vm = this;
      return vm.ga2.filter(function (item) {
        return item.toUpperCase().match(vm.ga2_filter.toUpperCase());
      });
    },
    ga3_filter_case(){
      const vm = this;
      return vm.ga3.filter(function (item) {
        return item.toUpperCase().match(vm.ga3_filter.toUpperCase());
      });
    },

  }//comp end

})