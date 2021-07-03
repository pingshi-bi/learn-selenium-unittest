layui.use(['table', 'form', 'laydate'], function(){
  var table = layui.table;
  var form = layui.form;
  laydate = layui.laydate;
  laydate.render({
    elem: '#order_date'
  });
  form.on('submit(orderList)', function(data){
    return false
  });

  table.render({
    elem: '#orderList'
    ,url:'/list_order/?data=json'
    ,where: {}
//    ,toolbar: '#toolbar' //开启头部工具栏，并为其绑定左侧模板
    ,defaultToolbar: ['exports', 'print']
    ,title: '需求信息表'
//    ,height: 'full-100'
    ,cellMinWidth: 80 //全局定义常规单元格的最小宽度，layui 2.2.1 新增
    ,cols: [[
      {field:'id', width:80, title: 'ID', sort: true}
      ,{field:'name', width:250, title: '需求名称'}
      ,{field:'dep', width:150, title: '需求部门'}
      ,{field:'type', width:120, title: '需求类型'}
      ,{field:'date', width:120, title: '需求日期'}
      ,{field:'desc', title: '需求描述'}
      ,{fixed:'right', title:'操作', toolbar: '#inlinebar', width: 120}
    ]]
    ,page:true
  });

  //监听行工具事件
  table.on('tool(orderList)', function(obj){
    var data = obj.data;
    if(obj.event === 'look'){
        oid = obj.data.id
        layer.open({
          type: 2,
          title: '需求详情',
          maxmin: false, //开启最大化最小化按钮
          area: ['80%', '80%'],
          content: '/info_order/?oid='+oid
        });
    }
  });

  function tableReload(){
    table.reload('orderList', {
      where: { //设定异步数据接口的额外参数，任意设
        order_name: $("#order_name").val()
        ,order_dep: $("#order_dep").val()
        ,order_type: $("#order_type").val()
        ,order_date: $("#order_date").val()
      }
      ,page: {
        curr: 1 //重新从第 1 页开始
      }
    });
    $("#listform")[0].reset();
  }

  $("#search").click(function(){
    tableReload();
  })
});