var form;
layui.use(['form', 'laydate'], function(){
  form = layui.form;
  laydate = layui.laydate;
  laydate.render({
    elem: '#order_date'
  });

  //监听提交
  form.on('submit(orderAdd)', function(data){
    console.log(data.field)
    innerIndex = layer.load()
    $.post(
        "/commit_order/",
        data.field,
        function(data,status){
            layer.close(innerIndex)
            if( status == 'success' && data.code == 0){
                $("#addForm")[0].reset();
                layer.msg('需求登记成功.',{
                    time:2000,
                    icon: 6
                });
            }else{
                layer.alert(data.msg, {
                    title: '出错了', icon: 5
                })
            }
        }
    )
    return false;
  });
});

