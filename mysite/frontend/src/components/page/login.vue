<template lang="pug">  
  div.loginbox
    
    form.form-signin(@submit.prevent="signin" )
         
        label(v-show="logShow")
            h1.h3.mb-3.font-weight-normal  STA 可視化報表
            label.sr-only(for='inputEmail') Email address
            input#inputEmail.form-control( v-model="user.username" type='text' placeholder='Email address' required='' autofocus='')
            label.sr-only(for='inputPassword') Password
            input#inputPassword.form-control( v-model="user.password" type='password' placeholder='Password' required='')
            button.btn.btn-lg.btn-primary.btn-block(type='submit') Sign in
            p.mt-5.mb-3.text-muted &copy; 2020 可視化チーム
        lable.login-loading(v-show="login")    
            .spinner-border.spinner-border-sm  
              
            
</template>

<script>
import $ from  'jquery'
import axios from 'axios'

export default {
   data(){
        return{
            user:{
                'username':"",
                'password':""
            },
            login: false ,
            logShow: false
        }
    },
    methods:{
        signin(){
             const api = `http://192.168.111.43:8070/client/log_in`;  //`${process.env.APIPATH}/admin/signin`;//
             const vm =  this;
             vm.login = !vm.login;
             vm.logShow = false;
             var form = new FormData();
             form.append('username', vm.user.username);
             form.append('password', vm.user.password);
             //console.log(vm.user[0],vm.user[1]);
             let config = {
                headers: {'Content-Type': 'multipart/form-data'}
            }; //添加请求头
             this.$http.post('http://192.168.111.43:8070/client/log_in',form,config).then((res) => {
                console.log(res);
                if(res.data.success){
                    vm.login = !vm.login;
                    vm.$router.push('/');
                }else{
                    $("#cliModal").modal('show');
                    vm.login = !vm.login;
                    vm.logShow = true;
                    alert('帳密錯誤');
                }
              })   
       
              /*
              $.ajax({ 
                type: 'POST', 
                url: api, //本地端網址或者有開放的cros api 
				async: true, // 預設為true(非同步)  false 為同步
                dataType: 'json',
                data : vm.user,
                success: function (res) { 
                    vm.login = !vm.login;
                    vm.$router.push('/');
                },
                error:function(xhr){
                    alert("發生錯誤: " + xhr.status + " " + xhr.statusText);
                  }
            })  */
            
        } 
    },
    activated(){
         this.login = false ;
         this.logShow =true;
        
    },
}
</script>

