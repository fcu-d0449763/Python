# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-08 09:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_nums', models.IntegerField(default=0, verbose_name='数量')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品')),
            ],
            options={
                'db_table': 'f_order_goods',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_sn', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='订单号')),
                ('trade_no', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='交易号')),
                ('pay_status', models.CharField(choices=[('paying', '待支付'), ('WAIT_BUYER_PAY', '交易创建'), ('TRADE_FINISHED', '交易结束'), ('TRADE_CLOSE', '交易关闭'), ('TRADE_SUCCESS', '成功')], default='PAYING', max_length=20, verbose_name='交易状态')),
                ('post_script', models.CharField(max_length=200, verbose_name='订单留言')),
                ('order_mount', models.FloatField(default=0.0, verbose_name='订单金额')),
                ('pay_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='支付时间')),
                ('address', models.CharField(default='', max_length=200, verbose_name='收货地址')),
                ('signer_name', models.CharField(default='', max_length=20, verbose_name='收货人')),
                ('signer_mobile', models.CharField(max_length=11, verbose_name='联系电话')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='用户')),
            ],
            options={
                'db_table': 'f_order',
            },
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='order.OrderInfo', verbose_name='订单详情'),
        ),
    ]