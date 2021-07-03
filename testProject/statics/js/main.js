$(function(){
    $(".innerLink").click(function(){
        console.log($(this).attr('action'))
        console.log($(this).text())
        $("#mainframe").attr("src", $(this).attr('action'))
        $("#pageName").text($(this).text())
    });
})