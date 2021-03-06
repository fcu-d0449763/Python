﻿$(document).ready(function(){
    $(".auth-warn").show();
})

$.get('/user/auth_person/', function(data){

    if(data.code == '200'){
//
//        $('.btn-success').hide()
//        $('.house-title h3').hide()

        $('.houses-list').show();
        $('.auth-warn').hide();

    }
    if(data.code == '100'){
        $('.houses-list').hide();
        $('.auth-warn').show();


    }
});
$.get('/house/myhouses/', function(msg){
    if(msg.code == '200'){
        var house_html = ''
        for(var i=0;i<msg.houses.length; i++){
            house_li = ''
            house_li +='<li>'
            house_li +='<a href="/house/detail/?house_id=' + msg.houses[i].id +'">'
            house_li +='<div class="house-title">'
            house_li +='<h3>房屋ID:' + msg.houses[i].id + ' —— ' + msg.houses[i].title + '</h3>'
            house_li +='</div>'
            house_li +='<div class="house-content">'
            house_li +='<img src="/static/' + msg.houses[i].image + '" alt="">'
            house_li +='<div class="house-text">'
            house_li +='<ul>'
            house_li +='<li>位于：' + msg.houses[i].area + '</li>'
            house_li +='<li>价格：￥' + msg.houses[i].price + '/晚</li>'
            house_li +='<li>发布时间：' + msg.houses[i].create_time +'</li>'
            house_li +='</ul>'
            house_li +='</div>'
            house_li +='</div>'
            house_li +='</a>'
            house_li +='</li>'

            house_html += house_li
        }
        $('#houses-list').append(house_html)
    };
});