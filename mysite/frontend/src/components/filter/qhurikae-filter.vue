<template lang="pug">
.dropdown-filter.col-sm-12
  h4.wrapper_back.mt-3(@click="backpage") 
    i.fas.fa-arrow-left.close-filter
    span.ml-3.close-filter 閉じる
  .title-filter.mb-5
    h1 検索条件 ドレント
  .container 
    .wrpapperbox-set
      .wrapperbox
        .all-label-box
          .row(v-show="nowstep == 'one'")
            .labelbox.col-4
              .col-12
                h4 産業別
                  i.fas.fa-eraser(@click="clickClear('ind')")
                input.search_box(placeholder="キーワード入力", v-model="ind_filter") 

                .label-wrapper
                  label 
                    input(
                      type="checkbox",
                      @change="clickAll('ind')",
                      v-model="allSelected_ind"
                    )
                    | 全選
                  label(v-for="item in indFD") 
                    input(
                      type="checkbox",
                      @change="clickFilter('ind')",
                      v-model="ind_send",
                      :value="item"
                    )
                    | {{ item }}
            .labelbox.col-4
              .col-12
                h4 クライアント
                  i.fas.fa-eraser(@click="clickClear('cli')")
                input.search_box(placeholder="キーワード入力", v-model="cli_filter") 

                .label-wrapper 
                  label(v-for="item in cliFD") 
                    input(
                      type="radio",
                      @change="clickFilter('cli')",
                      v-model="cli_send",
                      :value="item"
                    )
                    | {{ item }}
            .labelbox.col-4
              .col-12
                h4 商品名
                  i.fas.fa-eraser(@click="clickClear('pro')")
                input.search_box(placeholder="キーワード入力", v-model="pro_filter") 
                .label-wrapper 
                  label 
                    input(
                      type="checkbox",
                      @change="clickAll('pro')",
                      v-model="allSelected_pro"
                    )
                    | 全選
                  label(v-for="item in proFD") 
                    input(
                      type="checkbox",
                      @change="clickFilter('pro')",
                      v-model="pro_send",
                      :value="item"
                    )
                    | {{ item }}
          .row(v-show="nowstep == 'two'")
            .labelbox
              h4 支払い
                i.fas.fa-eraser(@click="clickClear('paymethod')")
              input.search_box(
                placeholder="キーワード入力",
                v-model="paymethod_filter"
              ) 
              .label-wrapper 
                label 
                  input(
                    type="checkbox",
                    @change="clickAll('paymethod')",
                    v-model="allSelected_paymethod"
                  )
                  | 全選
                label(v-for="item in paymethodFD") 
                  input(
                    type="checkbox",
                    v-model="paymethod_send",
                    :value="item.value"
                  )
                  | {{ item.name }}
            .labelbox
              h4 新規 / 既存
                i.fas.fa-eraser(@click="clickClear('ordertype')")
              input.search_box(
                placeholder="キーワード入力",
                v-model="ordertype_filter"
              ) 

              .label-wrapper 
                label 
                  input(
                    type="checkbox",
                    @change="clickAll('ordertype')",
                    v-model="allSelected_ordertype"
                  )
                  | 全選
                label(v-for="item in ordertypeFD") 
                  input(
                    type="checkbox",
                    v-model="ordertype_send",
                    :value="item"
                  )
                  | {{ item }}
            .labelbox
              h4 定期 / 都度
                i.fas.fa-eraser(@click="clickClear('regular')")
              input.search_box(placeholder="キーワード入力", v-model="regular_filter") 

              .label-wrapper 
                label 
                  input(
                    type="checkbox",
                    @change="clickAll('regular')",
                    v-model="allSelected_regular"
                  )
                  | 全選
                label(v-for="item in regularFD") 
                  input(type="checkbox", v-model="regular_send", :value="item")
                  | {{ item }}
          .row(v-show="nowstep == 'two'") 
            .labelbox
              h4 キャンペーン名
                i.fas.fa-eraser(@click="clickClear('campaign')") 
              input.search_box(
                placeholder="キーワード入力",
                v-model="campaign_filter"
              ) 
              .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
              .label-wrapper 
                label 
                  input(
                    type="checkbox",
                    @change="clickAll('campaign')",
                    v-model="allSelected_campaign"
                  )
                  | 全選
                label(v-for="item in campaignFD") 
                  input(
                    type="checkbox",
                    v-model="campaign_send",
                    :value="item"
                  )
                  | {{ item }}
            .labelbox
              h4 媒体別
                i.fas.fa-eraser(@click="clickClear('media')")
              input.search_box(placeholder="キーワード入力", v-model="media_filter") 
              .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
              .label-wrapper 
                label 
                  input(
                    type="checkbox",
                    @change="clickAll('media')",
                    v-model="allSelected_media"
                  )
                  | 全選
                label(v-for="item in mediaFD") 
                  input(type="checkbox", v-model="media_send", :value="item")
                  | {{ item }}
            .labelbox
              h4 リンク別
                i.fas.fa-eraser(@click="clickClear('link_type')")
              input.search_box(
                placeholder="キーワード入力",
                v-model="link_type_filter"
              ) 
              .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
              .label-wrapper 
                label 
                  input(
                    type="checkbox",
                    @change="clickAll('link_type')",
                    v-model="allSelected_link_type"
                  )
                  | 全選
                label(v-for="item in link_type_FD") 
                  input(
                    type="checkbox",
                    v-model="link_type_send",
                    :value="item"
                  )
                  | {{ item }}
          .row(v-show="nowstep == 'ga'") 
            .labelbox
              h4 GA1
                i.fas.fa-eraser(@click="clickClear('ga1')") 
              input.search_box(placeholder="キーワード入力") 
              .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
              .label-wrapper 
                label 
                  input(
                    type="checkbox",
                    @change="clickAll('ga1')",
                    v-model="allSelected_ga1"
                  )
                  | 全選
                label(v-for="item in ga1FD") 
                  input(type="checkbox", v-model="ga1_send", :value="item")
                  | {{ item }}
            .labelbox
              h4 GA2
                i.fas.fa-eraser(@click="clickClear('ga2')")
              input.search_box(placeholder="キーワード入力", v-model="media_filter") 
              .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
              .label-wrapper 
                label 
                  input(
                    type="checkbox",
                    @change="clickAll('ga2')",
                    v-model="allSelected_ga2"
                  )
                  | 全選
                label(v-for="item in ga2FD") 
                  input(type="checkbox", v-model="ga2_send", :value="item")
                  | {{ item }}
            .labelbox
              h4 GA3
                i.fas.fa-eraser(@click="clickClear('ga3')")
              input.search_box(placeholder="キーワード入力", v-model="pro_filter") 
              .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
              .label-wrapper 
                label 
                  input(
                    type="checkbox",
                    @change="clickAll('ga3')",
                    v-model="allSelected_ga3"
                  )
                  | 全選
                label(v-for="item in ga3FD") 
                  input(type="checkbox", v-model="ga3_send", :value="item")
                  | {{ item }}
      .button-item
        button.send-filter(v-show="nowstep == 'one'", @click="sendFilter2") さらに検索
        button.send-filter(v-show="nowstep =='two'", @click="nowstep = 'one'") 戻り
        button.send-filter(v-show="nowstep =='ga'", @click="nowstep = 'two'") 戻り
        button.send-filter.send-filter-send.mb-3(
          @click="sendFilter") 檢索
          i.fas.fa-search.ml-1
        button.ga-filter-style(v-show="nowstep =='two'", @click="sendFilter2")
           span GA
           i.fas.fa-chart-pie.ml-2
