function hrefBack() {
    history.go(-1);
}

function decodeQuery(){
    var search = decodeURI(document.location.search);
    return search.replace(/(^\?)/, '').split('&').reduce(function(result, item){
        values = item.split('=');
        result[values[0]] = values[1];
        return result;
    }, {});
}

$(document).ready(function(){
    var mySwiper = new Swiper ('.swiper-container', {
        loop: true,
        autoplay: 2000,
        autoplayDisableOnInteraction: false,
        pagination: '.swiper-pagination',
        paginationType: 'fraction'
    })
    $(".book-house").show();

    var info = location.search
    house_id = info.split('=')[1]
    $.get('/house/detail/' + house_id + '/', function(msg){

        // 轮播图
        var slide_str = ''
        for(var j=0;j<msg.house_info.images.length;j++){
            images_li = '<li class="swiper-slide">'
            images_li += '<img src="/static/' + msg.house_info.images[j] +'"></li>'
            slide_str += images_li
        }
        $('.swiper-wrapper').html(slide_str)

        $('.house-price span').text(msg.house_info.price)
        //房子标题
        $('.house-title').text(msg.house_info.title)
//        $('.landlord-pic img').attr('src',''/static/'+msg.house_info.user_avatar')
        $('.landlord-name').text(msg.house_info.user_name)
        $('.text-center li').text(msg.house_info.address)
        $('.house_room').text('出租'+msg.house_info.room_count+'间')
        $('.house_acreage').text('房屋面积:'+msg.house_info.acreage+'平米')
        $('.house_unit').text('房屋户型:'+msg.house_info.unit)
        $('.house_capacity').text('宜住'+msg.house_info.capacity+'人')
        //床位
        $('.house_beds').text(msg.house_info.beds)

        //押金
        $('.house_deposit').text(msg.house_info.deposit)
        //最少天数
        $('.house_min_days').text(msg.house_info.min_days)
        //最大天数
        if(msg.house_info.max_days==0){
            $('.house_max_days').text('无限制')
        }else{
            $('.house_max_days').text(msg.house_info.max_days)
        }

//      设施
        var facility_str = ''
        for(var i=0;i<msg.house_info.facilities.length;i++){
            facility_li = '<li><span class="' + msg.house_info.facilities[i]['css']  + '">'
            facility_li += '</span>' + msg.house_info.facilities[i]['name'] +'</li>'
            facility_str += facility_li
        }
        $('.house-facility-list').html(facility_str)


        $('.book-house').attr('href', '/house/booking/?house_id=' + msg.house_info.id)
    });


})

