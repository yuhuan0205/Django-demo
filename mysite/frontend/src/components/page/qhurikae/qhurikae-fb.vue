<template lang="pug">
.page-content
  .row
    .col-xl-12.d-flex.justify-content-center
      h1.mb-5 {{ String(clients) }}
  .row 
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCPO
          .card-body
            h6.card-title CPO
              i.fas.fa-question.ml-3(type='button' data-toggle='modal' data-target='#exampleModal' @click="Description = 'cardCPO'")
            i.fas.fa-eye(@click="chart_scale('cardCPO')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCPO
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCV
          .card-body
            h6.card-title CV
              i.fas.fa-question.ml-3(type='button' data-toggle='modal' data-target='#exampleModal' @click="Description = 'cardCV'")
            i.fas.fa-eye(@click="chart_scale('cardCV')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCV 
  .row 
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCOST
          .card-body
            h6.card-title COST
              i.fas.fa-question.ml-3(type='button' data-toggle='modal' data-target='#exampleModal' @click="Description = 'cardCOST'")
            i.fas.fa-eye(@click="chart_scale('cardCOST')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCOST 
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCVR
          .card-body
            h6.card-title CVR
              i.fas.fa-question.ml-3(type='button' data-toggle='modal' data-target='#exampleModal' @click="Description = 'cardCVR'")
            i.fas.fa-eye(@click="chart_scale('cardCVR')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCVR 
  .row 
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCTR
          .card-body
            h6.card-title CTR
              i.fas.fa-question.ml-3(type='button' data-toggle='modal' data-target='#exampleModal' @click="Description = 'cardCTR'")
            i.fas.fa-eye(@click="chart_scale('cardCTR')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCTR
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCPM
          .card-body
            h6.card-title CPM
              i.fas.fa-question.ml-3(type='button' data-toggle='modal' data-target='#exampleModal' @click="Description = 'cardCPM'")
            i.fas.fa-eye(@click="chart_scale('cardCPM')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCPM 
  .row 
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCPC
          .card-body
            h6.card-title CPC
              i.fas.fa-question.ml-3(type='button' data-toggle='modal' data-target='#exampleModal' @click="Description = 'cardCPC'")
            i.fas.fa-eye(@click="chart_scale('cardCPC')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCPC 
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardIMP
          .card-body
            h6.card-title IMP
              i.fas.fa-question.ml-3(type='button' data-toggle='modal' data-target='#exampleModal' @click="Description = 'cardIMP'")
            i.fas.fa-eye(@click="chart_scale('cardIMP')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineIMP 
  .row 
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCLICK
          .card-body
            h6.card-title CLICK
              i.fas.fa-question.ml-3(type='button' data-toggle='modal' data-target='#exampleModal' @click="Description = 'cardCLICK'")
            i.fas.fa-eye
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCLICK 
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCOST_CPO
          .card-body
            h6.card-title COST x CPO
              i.fas.fa-question.ml-3(type='button' data-toggle='modal' data-target='#exampleModal' @click="Description = 'cardCOSTCPO'")
            i.fas.fa-eye(@click="chart_scale('cardCOST_CPO')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCOST_CPO 
  .row
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCPO_CV
          .card-body
            h6.card-title CPO x CV
              i.fas.fa-question.ml-3(type='button' data-toggle='modal' data-target='#exampleModal' @click="Description = 'cardCPOCV'")
            i.fas.fa-eye(@click="chart_scale('cardCPO_CV')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCPO_CV
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCPO_CPM
          .card-body
            h6.card-title CPO x CPM
              i.fas.fa-question.ml-3(type='button' data-toggle='modal' data-target='#exampleModal' @click="Description = 'cardCPOCPM'")
            i.fas.fa-eye(@click="chart_scale('cardCPO_CPM')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCPO_CPM
  .row
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCTR_CVR
          .card-body
            h6.card-title CTR x CVR
              i.fas.fa-question.ml-3(type='button' data-toggle='modal' data-target='#exampleModal' @click="Description = 'cardCTRCVR'")
            i.fas.fa-eye(@click="chart_scale('cardCTR_CVR')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCTR_CVR
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCPM_CVR
          .card-body
            h6.card-title CPM x CVR
              i.fas.fa-question.ml-3(type='button' data-toggle='modal' data-target='#exampleModal' @click="Description = 'cardCPMCVR'")
            i.fas.fa-eye(@click="chart_scale('cardCPM_CVR')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCPM_CVR
  .row 
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCPM_CTR_CVR
          .card-body
            h6.card-title CPM x CTR x CVR
              i.fas.fa-question.ml-3(type='button' data-toggle='modal' data-target='#exampleModal' @click="Description = 'cardCPMCTRCVR'")
            i.fas.fa-eye(@click="chart_scale('cardCPM_CTR_CVR')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCPM_CTR_CVR 
  #exampleModal.modal.fade(tabindex='-1' role='dialog' aria-labelledby='exampleModalLabel' aria-hidden='true' )
      .modal-dialog(role='document' v-show="Description == item.name " v-for="  item  in Description_context" ).modal-dialog-centered
        .modal-content
          .modal-header
            h5#exampleModalLabel.modal-title {{item.title}}
            button.close(type='button' data-dismiss='modal' aria-label='Close')
              span(aria-hidden='true') &times;
          .modal-body
            | ...
          .modal-footer
            button.btn.btn-secondary(type='button' data-dismiss='modal') Close          
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
      fb_df: [],
      clients: [],
      data: [],
      Description: "",
      Description_context: [
        { title:"CPO" , name:"cardCPO"},
        { title:"CV" ,name:"cardCV"},
        { title:"COST" ,name:"cardCOST"},
        { title:"CVR" ,name:"cardCVR"},
        { title:"CTR" ,name:"cardCTR"} ,
        { title:"CPM" ,name:"cardCPM"} ,
        { title:"CPC" ,name:"cardCPC"} ,
        { title:"IMP" ,name:"cardIMP"} ,
        { title:"CLICK" ,name:"cardCLICK" },
        { title:"COST x CPO",name:"cardCOSTCPO"},
        { title:"CPO x CV",name:"cardCPOCV"},
        { title:"CPO x CPM",name:"cardCPOCPM"},
        { title:"CTR x CVR",name:"cardCTRCVR"},
        { title:"CPM x CVR",name:"cardCPMCVR"},
        { title:"CPM x CTR x CVR",name:"cardCPMCTRCVR"},

      ],
      a_CPO: new_cpo,
      a_CV: new_cv,
      a_COST: new_cost,
      a_CVR: new_cvr,
      a_CTR: new_ctr,
      a_CPM: new_cpm,
      a_CPC: new_cpc,
      a_IMP: new_imp,
      a_CLICK: new_click,
      a_COST_CPO: new_COST_CPO,
      a_CPO_CV: new_CPO_CV,
      a_CPO_CPM: new_CPO_CPM,
      a_CTR_CVR: new_CTR_CVR,
      a_CPM_CVR: new_CPM_CVR,
      a_CPM_CTR_CVR: new_CPM_CTR_CVR,
      date1: "",
      date2: "",
      sendNow: false,
    };
  },
  watch: {
     dateType(){
       this.upDate();
     },
     new_data(){
        this.upDate(); 
     },
  },
   computed:{
     isLoading(){
        return  this.$store.state.qhurikae.isLoading_fb;
     },
      new_data(){
        return  this.$store.state.qhurikae.fb; //  綁定傳送
     },
     dateType(){
        return  this.$store.state.qhurikae.dateType
     },
  },
  methods: {
    openModal() {
      $("#cliModal").modal("show");
    },
    chart_scale(card) {
      console.log(card);
      const acard = document.querySelector(`.${card}`);
      screenfull.request(acard);
      if (screenfull) {
        screenfull.exit(acard);
      }
    },
    upDate() {
    const vm = this;
    let fb_df = this.$store.state.qhurikae.fb;
    let clients = [] ;
    clients =  fb_df[0].clients;
    vm.clients = clients
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
      console.log(fb_charts);
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
            y: item.cpo,
          });
        if (item.clientname == cvBox[cli].label)
          cvBox[cli].data.push({
            x: item.date,
            y: item.cv,
          });
        if (item.clientname == costBox[cli].label)
          costBox[cli].data.push({
            x: item.date,
            y: item.cost,
          });
        if (item.clientname == cvrBox[cli].label)
          cvrBox[cli].data.push({
            x: item.date,
            y: toCurrency_round(item.cvr),
          });
        if (item.clientname == ctrBox[cli].label)
          ctrBox[cli].data.push({
            x: item.date,
            y: toCurrency_round(item.ctr),
          });
        if (item.clientname == cpmBox[cli].label)
          cpmBox[cli].data.push({
            x: item.date,
            y: item.cpm,
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
      vm.a_CPO.datasets[0].label = "CPO";

      vm.a_CV.datasets = cvBox;
      vm.a_CV.datasets[0].label = "CV";

      vm.a_COST.datasets = costBox;
      vm.a_COST.datasets[0].label = "COST";

      vm.a_CVR.datasets = cvrBox;
      vm.a_CVR.datasets[0].label = "CVR";

      vm.a_CTR.datasets = ctrBox;
      vm.a_CTR.datasets[0].label = "CTR";

      vm.a_CPM.datasets = cpmBox;
      vm.a_CPM.datasets[0].label = "CPM";

      vm.a_CPC.datasets = cpcBox;
      vm.a_CPC.datasets[0].label = "CPC";

      vm.a_IMP.datasets = impBox;
      vm.a_IMP.datasets[0].label = "IMP";

      vm.a_CLICK.datasets = clickBox;
      vm.a_CLICK.datasets[0].label = "CLICK";

      vm.a_COST_CPO.datasets[0].data = costBox[0].data; // COST
      vm.a_COST_CPO.datasets[1].data = cpoBox[0].data; // Cpo

      vm.a_CPO_CV.datasets[0].data = cpoBox[0].data; // Cpo
      vm.a_CPO_CV.datasets[1].data = cvBox[0].data; // Cv

      vm.a_CPO_CPM.datasets[0].data = cpoBox[0].data; // Cpo
      vm.a_CPO_CPM.datasets[1].data = cpmBox[0].data; // cpm

      vm.a_CTR_CVR.datasets[0].data = ctrBox[0].data; // Ctr
      vm.a_CTR_CVR.datasets[1].data = cvrBox[0].data; // cvr

      vm.a_CPM_CVR.datasets[0].data = cpmBox[0].data; // cpm
      vm.a_CPM_CVR.datasets[1].data = cvrBox[0].data; // cvr

      vm.a_CPM_CTR_CVR.datasets[0].data = cpmBox[0].data; // cpm
      vm.a_CPM_CTR_CVR.datasets[1].data = ctrBox[0].data; // ctr
      vm.a_CPM_CTR_CVR.datasets[2].data = cvrBox[0].data; // cvr
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
    vm.a_COST_CPO.labels = timeBox;
    vm.a_CPO_CV.labels = timeBox;
    vm.a_CPO_CPM.labels = timeBox;
    vm.a_CTR_CVR.labels = timeBox;
    vm.a_CPM_CVR.labels = timeBox;
    vm.a_CPM_CTR_CVR.labels = timeBox;

    window.myBarCPO.update();
    window.myBarCV.update();
    window.myBarCOST.update();
    window.myBarCVR.update();

    window.myBarCTR.update();
    window.myBarCPM.update();
    window.myBarCPC.update();
    window.myBarIMP.update();
    window.myBarCLICK.update();
    window.myBarCOST_CPO.update();
    window.myBarCPO_CV.update();
    window.myBarCPO_CPM.update();
    window.myBarCTR_CVR.update();
    window.myBarCPM_CVR.update();
    window.myBarCPM_CTR_CVR.update();
    function toCurrency_round(num) {
      let new_num = Math.round(num * 10000) / 100;

      var parts = new_num.toString().split(".");
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      return parts.join(".");
    }
    
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
      if ($("#chartjsLineCOST_CPO").length) {
        (Chart.defaults.global.defaultFontFamily = "Noto Sans JP"),
          (window.myBarCOST_CPO = new Chart($("#chartjsLineCOST_CPO"), {
            type: "line",
            data: new_COST_CPO,
            options: {
              responsive: true,
              stacked: false,
              hoverMode: "index",
              scales: {
                yAxes: [
                  {
                    type: "linear", // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
                    display: true,
                    position: "left",
                    id: "y-axis-1",
                  },
                  {
                    type: "linear", // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
                    display: true,
                    position: "right",
                    id: "y-axis-2",
                    gridLines: {
                      drawOnChartArea: false,
                    },
                  },
                ],
              },
            },
          }));
      } // CH END
      if ($("#chartjsLineCPO_CV").length) {
        (Chart.defaults.global.deCPO_CVfaultFontFamily = "Noto Sans JP"),
          (window.myBarCPO_CV = new Chart($("#chartjsLineCPO_CV"), {
            type: "line",
            data: new_CPO_CV,
            options: {
              responsive: true,
              stacked: false,
              hoverMode: "index",
              scales: {
                yAxes: [
                  {
                    type: "linear", // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
                    display: true,
                    position: "left",
                    id: "y-axis-1",
                  },
                  {
                    type: "linear", // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
                    display: true,
                    position: "right",
                    id: "y-axis-2",
                    gridLines: {
                      drawOnChartArea: false,
                    },
                  },
                ],
              },
            },
          }));
      } // CH END
      if ($("#chartjsLineCPO_CPM").length) {
        (Chart.defaults.global.deCPO_CVfaultFontFamily = "Noto Sans JP"),
          (window.myBarCPO_CPM = new Chart($("#chartjsLineCPO_CPM"), {
            type: "line",
            data: new_CPO_CPM,
            options: {
              responsive: true,
              stacked: false,
              hoverMode: "index",
              scales: {
                yAxes: [
                  {
                    type: "linear", // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
                    display: true,
                    position: "left",
                    id: "y-axis-1",
                  },
                  {
                    type: "linear", // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
                    display: true,
                    position: "right",
                    id: "y-axis-2",
                    gridLines: {
                      drawOnChartArea: false,
                    },
                  },
                ],
              },
            },
          }));
      } // CH END
      if ($("#chartjsLineCTR_CVR").length) {
        (Chart.defaults.global.deCPO_CVfaultFontFamily = "Noto Sans JP"),
          (window.myBarCTR_CVR = new Chart($("#chartjsLineCTR_CVR"), {
            type: "line",
            data: new_CTR_CVR,
            options: {
              responsive: true,
              stacked: false,
              hoverMode: "index",
              scales: {
                yAxes: [
                  {
                    type: "linear", // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
                    display: true,
                    position: "left",
                    id: "y-axis-1",
                  },
                  {
                    type: "linear", // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
                    display: true,
                    position: "right",
                    id: "y-axis-2",
                    gridLines: {
                      drawOnChartArea: false,
                    },
                  },
                ],
              },
            },
          }));
      } // CH END
      if ($("#chartjsLineCPM_CVR").length) {
        (Chart.defaults.global.deCPO_CVfaultFontFamily = "Noto Sans JP"),
          (window.myBarCPM_CVR = new Chart($("#chartjsLineCPM_CVR"), {
            type: "line",
            data: new_CPM_CVR,
            options: {
              responsive: true,
              stacked: false,
              hoverMode: "index",
              scales: {
                yAxes: [
                  {
                    type: "linear", // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
                    display: true,
                    position: "left",
                    id: "y-axis-1",
                  },
                  {
                    type: "linear", // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
                    display: true,
                    position: "right",
                    id: "y-axis-2",
                    gridLines: {
                      drawOnChartArea: false,
                    },
                  },
                ],
              },
            },
          }));
      } // CH END
      if ($("#chartjsLineCPM_CTR_CVR").length) {
        (Chart.defaults.global.deCPO_CVfaultFontFamily = "Noto Sans JP"),
          (window.myBarCPM_CTR_CVR = new Chart($("#chartjsLineCPM_CTR_CVR"), {
            type: "line",
            data: new_CPM_CTR_CVR,
            options: {
              responsive: true,
              stacked: false,
              hoverMode: "index",
              scales: {
                yAxes: [
                  {
                    type: "linear", // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
                    display: true,
                    position: "left",
                    id: "y-axis-1",
                  },
                  {
                    type: "linear", // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
                    display: true,
                    position: "right",
                    id: "y-axis-2",
                    gridLines: {
                      drawOnChartArea: false,
                    },
                  },
                ],
              },
            },
          }));
      } // CH END
    }); //FUNCTION END
      let mode = "";
          if(this.$route.name =='qhurikae-cros'){
              mode = "cros"; 
           }
           if(this.$route.name =='qhurikae-fb'){
              mode = "fb";  
           } 
            if(this.$route.name =='qhurikae-line'){
              mode = "line";  
           }   
        this.$store.dispatch('qhurikae/getMode',mode);
        this.$store.dispatch('qhurikae/getData');
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
var new_COST_CPO = {
  labels: [],
  datasets: [
    {
      label: "COST",
      backgroundColor: "#f38181",
      borderColor: "#f38181",
      yAxisID: "y-axis-1",
      data: [],
      fill: false,
    },
    {
      label: "CPO",
      backgroundColor: "#fff",
      borderColor: "#fff",
      yAxisID: "y-axis-2",
      data: [],
      fill: false,
    },
  ],
};
var new_CPO_CV = {
  labels: [],
  datasets: [
    {
      label: "CPO",
      backgroundColor: "#f38181",
      borderColor: "#f38181",
      yAxisID: "y-axis-1",
      data: [],
      fill: false,
    },
    {
      label: "CV",
      backgroundColor: "#fff",
      borderColor: "#fff",
      yAxisID: "y-axis-2",
      data: [],
      fill: false,
    },
  ],
};
var new_CPO_CPM = {
  labels: [],
  datasets: [
    {
      label: "CPO",
      backgroundColor: "#f38181",
      borderColor: "#f38181",
      yAxisID: "y-axis-1",
      data: [],
      fill: false,
    },
    {
      label: "CPM",
      backgroundColor: "#fff",
      borderColor: "#fff",
      yAxisID: "y-axis-2",
      data: [],
      fill: false,
    },
  ],
};
var new_CTR_CVR = {
  labels: [],
  datasets: [
    {
      label: "CTR",
      backgroundColor: "#f38181",
      borderColor: "#f38181",
      yAxisID: "y-axis-1",
      data: [],
      fill: false,
    },
    {
      label: "CVR",
      backgroundColor: "#fff",
      borderColor: "#fff",
      yAxisID: "y-axis-2",
      data: [],
      fill: false,
    },
  ],
};
var new_CPM_CVR = {
  labels: [],
  datasets: [
    {
      label: "CPM",
      backgroundColor: "#f38181",
      borderColor: "#f38181",
      yAxisID: "y-axis-1",
      data: [],
      fill: false,
    },
    {
      label: "CVR",
      backgroundColor: "#fff",
      borderColor: "#fff",
      yAxisID: "y-axis-2",
      data: [],
      fill: false,
    },
  ],
};
var new_CPM_CTR_CVR = {
  labels: [],
  datasets: [
    {
      label: "CPM",
      backgroundColor: "#f38181",
      borderColor: "#f38181",
      yAxisID: "y-axis-1",
      data: [],
      fill: false,
    },
    {
      label: "CTR",
      backgroundColor: "#a6d0e4",
      borderColor: "#a6d0e4",
      yAxisID: "y-axis-2",
      data: [],
      fill: false,
    },
    {
      label: "CVR",
      backgroundColor: "#ffecda",
      borderColor: "#ffecda",
      yAxisID: "y-axis-2",
      data: [],
      fill: false,
    },
  ],
};
</script>


<style>
</style>