</template>

<script>
export default {
  data() {
    return {
      //傳參
      ind_send: [],
      cli_send: "",
      pro_send: [],
      campaign_send: [],
      media_send: [],
      paymethod_send: [],
      ordertype_send: [],
      regular_send: [],
      link_type_send: [],
      ga1_send: [],
      ga2_send: [],
      ga3_send: [],
      data: [],
      ind: [],
      cli: [],
      pro: [],
      campaign: [],
      media: [],
      paymethod: [
        //支払い

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
        },
      ],
      ordertype: ["新規", "既存"], //新規既存
      regular: ["定期", "都度"], // 定都
      media: [], //媒體別
      link_type: [], //リンク別
      ga1: [],
      ga2: [],
      ga3: [],
      ind_df: [],
      cli_df: [],
      pro_df: [],
      ind_filter: "",
      cli_filter: "",
      pro_filter: "",
      campaign_filter: "",
      media_filter: "",
      link_type_filter: "",
      paymethod_filter: "",
      ordertype_filter: "",
      regular_filter: "",
      ga1_filter: "",
      ga2_filter: "",
      ga3_filter: "",
      allSelected_ind: false,
      allSelected_cli: false,
      allSelected_pro: false,
      allSelected_campaign: false,
      allSelected_paymethod: false,
      allSelected_ordertype: false,
      allSelected_regular: false,
      allSelected_media: false,
      allSelected_link_type: false,
      allSelected_ga1: false,
      allSelected_ga2: false,
      allSelected_ga3: false,
      nowstep: "one",
    };
  },

  computed: {
    isLoading() {
      switch (this.$store.state.qhurikae.mode) {
        case "cros":
          return this.$store.state.qhurikae.isLoading_cros;
          break;
        case "fb":
          return this.$store.state.qhurikae.isLoading_fb;
          break;
        case "line":
          return this.$store.state.qhurikae.isLoading_line;
      }
    },
    indFD() {
      const vm = this;
      let ind = [];
       ind = vm.ind.filter(function (item) {
          return   item.toUpperCase().match(vm.ind_filter.toUpperCase());
       });
       return  ind.filter((item, key, arr) => arr.indexOf(item) == key);
    }, // ind
    cliFD() {
      const vm = this;
      let cli = []; 
      cli = vm.cli.filter(function (item) {
        return item.toUpperCase().match(vm.cli_filter.toUpperCase());
      });
      return  cli.filter((item, key, arr) => arr.indexOf(item) == key);
    }, // cli
    proFD() {
      const vm = this;
      let pro = [];
      pro = vm.pro.filter(function (item) {
        return item.toUpperCase().match(vm.pro_filter.toUpperCase());
      });
       return  pro.filter((item, key, arr) => arr.indexOf(item) == key);
    }, // pro
    campaignFD() {
      const vm = this;
      return vm.campaign.filter(function (item) {
        return item.toUpperCase().match(vm.campaign_filter.toUpperCase());
      });
    },
    mediaFD() {
      const vm = this;
      return vm.media.filter(function (item) {
        return item.toUpperCase().match(vm.media_filter.toUpperCase());
      });
    },
    link_type_FD() {
      const vm = this;
      return vm.link_type.filter(function (item) {
        return item.toUpperCase().match(vm.link_type_filter.toUpperCase());
      });
    },
    paymethodFD() {
      const vm = this;
      return vm.paymethod.filter(function (item) {
        return item.name.toUpperCase().match(vm.paymethod_filter.toUpperCase());
      });
    },
    ordertypeFD() {
      const vm = this;
      return vm.ordertype.filter(function (item) {
        return item.toUpperCase().match(vm.ordertype_filter.toUpperCase());
      });
    },
    regularFD() {
      const vm = this;
      return vm.regular.filter(function (item) {
        return item.toUpperCase().match(vm.regular_filter.toUpperCase());
      });
    },
    ga1FD() {
      const vm = this;
      return vm.ga1.filter(function (item) {
        return item.toUpperCase().match(vm.ga1_filter.toUpperCase());
      });
    },
    ga2FD() {
      const vm = this;
      return vm.ga2.filter(function (item) {
        return item.toUpperCase().match(vm.ga2_filter.toUpperCase());
      });
    },
    ga3FD() {
      const vm = this;
      return vm.ga3.filter(function (item) {
        return item.toUpperCase().match(vm.ga3_filter.toUpperCase());
      });
    },
  },
  methods: {
    backpage() {
      this.$store.dispatch('actFilter',false);
    },
    sendFilter() {
      const vm = this;
      let cli = this.cli_send;
      let pro = this.pro_send;
      let pay = this.paymethod_send;
      let ord = this.ordertype_send;
      let reg = this.regular_send;
      let cam = this.campaign_send;
      let media = this.media_send;
      let link = this.link_type_send;
      let ga1 = this.ga1_send;
      let ga2 = this.ga2_send;
      let ga3 = this.ga3_send;

      if (cli.length == 0) {
        cli = "top1";
      } else {
        cli = vm.cli_send;
      }
      this.$store.dispatch("qhurikae/getFilter", {
        cli,
        pro,
        pay,
        ord,
        reg,
        cam,
        media,
        link,
        ga1,
        ga2,
        ga3,
      });
      this.$store.dispatch("qhurikae/getCros");
      this.$store.dispatch("qhurikae/getFb");
      this.$store.dispatch("qhurikae/getLine");
      this.$store.dispatch('qhurikae/getData');
      this.backpage();
    },
    sendFilter2() {
      let cli = this.cli_send;
      let pro = this.pro_send;
      let pay = this.paymethod_send;
      let ord = this.ordertype_send;
      let reg = this.regular_send;
      let cam = this.campaign_send;
      let media = this.media_send;
      let link = this.link_type_send;
      let ga1 = this.ga1_send;
      let ga2 = this.ga2_send;
      let ga3 = this.ga3_send;
      $("html,body").scrollTop(0);
      this.$store.dispatch("qhurikae/getFilter", {
        cli,
        pro,
        pay,
        ord,
        reg,
        cam,
        media,
        link,
        ga1,
        ga2,
        ga3,
      });
      this.$store.dispatch("qhurikae/getCros");
      this.$store.dispatch("qhurikae/getFb");
      this.$store.dispatch("qhurikae/getLine");
      this.$store.dispatch('qhurikae/getData');
      this.getFilter();
    },

    getFilter() {
      const vm = this;
      let cli = this.cli_send;
      let pro = this.pro_send;
      let pay = this.paymethod_send;
      let ord = this.ordertype_send;
      let reg = this.regular_send;
      let cam = this.campaign_send;
      let media = this.media_send;
      let link = this.link_type_send;
      let ga1 = this.ga1_send;
      let ga2 = this.ga2_send;
      let ga3 = this.ga3_send;
      let date1 = this.$store.state.dorento.date1;
      let date2 = this.$store.state.dorento.date2;
      //this.media = data.media;
      //this.link_type = data.link_type;
      // this.ga1 = data.ga1;
      // this.ga2 = data.ga2;
      // this.ga3 = data.ga3;
      if (this.nowstep == "one") {
        this.nowstep = "two";
      }
      else if (this.nowstep == "two") {
        this.nowstep = "ga";
      }
      let mode = "";
      if (this.$store.state.qhurikae.mode == "cros") {
        mode = "cros";
      }
      if (this.$store.state.qhurikae.mode == "fb") {
        mode = "fb";
      }
      if (this.$store.state.qhurikae.mode == "line") {
        mode = "line";
      }
      let api = `${process.env.APIPATH}/${process.env.DORENTO}`;
      this.$http.get(api).then((res) => {
        if (res) {
          if (res.data.length < 3) {
            alert("此區段沒有資料😢");
            if (this.nowstep == "two") {
              this.nowstep = "one";
              return;
            } else if (this.nowstep == "ga") {
              this.nowstep = "two";
              return;
            }
          }

          vm.media = res.data[0].media;
          vm.campaign = res.data[0].campaign;
          vm.link_type = res.data[0].link_type;
          vm.ga1 = res.data[0].ga1;
          vm.ga2 = res.data[0].ga2;
          vm.ga3 = res.data[0].ga3;
        } else {
          return;
        }
      });
    },
    clickFilter(value) {
       const vm = this;

      switch (value) {
        case "ind":
         vm.cli = [];
         vm.pro = [];
         for(let item in vm.data){
            if(vm.ind_send == 0){
              vm.cli = vm.cli_df;
              vm.pro = vm.pro_df;
            } else if(vm.ind_send.includes(vm.data[item].industrytype) == 1){
              vm.cli.push(vm.data[item].clientname);
              vm.pro.push(vm.data[item].productname);
            }
         }
          this.allSelected_ind = false;
          break;

        case "cli":
          vm.ind = [];
          vm.pro = [];
          for(let item in vm.data){
              if (vm.cli_send == 0) {
                vm.ind = vm.ind_df;
                vm.pro = vm.pro_df;
              } else if (vm.cli_send.includes(vm.data[item].clientname) == 1) {
                vm.ind.push(vm.data[item].industrytype);
                vm.pro.push(vm.data[item].productname);
              }

          }
          this.allSelected_cli = false;
          break;
        case "pro":
          vm.ind = [];
          vm.cli = [];
          for (let item in vm.data) {
            if (vm.pro_send == 0) {
              vm.ind = vm.ind_df;
              vm.cli = vm.cli_df;
            } else if (vm.pro_send.includes(vm.data[item].productname) == 1) {
              vm.ind.push(vm.data[item].industrytype);
              vm.cli.push(vm.data[item].clientname);
            }
          }
         
          this.allSelected_pro = false;
          break;
      }
    }, //clickFilter end  for  ind cli pro
    clickAll(value) {
      const vm = this;
      switch (value) {
        case "ind":
          vm.ind_send = [];
          if (vm.allSelected_ind) {
            vm.indFD.forEach(function (item) {
              vm.ind_send.push(item);
            });
          }
          vm.clickFilter("ind");
          break;
        case "cli":
          vm.cli_send = [];
          if (vm.allSelected_cli) {
            vm.cliFD.forEach(function (item) {
              vm.cli_send.push(item);
            });
          }
          vm.clickFilter("cli");
          break;
        case "pro":
          vm.pro_send = [];
          if (vm.allSelected_pro) {
            vm.proFD.forEach(function (item) {
              vm.pro_send.push(item);
            });
          }
          vm.clickFilter("pro");
          break;
        case "paymethod":
          vm.paymethod_send = [];

          if (vm.allSelected_paymethod) {
            vm.paymethodFD.forEach(function (item) {
              vm.paymethod_send.push(item.value);
            });
          }
          break;
        case "ordertype":
          vm.ordertype_send = [];
          if (vm.allSelected_ordertype) {
            vm.ordertypeFD.forEach(function (item) {
              vm.ordertype_send.push(item);
            });
          }
          break;
        case "regular":
          vm.regular_send = [];
          if (vm.allSelected_regular) {
            vm.regularFD.forEach(function (item) {
              vm.regular_send.push(item);
            });
          }
          break;
        case "campaign":
          vm.campaign_send = [];
          if (vm.allSelected_campaign) {
            vm.campaignFD.forEach(function (item) {
              vm.campaign_send.push(item);
            });
          }
          break;
        case "link_type":
          vm.line_type_send = [];
          if (vm.allSelected_link_type) {
            vm.link_type_FD.forEach(function (item) {
              vm.link_type_send.push(item);
            });
          }
          break;
        case "media":
          vm.media_send = [];
          if (vm.allSelected_media) {
            vm.mediaFD.forEach(function (item) {
              vm.media_send.push(item);
            });
          }
          break;
        case "ga1":
          vm.ga1_send = [];
          if (vm.allSelected_ga1) {
            vm.ga1FD.forEach(function (item) {
              vm.ga1_send.push(item);
            });
          }
          break;
        case "ga2":
          vm.ga2_send = [];
          if (vm.allSelected_ga2) {
            vm.ga2FD.forEach(function (item) {
              vm.ga2_send.push(item);
            });
          }
          break;
        case "ga3":
          vm.ga3_send = [];
          if (vm.allSelected_ga3) {
            vm.ga3FD.forEach(function (item) {
              vm.ga3_send.push(item);
            });
          }
          break;
      }
    }, // clickAll
    clickClear(value) {
      const vm = this;
      switch (value) {
        case "ind":
          vm.ind_send = [];
          vm.allSelected_ind = false;
          vm.clickFilter("ind");
          break;
        case "cli":
          vm.cli_send = [];
          vm.allSelected_cli = false;
          vm.clickFilter("cli");
          break;
        case "pro":
          vm.pro_send = [];
          vm.allSelected_pro = false;
          vm.clickFilter("pro");
          break;
        case "paymethod":
          vm.paymethod_send = [];
          vm.allSelected_paymethod = false;
          break;
        case "ordertype":
          vm.ordertype_send = [];
          vm.allSelected_ordertype = false;
          break;
        case "regular":
          vm.regular_send = [];
          vm.allSelected_regular = false;
          break;
        case "campaign":
          vm.campaign_send = [];
          vm.allSelected_campaign = false;
          break;
        case "media":
          vm.media_send = [];
          vm.allSelected_media = false;
          break;
        case "link_type":
          vm.link_type_send = [];
          vm.allSelected_link_type = false;
          break;
        case "ga1":
          vm.ga1_send = [];
          vm.allSelected_ga1 = false;
          break;
        case "ga2":
          vm.ga2_send = [];
          vm.allSelected_ga2 = false;
          break;
        case "ga3":
          vm.ga3_send = [];
          vm.allSelected_ga3 = false;
          break;
      }
    }, // clickClear
  },
  watch: {
    $route(){
      this.nowstep = "one";  
    }//前面只要切換葉面 就會回到第一頁
  },
  created() {
    const vm = this;

    $.ajax({
      type: "GET",
      url: `/static/json/data.json`, //本地端
      dataType: "json",
      success: function (response) {
        vm.data = response;
        const newind = vm.data.map((item) => item.industrytype);
        const newcli = vm.data.map((item) => item.clientname);
        const newpro = vm.data.map((item) => item.productname);
        vm.ind = newind.filter((item, key, arr) => arr.indexOf(item) == key);
        vm.cli = newcli.filter((item, key, arr) => arr.indexOf(item) == key);
        vm.pro = newpro.filter((item, key, arr) => arr.indexOf(item) == key);
        vm.ind_df = newind.filter((item, key, arr) => arr.indexOf(item) == key);
        vm.cli_df = newcli.filter((item, key, arr) => arr.indexOf(item) == key);
        vm.pro_df = newpro.filter((item, key, arr) => arr.indexOf(item) == key);
      },
    });
  },
};
</script>

