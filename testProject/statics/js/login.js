$(function(){
  layui.use('form', function(){});
  $("#loginButton").click(function(){
      var userName = $("#LAY-user-login-username").val();
      var password = $("#LAY-user-login-password").val();
      var randCode = $("#LAY-user-login-vercode").val();
      if( !userName || !password ){
          layer.msg("请输入用户名和密码", {icon: 5});
          return false;
      }
      if( !randCode ){
          layer.msg("请输入验证码", {icon: 5});
          return false;
      }

      innerIndex = layer.load()
      $.post(
        "/dologin/", {
            "username": userName,
            "pwd": password,
            "randomCode": randCode
        }, function(data,status){
            layer.close(innerIndex)
            if( status == 'success' && data.code == 0){
                window.location = "/mainpage/"
            }else{
                layer.alert(data.msg, {
                    title: '出错了', icon: 5
                })
            }
        }
    )
  });
});