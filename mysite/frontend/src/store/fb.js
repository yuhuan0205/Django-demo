import axios from 'axios'  //主要的ajax套件


export default {
    namespaced: true,
    state:{
        isLoading_FB: false ,
        isLoading_filter: false,
        type_index: 'cli' ,
        data:[],   // fb的資料包
        cli : ['top1'],  // 篩選參數 客戶別
        pro : [], // 篩選參數
        account: [],
        group : [], // 篩選參數
        cn : [], // 篩選參數
        ads : [], // 篩選參數
        adn : [], // 篩選參數
        link: [], // 篩選參數
        ga1: [], // 篩選參數
        ga2: [], // 篩選參數
        ga3: [], // 篩選參數
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
        getTime(context,{date1,date2}){  //改變時間
            context.commit('sendDate',{date1,date2});
        },
        getFilter(context,{cli,pro,account,group,cn,ads,adn,link,ga1,ga2,ga3}){  //篩選改變   
            context.commit('sendFilter',{cli,pro,account,group,cn,ads,adn,link,ga1,ga2,ga3});  
        }, 
        getData(context){  //獲取下載api 
            let date1 = context.state.date1;
            let date2 = context.state.date2;     
            let cli = context.state.cli;
            let pro = context.state.pro;
            let account = context.state.account;
            let group = context.state.group;
            let cn = context.state.cn;
            let ads = context.state.ads;
            let adn = context.state.adn;
            let link = context.state.link;
            let ga1 = context.state.ga1;
            let ga2 = context.state.ga2;
            let ga3 = context.state.ga3;
            context.commit('sendDownApi',{date1,date2,cli,pro,account,group,cn,ads,adn,link,ga1,ga2,ga3});
        }, 
        getFb(context){   // fb 的api 
     
            context.commit('isLoading',true);
            let date1 = context.state.date1;
            let date2 = context.state.date2;     
            let cli = context.state.cli;
            let pro = context.state.pro;
            let account = context.state.account;
            let group = context.state.group;
            let cn = context.state.cn;
            let ads = context.state.ads;
            let adn = context.state.adn;
            let link = context.state.link;
            let ga1 = context.state.ga1;
            let ga2 = context.state.ga2;
            let ga3 = context.state.ga3;
            let api = `${process.env.APIPATH}/${process.env.FACEBOOK}`;
           
            $("*").css("cursor",`url('/static/images/wait.ico') ,auto`);
            axios.get(api).then((res) => {
                if(res){ 
                    let fb = res.data
                    context.commit('sendFb',fb);
                    context.commit('isLoading',false);
                    $("*").css("cursor",`url('/static/images/move.ico') ,auto`);
                }else{
                    return 
                }

           })
        },// fb end

    }, //act end 
    mutations:{
        sendFb(state,fb){
            state.data = fb; 
        },
        isLoading(state,status){
            state.isLoading_FB = status;
        },
        sendFilter(state,{cli,pro,account,group,cn,ads,adn,link,ga1,ga2,ga3}){
            state.cli = cli;
            state.pro = pro;
            state.account = account;
            state.group = group;
            state.cn = cn;
            state.ads = ads;
            state.adn = adn;
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
        sendDownApi(state,{date1,date2,cli,pro,account,group,cn,ads,adn,link,ga1,ga2,ga3}){
            state.download_api = `${process.env.APIPATH}/${process.env.FACEBOOK_DOWNLOAD}`;
        }, 
    }


    
}