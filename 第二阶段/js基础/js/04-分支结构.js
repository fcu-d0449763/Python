//js中的分支结构:if语句,switch语句
//1.if语句
/*结构:
 * a.if(条件语句)
 * {
 		代码段
 * }
 执行过程:先判断条件语句是否为true,为true就执行代码段
 *b.if-else结构:
 * if(条件语句){
 * 	代码段1
 * }
 * else{
 * 	代码段2
 * }
 * c.if else-if else:(这儿的else if 相当于python中的elif)
 * if(条件语句1){
 * 	代码段1
 * }
 * else if(条件语句2){
 	代码段2
 * 	
 * }
 * else{
 * 	代码段3
 * }
 * */
//判断一个数是否是偶数,如果是就打印'偶数'
var num = 11
if(num%2==0){
	console.log('偶数')
}
if(num%2==0){
	console.log('偶数')
}
else{
	console.log('是奇数')
}
//2.switch
/*
 *a.结构:
switch(表达式){
	case 值1:{
		代码段1
		break
	}
	case 值2:{
		代码段2
		break
	}
	...
	default:{
		break
	}
}
b.执行过程:先计算表达式的值,然后再用这个值去和后边case关键字后面的值一一对比,看是否相等.
	找到第一个和表达式的值相等的case,然后将这个case作为入门,依次执行后面的代码
	直到遇到break或者switch结束.如果没有找到和表达式的值相等的case就执行finally后面的代码
c.注意:default可有可无,case可以有若干个
 * */
var num1=100
switch(num1){
	case 100:
		console.log('A')
	case 10:
		console.log('B')
	case 'abc':
		console.log('C')
	default:
		console.log('D')
}
//练习:0-6,根据数字对应的值不一样,打印不同的结果:0--星期天,1--星期一
var week = 1
switch(week){
	case 0:{
		console.log('星期天')
		break
	}
	case 1:{
		console.log('星期一')
		break
	}
	case 2:{
		console.log('星期二')
		break
	}
	case 3:{
		console.log('星期三')
		break
	}
	case 4:{
		console.log('星期四')
		break
	}
	case 5:{
		console.log('星期五')
		break
	}
	case 6:{
		console.log('星期六')
		break
	}
}
//练习2:根据分数等级:1-5:不及格,6:及格,7,8:良好,9,10:优秀
var score = 2
switch(score){
	case 9 :{
		console.log('优秀')
		break
	}
	case 10:{
		console.log('优秀')
		break
	}
	case 7:{
		console.log('良好')
		break
	}
	case 8:{
		console.log('良好')
		break
	}
	case 6:{
		console.log('及格')
		break
	}
	default:{
		console.log('不及格')
	}
	
}
