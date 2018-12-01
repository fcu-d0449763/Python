function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

$(document).ready(function(){

    $("#form-auth").submit(function(e){
        e.preventDefault();
        var id_card = $("#id-card").val();
        var id_name = $("#real-name").val();
        $.ajax({
            url:'/user/auth/',
            dataType:'json',
            type:'POST',
            data:{'id_card':id_card,'id_name':id_name},
            success:function(msg){
                if(msg.code=='200'){
                    location.href = '/user/my/'
                }

            },
            error:function(msg){
                alert('实名认证失败')
            }

        })


    });


})


$.get('/user/auth_person/', function(data){

    if(data.code == '200'){
        $('#real-name').attr('placeholder',data.data.id_name)
        $('#id-card').attr('placeholder',data.data.id_card)
        $('#real-name').attr('disabled','disabled')
        $('#id-card').attr('disabled','disabled')
        $('.btn-success').attr('type','hidden')

    }
});