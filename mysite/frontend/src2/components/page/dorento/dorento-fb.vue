<template lang="pug">
.page-content 
  .row 
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCPO
          .card-body
            h6.card-title CPO
            i.fas.fa-eye(@click="$chart_scale('cardCPO')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCPO
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCV
          .card-body
            h6.card-title CV
            i.fas.fa-eye(@click="$chart_scale('cardCV')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCV 
  .row 
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCOST
          .card-body
            h6.card-title COST
            i.fas.fa-eye(@click="$chart_scale('cardCOST')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCOST 
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCVR
          .card-body
            h6.card-title CVR
            i.fas.fa-eye(@click="$chart_scale('cardCVR')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCVR 
  .row 
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCTR
          .card-body
            h6.card-title CTR
            i.fas.fa-eye(@click="$chart_scale('cardCTR')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCTR
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCPM
          .card-body
            h6.card-title CPM
            i.fas.fa-eye(@click="$chart_scale('cardCPM')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCPM 
  .row 
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCPC
          .card-body
            h6.card-title CPC
            i.fas.fa-eye(@click="$chart_scale('cardCPC')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCPC 
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardIMP
          .card-body
            h6.card-title IMP
            i.fas.fa-eye(@click="$chart_scale('cardIMP')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineIMP 
  .row 
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCLICK
          .card-body
            h6.card-title CLICK
            i.fas.fa-eye
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCLICK 
  keep-alive 
    FBTABLE(:fb="fb_df", v-if="sendNow", :clients="clients") 
</template>

<script>
import $ from "jquery";
import FBTABLE from "@/components/table/dorento/dorento-fb-table";
export default {
  components: {
    FBTABLE,
  },
  data() {
    return {
      fb_df: [], // 表格
      clients: [], // 表格
      sendNow: false, // 表格狀態
      a_CPO: new_cpo,
      a_CV: new_cv,
      a_COST: new_cost,
      a_CVR: new_cvr,
      a_CTR: new_ctr,
      a_CPM: new_cpm,
      a_CPC: new_cpc,
      a_IMP: new_imp,
      a_CLICK: new_click
    };
  },
  watch: {
     dateType(){
       const vm = this;
       vm.upDate();
     },
     new_data(){
        this.upDate(); 
     },

  },
  computed:{
     isLoading(){
        return  this.$store.state.dorento.isLoading_fb;
     },
      new_data(){
        return  this.$store.state.dorento.fb; //  綁定傳送
     },
     dateType(){
        return  this.$store.state.dorento.dateType
     },
  },
  methods: {
    upDate() {
      const vm = this;
      let fb_df = this.$store.state.dorento.fb;

      vm.clients = fb_df[0].clients;
      vm.fb_df = fb_df[1];
      if (!vm.dateType) {
        fb_df = fb_df[1];
      }
      if (vm.dateType == "m") {
        fb_df = fb_df[2];
      }
      if (vm.dateType == "q") {
        fb_df = fb_df[3];
      }
      vm.sendNow = true;
      let timeBox = [];
      let fb_charts = [[], [], [], [], [], [], [], [], []];
      let color_all = [
        "#f38181",
        "#fce38a",
        "#eaffd0",
        "#a8e6cf",
        "#fdffab",
        "#ffd3b6",
        "#ffaaa5",
        "#d4a5a5",
        "#ffecda",
        "#f9ffea",
        "#a6d0e4",
        "#ff6f3c",
        "#ff9a3c",
        "#ffc93c",
        "#17b978",
        "#a7ff83",
      ];
      for (let cli in vm.clients) {
        for (let charts in fb_charts) {
          fb_charts[charts].push({
            data: [],
            label: vm.clients[cli],
            borderColor: color_all[cli] || "#7ee5e5",
            backgroundColor: "#fff",
            fill: false,
          });
        }
        let [
          cpoBox,
          cvBox,
          costBox,
          cvrBox,
          ctrBox,
          cpmBox,
          cpcBox,
          impBox,
          clickBox,
        ] = fb_charts;
        fb_df.forEach(function (item) {
          if (item.clientname.includes(vm.clients[cli]) == 1)
            timeBox.push(item.date);

          if (item.clientname == cpoBox[cli].label)
            cpoBox[cli].data.push({
              x: item.date,
              y: Math.round(item.cpo * 100)/100,
            });
          if (item.clientname == cvBox[cli].label)
            cvBox[cli].data.push({
              x: item.date,
              y: item.cv,
            });
          if (item.clientname == costBox[cli].label)
            costBox[cli].data.push({
              x: item.date,
              y: Math.round(item.cost * 100)/100,
            });
          if (item.clientname == cvrBox[cli].label)
            cvrBox[cli].data.push({
              x: item.date,
              y: Math.round(item.cvr *100) /100,
            });
          if (item.clientname == ctrBox[cli].label)
            ctrBox[cli].data.push({
              x: item.date,
              y: Math.round(item.ctr *100)/100,
            });
          if (item.clientname == cpmBox[cli].label)
            cpmBox[cli].data.push({
              x: item.date,
              y: Math.round(item.cpm *100)/100
            });
          if (item.clientname == cpcBox[cli].label)
            cpcBox[cli].data.push({
              x: item.date,
              y: Math.round(item.cpc * 100) / 100
            });
          if (item.clientname == impBox[cli].label)
            impBox[cli].data.push({
              x: item.date,
              y: item.impressions,
            });
          if (item.clientname == clickBox[cli].label)
            clickBox[cli].data.push({
              x: item.date,
              y: item.clicks,
            });
        });

        vm.a_CPO.datasets = cpoBox;
        vm.a_CV.datasets = cvBox;
        vm.a_COST.datasets = costBox;
        vm.a_CVR.datasets = cvrBox;

        vm.a_CTR.datasets = ctrBox;
        vm.a_CPM.datasets = cpmBox;
        vm.a_CPC.datasets = cpcBox;
        vm.a_IMP.datasets = impBox;
        vm.a_CLICK.datasets = clickBox;
      }
      timeBox = timeBox.filter((item, key, arr) => arr.indexOf(item) == key);
      timeBox.sort((a, b) => (a > b ? 1 : -1)); //
      // time
      vm.a_CPO.labels = timeBox;
      vm.a_CV.labels = timeBox;
      vm.a_COST.labels = timeBox;
      vm.a_CVR.labels = timeBox;
      vm.a_CTR.labels = timeBox;
      vm.a_CPM.labels = timeBox;
      vm.a_CPC.labels = timeBox;
      vm.a_IMP.labels = timeBox;
      vm.a_CLICK.labels = timeBox;

      window.myBarCPO.update();
      window.myBarCV.update();
      window.myBarCOST.update();
      window.myBarCVR.update();

      window.myBarCTR.update();
      window.myBarCPM.update();
      window.myBarCPC.update();
      window.myBarIMP.update();
      window.myBarCLICK.update();
    },
  },
  activated() {
   
    $(function () {
      if ($("#chartjsLineCPO").length) {
        (Chart.defaults.global.defaultFontFamily = "Noto Sans JP"),
          (window.myBarCPO = new Chart($("#chartjsLineCPO"), {
            type: "line",
            data: new_cpo,
          }));
      } // CH END
      if ($("#chartjsLineCV").length) {
        (Chart.defaults.global.defaultFontFamily = "Noto Sans JP"),
          (window.myBarCV = new Chart($("#chartjsLineCV"), {
            type: "line",
            data: new_cv,
          }));
      } // CH END
      if ($("#chartjsLineCOST").length) {
        (Chart.defaults.global.defaultFontFamily = "Noto Sans JP"),
          (window.myBarCOST = new Chart($("#chartjsLineCOST"), {
            type: "line",
            data: new_cost,
          }));
      } // CH END
      if ($("#chartjsLineCVR").length) {
        (Chart.defaults.global.defaultFontFamily = "Noto Sans JP"),
          (window.myBarCVR = new Chart($("#chartjsLineCVR"), {
            type: "line",
            data: new_cvr,
          }));
      } // CH END
      if ($("#chartjsLineCTR").length) {
        (Chart.defaults.global.defaultFontFamily = "Noto Sans JP"),
          (window.myBarCTR = new Chart($("#chartjsLineCTR"), {
            type: "line",
            data: new_ctr,
          }));
      } // CH END
      if ($("#chartjsLineCPM").length) {
        (Chart.defaults.global.defaultFontFamily = "Noto Sans JP"),
          (window.myBarCPM = new Chart($("#chartjsLineCPM"), {
            type: "line",
            data: new_cpm,
          }));
      } // CH END
      if ($("#chartjsLineCPC").length) {
        (Chart.defaults.global.defaultFontFamily = "Noto Sans JP"),
          (window.myBarCPC = new Chart($("#chartjsLineCPC"), {
            type: "line",
            data: new_cpc,
          }));
      } // CH END
      if ($("#chartjsLineIMP").length) {
        (Chart.defaults.global.defaultFontFamily = "Noto Sans JP"),
          (window.myBarIMP = new Chart($("#chartjsLineIMP"), {
            type: "line",
            data: new_imp,
          }));
      } // CH END
      if ($("#chartjsLineCLICK").length) {
        (Chart.defaults.global.defaultFontFamily = "Noto Sans JP"),
          (window.myBarCLICK = new Chart($("#chartjsLineCLICK"), {
            type: "line",
            data: new_click,
          }));
      } // CH END
    }); //FUNCTION END
   
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
  }, // activated end
}; // VUE END
var new_cpo = {
  labels: [],
  datasets: [],
};
var new_cv = {
  labels: [],
  datasets: [],
};
var new_cost = {
  labels: [],
  datasets: [],
};
var new_cvr = {
  labels: [],
  datasets: [],
};
var new_ctr = {
  labels: [],
  datasets: [],
};
var new_cpm = {
  labels: [],
  datasets: [],
};
var new_cpc = {
  labels: [],
  datasets: [],
};
var new_imp = {
  labels: [],
  datasets: [],
};
var new_click = {
  labels: [],
  datasets: [],
};
</script>


