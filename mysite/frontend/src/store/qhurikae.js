import axios from 'axios'  //主要的ajax套件



export default {
    namespaced: true,
	state:{
        isLoading_cros: false, //cros頁面的loading 
        isLoading_fb: false, //fb頁面的loading 
        isLoading_line: false, //linee頁面的loading 
        isLoading_filter: false,
        cros: [],  // cros 的資料包
        fb:[],   // fb的資料包
        line:[], // line的資料包
        cli : [],  // 篩選參數 客戶別
        pro : [], // 篩選參數
        pay : [], // 篩選參數
        ord : [], // 篩選參數
        reg : [], // 篩選參數
        cam : [], // 篩選參數
        media: [], // 篩選參數
        link: [], // 篩選參數
        ga1: [], // 篩選參數
        ga2: [], // 篩選參數
        ga3: [], // 篩選參數
        mode: "", // 篩選參數 與當前頁面
        date1 : "", // 篩選參數 時間別
        date2 : "",  // 篩選參數 時間別
        dateType: '', // 判定年月日
        send: 0, //送出
        download_api: "", //下載的參數
    },
    actions:{
        timeType(context,type){  //時間型態
            context.commit('sendDateType',type);
        },
        getMode(context,mode){  //偵測當前頁面
            context.commit('sendMode',mode);
        },
        getTime(context,{date1,date2}){  //改變時間
         
            context.commit('sendDate',{date1,date2});
        },
        getFilter(context,{cli,pro,pay,ord,reg,cam,media,link,ga1,ga2,ga3}){  //篩選改變
            context.commit('sendFilter',{cli,pro,pay,ord,reg,cam,media,link,ga1,ga2,ga3});  
        }, 
        getData(context){  //獲取下載api 
            let mode = context.state.mode;
            let date1 = context.state.date1;
            let date2 = context.state.date2;     
            let cli = context.state.cli;
            let pro = context.state.pro;
            let pay = context.state.pay;
            let ord = context.state.ord;
            let reg = context.state.reg;
            let cam = context.state.cam;
            let media = context.state.media;
            let link = context.state.link;
            let ga1 = context.state.ga1;
            let ga2 = context.state.ga2;
            let ga3 = context.state.ga3;
            context.commit('sendDownApi',{mode,date1,date2,cli,pro,pay,ord,reg,cam,media,link,ga1,ga2,ga3});

        }, 
       
        getLine(context){  // line的api 
            context.commit('sendLoading_line',true);
            let date1 = context.state.date1;
            let date2 = context.state.date2;     
            let cli = context.state.cli;
            let pro = context.state.pro;
            let pay = context.state.pay;
            let ord = context.state.ord;
            let reg = context.state.reg;
            let cam = context.state.cam;
            let media = context.state.media;
            let link = context.state.link;
            let ga1 = context.state.ga1;
            let ga2 = context.state.ga2;
            let ga3 = context.state.ga3;
            let mode = 'line';
            let api = `${process.env.APIPATH}/${process.env.DORENTO}`;
            console.log(date1,date2);
            axios.get(api).then((res) => {
                if(res){
                  let line = res.data
                  
                  context.commit('sendLine',line);
                  context.commit('sendLoading_line',false);
                  
                }else{
                    return 
                }

           })
        },// line end
        getFb(context){   // fb 的api 
            context.commit('sendLoading_fb',true);
            let date1 = context.state.date1;
            let date2 = context.state.date2;     
            let cli = context.state.cli;
            let pro = context.state.pro;
            let pay = context.state.pay;
            let ord = context.state.ord;
            let reg = context.state.reg;
            let cam = context.state.cam;
            let media = context.state.media;
            let link = context.state.link;
            let ga1 = context.state.ga1;
            let ga2 = context.state.ga2;
            let ga3 = context.state.ga3;
            let mode = 'fb';
            let api = `${process.env.APIPATH}/${process.env.DORENTO}`;
            axios.get(api).then((res) => {
                if(res){
                    let fb = res.data
                    context.commit('sendFb',fb);
                    context.commit('sendLoading_fb',false);
                  
                }else{
                    return 
                }

           })
        },// line end
        getCros(context){ // cros 的 api 
            context.commit('sendLoading_cros',true);
            let date1 = context.state.date1;
            let date2 = context.state.date2;     
            let cli = context.state.cli;
            let pro = context.state.pro;
            let pay = context.state.pay;
            let ord = context.state.ord;
            let reg = context.state.reg;
            let cam = context.state.cam;
            let media = context.state.media;
            let link = context.state.link;
            let ga1 = context.state.ga1;
            let ga2 = context.state.ga2;
            let ga3 = context.state.ga3;
            let mode = 'cros';
            let api = `${process.env.APIPATH}/${process.env.DORENTO}`;
            axios.get(api).then((res) => {
                if(res){
                  let cros = res.data;
                  context.commit('sendCros',cros);
                  context.commit('sendLoading_cros',false);
                  
                }else{
                    return 
                }

           })
         } // cros end  
       
       
     
       
    },// ACT END 
    mutations:{
        sendLoading_cros(state,status){ 
            state.isLoading_cros = status;
        },
        sendLoading_fb(state,status){
            state.isLoading_fb = status;
        },
        sendLoading_line(state,status){
            state.isLoading_line = status;
        },
        sendMode(state,mode){
            state.mode = mode;
        },
        sendFilter(state,{cli,pro,pay,ord,reg,cam,media,link,ga1,ga2,ga3}){
             state.cli = cli;
             state.pro = pro;
             state.pay = pay;
             state.ord = ord;
             state.reg = reg;
             state.cam = cam;
             state.media = media;
             state.link = link;
             state.ga1 = ga1;
             state.ga2 = ga2;
             state.ga3 = ga3;  
        },
        sendDate(state,{date1,date2}){
            state.date1 = date1;
            state.date2 = date2;
        },
        sendDateType(state,type){
            state.dateType = type;
        },
        sendCros(state,cros){
            state.cros = cros;   
        },
       
        sendFb(state,fb){
            state.fb = fb; 
        },
        sendLine(state,line){
            state.line = line;
        },
        sendDownApi(state,{mode,date1,date2,cli,pro,pay,ord,reg,cam,media,link,ga1,ga2,ga3}){
            state.download_api = `${process.env.APIPATH}/${process.env.DORENTO_DOWNLOAD}`;
        },
    }     

}