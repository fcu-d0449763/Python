function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}



$(document).ready(function(){
    $("#form-name").submit(function(e){
        e.preventDefault();
        name = $("#user-name").val();
        $.ajax({
            url:'/user/profile/',
            dataType:'json',
            type:'POST',
            data:{'name':name},
            success:function(msg){
                if(msg.code=='200'){
                    location.href = '/user/my/'
                }

            },
            error:function(msg){

                alert('–ﬁ∏ƒ ß∞‹')
            }



        })

    });


    $('#form-avatar').submit(function(){
        $(this).ajaxSubmit({
            url:'/user/profile/',
            type:'PATCH',
            dataType:'json',
            success:function(msg){
                $('#user-avatar').attr('src', '/static/' + msg.image_url)
            },
            error: function(msg){
                alert('«Î«Û ß∞‹')
            }
        })
        return false;
    });


})
