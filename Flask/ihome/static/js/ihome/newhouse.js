function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

//$(document).ready(function(){
//    // $('.popup_con').fadeIn('fast');
//    // $('.popup_con').fadeOut('fast');
//})

$.get('/house/area_facility/',function(msg){
    if(msg.code=='200'){
        var area_str = ''
        var facility_str = ''
        for(var i=0;i<msg.areas.length;i++){
            area_option = '<option value=' + msg.areas[i].id + '>' + msg.areas[i].name + '</option>'
            area_str += area_option
        }
        $('#area-id').html(area_str)
        for(var j=0;j<msg.facilitys.length;j++){
            facility_li = '<li><div class="check"><label>'
            facility_li += '<input type="checkbox" name="facility" value="' + msg.facilitys[j].id + '">' + msg.facilitys[j].name
            facility_li += '</label></div></li>'
            facility_str += facility_li

        }
        $('.house-facility-list').html(facility_str)


    }


});

$(document).ready(function(){
    $('#form-house-info').submit(function(e){
        e.preventDefault();
        $(this).ajaxSubmit({
            url:'/house/newhouse/',
            type:'POST',
            dataType:'json',
            success:function(data){
                if(data.code == '200'){
                    $('#form-house-image').show()
                    $('#form-house-info').hide()
                    $('#house-id').val(data.house_id)
                }
            },
            error:function(data){
                alert(' ß∞‹')
            }
        });
    });

    $('#form-house-image').submit(function(e){
        e.preventDefault()
        $(this).ajaxSubmit({
            url:'/house/house_images/',
            dataType:'json',
            type:'POST',
            success:function(data){
                if(data.code == '200'){
                    var img_src = '<img src="/static/' + data.image_url + '">'
                    $('.house-image-cons').append(img_src)
                }
            },
            error:function(data){
                alert('«Î«Û ß∞‹')
            }
        })
    });


});