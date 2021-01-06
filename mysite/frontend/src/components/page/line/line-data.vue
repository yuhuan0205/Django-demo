<template lang="pug">
.page-content 
  .row 
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCPO
          .card-body
            h6.card-title CPO
              i.fas.fa-question.ml-3(type='button' data-toggle='modal' data-target='#exampleModal' @click="Description = 'cardCPO'")
            i.fas.fa-eye(@click="$chart_scale('cardCPO')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCPO
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCV
          .card-body
            h6.card-title CV
              i.fas.fa-question.ml-3(type='button' data-toggle='modal' data-target='#exampleModal' @click="Description = 'cardCV'")
            i.fas.fa-eye(@click="$chart_scale('cardCV')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCV 
  .row 
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCOST
          .card-body
            h6.card-title COST
              i.fas.fa-question.ml-3(type='button' data-toggle='modal' data-target='#exampleModal' @click="Description = 'cardCOST'")
            i.fas.fa-eye(@click="$chart_scale('cardCOST')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCOST 
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCVR
          .card-body
            h6.card-title CVR
              i.fas.fa-question.ml-3(type='button' data-toggle='modal' data-target='#exampleModal' @click="Description = 'cardCVR'")
            i.fas.fa-eye(@click="$chart_scale('cardCVR')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCVR 
  .row 
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCTR
          .card-body
            h6.card-title CTR
              i.fas.fa-question.ml-3(type='button' data-toggle='modal' data-target='#exampleModal' @click="Description = 'cardCTR'")
            i.fas.fa-eye(@click="$chart_scale('cardCTR')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCTR
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCPM
          .card-body
            h6.card-title CPM
              i.fas.fa-question.ml-3(type='button' data-toggle='modal' data-target='#exampleModal' @click="Description = 'cardCPM'")
            i.fas.fa-eye(@click="$chart_scale('cardCPM')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCPM 
  .row 
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardCPC
          .card-body
            h6.card-title CPC
              i.fas.fa-question.ml-3(type='button' data-toggle='modal' data-target='#exampleModal' @click="Description = 'cardCPC'")
            i.fas.fa-eye(@click="$chart_scale('cardCPC')")
            .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
            canvas#chartjsLineCPC 
    .col-xl-6.grid-margin.stretch-card
      .col-sm-12.ml-3
        .card.cardIMP
          .card-body
            h6.card-title IMP
              i.fas.fa-question.ml-3(type='button' data-toggle='modal' data-target='#exampleModal' @click="Description = 'cardIMP'")
            i.fas.fa-eye(@click="$chart_scale('cardIMP')")
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
  #exampleModal.modal.fade(tabindex='-1' role='dialog' aria-labelledby='exampleModalLabel' aria-hidden='true' )
      .modal-dialog(role='document' v-show="Description == item.name" v-for="  item  in Description_context" ).modal-dialog-centered
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
    LINETABLE(:line="line_df", v-if="sendNow", :clients="clients")
</template>

<script>
import LINETABLE from "@/components/table/line-table";
export default {
  components: {
    LINETABLE,
  },
  data() {
    return {
      line_df: [],
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
        { title:"CLICK" ,name:"cardCLICK" }

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
      date_df: "",
      sendNow: false,
    };
  },
  computed:{
     isLoading(){
        return  this.$store.state.dorento.isLoading_line;
     },
     new_data(){
        return  this.$store.state.dorento.line; //  綁定傳送
     },
     dateType(){
        return  this.$store.state.dorento.dateType
     },
  },
  watch: {
    dateType(){
       this.upDate();
     },
     new_data(){
       console.log(this.$store.state.dorento.line);
       this.upDate(); 
     },

   
  },
  methods: {  
    
    upDate() {
      console.time('line updata的執行時間');
      const vm = this;
      let line_df = this.$store.state.dorento.line;
      
      vm.line_df = line_df[1];
      if (!vm.dateType) {
        line_df = line_df[1];
      }
      if (vm.dateType == "m") {
        line_df = line_df[2];
      }
      if (vm.dateType == "q") {
        line_df = line_df[3];
      }
      vm.sendNow = true;
      let timeBox = [];
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
      let line_charts = [[], [], [], [], [], [], [], [], []];
      for (let cli in vm.clients) {
        for (let charts in line_charts) {
          line_charts[charts].push({
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
        ] = line_charts;
        line_df.forEach(function (item) {
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
      console.timeEnd('line updata的執行時間');
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

