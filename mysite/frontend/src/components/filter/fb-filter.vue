<template lang="pug">
.dropdown-filter.col-sm-12
  h4.wrapper_back.mt-3(@click="backpage") 
    i.fas.fa-arrow-left.close-filter
    span.ml-3.close-filter 閉じる
  .title-filter.mb-5
    h1 検索条件 FACEBOOK
  .container 
    .wrpapperbox-set
      .wrapperbox
        .all-label-box
          .row(v-show="nowstep == 'one'")
            .labelbox.col-3
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
            .labelbox.col-3
              .col-12
                h4 クライアント
                  i.fas.fa-eraser(@click="clickClear('cli')")
                input.search_box(placeholder="キーワード入力", v-model="cli_filter") 

                .label-wrapper 
                  label 
                    input(
                      type="checkbox",
                      @change="clickAll('cli')",
                      v-model="allSelected_cli"
                    )
                    | 全選
                  label(v-for="item in cliFD") 
                    input(
                      type="checkbox",
                      @change="clickFilter('cli')",
                      v-model="cli_send",
                      :value="item"
                    )
                    | {{ item }}
            .labelbox.col-3
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
          
            .labelbox.col-3
              .col-12
                h4 帳戶名
                  i.fas.fa-eraser(@click="clickClear('account')")
                input.search_box(placeholder="キーワード入力", v-model="account_filter") 
                .label-wrapper 
                  label 
                    input(
                      type="checkbox",
                      @change="clickAll('account')",
                      v-model="allSelected_account"
                    )
                    | 全選
                  label(v-for="item in accountFD") 
                    input(
                      type="checkbox",
                      @change="clickFilter('account')",
                      v-model="account_send",
                      :value="item"
                    )
                    | {{ item }}  
          .row(v-show="nowstep == 'two'")
            .labelbox
              h4 群組類型
                i.fas.fa-eraser(@click="clickClear('group_type')")
              input.search_box(
                placeholder="キーワード入力",
                v-model="group_type_filter"
              ) 
              .label-wrapper 
                label 
                  input(
                    type="checkbox",
                    @change="clickAll('group_type')",
                    v-model="allSelected_group_type"
                  )
                  | 全選
                label(v-for="item in group_typeFD") 
                  input(
                    type="checkbox",
                    v-model="group_type_send",
                    :value="item"
                  )
                  | {{ item }}
            .labelbox
              h4 行銷活動名稱 
                i.fas.fa-eraser(@click="clickClear('campaign_name')")
              input.search_box(
                placeholder="キーワード入力",
                v-model="campaign_name_filter"
              ) 

              .label-wrapper 
                label 
                  input(
                    type="checkbox",
                    @change="clickAll('campaign_name')",
                    v-model="allSelected_campaign_name"
                  )
                  | 全選
                label(v-for="item in campaign_nameFD") 
                  input(
                    type="checkbox",
                    v-model="campaign_name_send",
                    :value="item"
                  )
                  | {{ item }}
            .labelbox
              h4 廣告組合名稱
                i.fas.fa-eraser(@click="clickClear('ad_set_name')")
              input.search_box(placeholder="キーワード入力", v-model="ad_set_name_filter") 

              .label-wrapper 
                label 
                  input(
                    type="checkbox",
                    @change="clickAll('ad_set_name')",
                    v-model="allSelected_ad_set_name"
                  )
                  | 全選
                label(v-for="item in ad_set_nameFD") 
                  input(type="checkbox", v-model="ad_set_name_send", :value="item")
                  | {{ item }}
          .row(v-show="nowstep == 'two'") 
            .labelbox
              h4 廣告名稱
                i.fas.fa-eraser(@click="clickClear('ad_name')") 
              input.search_box(
                placeholder="キーワード入力",
                v-model="ad_name_filter"
              ) 
              .spinner-border.spinner-border-sm.chart_loading(v-if="isLoading")
              .label-wrapper 
                label 
                  input(
                    type="checkbox",
                    @change="clickAll('ad_name')",
                    v-model="allSelected_ad_name"
                  )
                  | 全選
                label(v-for="item in ad_nameFD") 
                  input(
                    type="checkbox",
                    v-model="ad_name_send",
                    :value="item"
                  )
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
              input.search_box(placeholder="キーワード入力" v-model="ga1_filter") 
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
              input.search_box(placeholder="キーワード入力", v-model="ga2_filter") 
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
                i.fas.fa-eraser(@click="clickClear('ga3')" v-model="ga3_filter")
              input.search_box(placeholder="キーワード入力", v-model="ga3_send") 
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
      cli_send: [],
      pro_send: [],
      account_send:[],
      group_type_send: [],
      campaign_name_send: [],
      ad_set_name_send: [],
      ad_name_send: [],
      link_type_send: [],
      ga1_send: [],
      ga2_send: [],
      ga3_send: [],

      data: [],
      ind: [],
      cli: [],
      pro: [],
      account:[],

      group_type: [],
      campaign_name: [],
      ad_set_name: [], 
      ad_name: [], 
      link_type: [], //リンク別
      ga1: [],
      ga2: [],
      ga3: [],
      ind_df: [],
      cli_df: [],
      pro_df: [],
      account_df:[],

      ind_filter: "",
      cli_filter: "",
      pro_filter: "",
      account_filter:"",
      group_type_filter: "",
      link_type_filter: "",
      campaign_name_filter: "",
      ad_set_name_filter: "",
      ad_name_filter: "",
      ga1_filter: "",
      ga2_filter: "",
      ga3_filter: "",
      allSelected_ind: false,
      allSelected_cli: false,
      allSelected_pro: false,
      allSelected_account: false,
      allSelected_group_type: false,
      allSelected_campaign_name: false,
      allSelected_ad_set_name: false,
      allSelected_ad_name: false,
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
        return this.$store.state.fb.isLoading_FB;
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
    
      let cli = this.cli_send;
      let pro = this.pro_send;
      let account = this.account_send ; // new  
      let group = this.group_type_send;
      let cn = this.campaign_name_send;
      let adset = this.ad_set_name_send;
      let adn = this.ad_name_send;
      let link = this.link_type_send; 
      let ga1 = this.ga1_send;
      let ga2 = this.ga2_send;
      let ga3 = this.ga3_send;
     
      if (cli.length == 0) {
        cli = "top1";
      } else {
        cli = this.cli_send;
      }
      /*this.$store.dispatch("fb/getFilter", {
        cli,
        pro,
        account,
        group,
        cn,
        ads,
        adn,
        link,
        ga1,
        ga2,
        ga3,
      });

      this.$store.dispatch('fb/getFb');
      this.$store.dispatch('fb/getData');
      */
      this.backpage();
    },
    sendFilter2() {
      let cli = this.cli_send;
      let pro = this.pro_send;
      let account = this.account_send ; // new  
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

      this.getFilter();
      /*
      this.$store.dispatch("fb/getFilter", {
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
        this.$store.dispatch('fb/getFb');
        this.$store.dispatch('fb/getData');
      
      
      */
    },

    getFilter() {
      const vm = this;
      let cli = this.cli_send;
      let pro = this.pro_send;
      let account = this.account_send ; // new  
      let pay = this.paymethod_send;
      let ord = this.ordertype_send;
      let reg = this.regular_send;
      let cam = this.campaign_send;
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
      return ;
      let api = `${process.env.APIPATH}/${process.env.FACEBOOK}`;
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
        case "account":
          vm.account_send = [];
          if (vm.allSelected_account) {
            vm.accountFD.forEach(function (item) {
              vm.account_send.push(item);
            });
          }
         // vm.clickFilter("account");
          break;  
        case "group_type":
          vm.group_type_send = [];

          if (vm.allSelected_group_type) {
            vm.group_typeFD.forEach(function (item) {
              vm.group_type_send.push(item.value);
            });
          }
          break;
        case "campaign_name":
          vm.campaign_name_send = [];
          if (vm.allSelected_campaign_name) {
            vm.campaign_nameFD.forEach(function (item) {
              vm.campaign_name_send.push(item);
            });
          }
          break;
        case "ad_set_name":
          vm.ad_set_name_send = [];
          if (vm.allSelected_ad_set_name) {
            vm.ad_set_nameFD.forEach(function (item) {
              vm.ad_set_name_send.push(item);
            });
          }
          break;
        case "ad_name":
          vm.ad_name_send = [];
          if (vm.allSelected_ad_name) {
            vm.ad_nameFD.forEach(function (item) {
              vm.ad_name_send.push(item);
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
        case "account":
          vm.account_send = [];
          vm.allSelected_account = false;
          vm.clickFilter("account");
          break;  
        case "group_type":
          vm.group_type_send = [];
          vm.allSelected_group_type = false;
          break;
        case "campaign_name":
          vm.campaign_name_send = [];
          vm.allSelected_campaign_name = false;
          break;
        case "ad_set_name":
          vm.ad_set_name_send = [];
          vm.allSelected_ad_set_name = false;
          break;
        case "ad_name":
          vm.ad_name_send = [];
          vm.allSelected_ad_name = false;
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

