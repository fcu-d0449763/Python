//1.函数的声明
/*
function 函数名(参数列表){
	函数体
}
说明:
a.function:是js中声明函数的关键字
b.函数名:标识符,不能是关键字;见名知义,驼峰式命名
c.参数列表:参数名1,参数名2...;形参:将数据从函数的外面传到函数中
d.函数体:实现函数的功能

注意:函数体只有在函数调用的时候才执行

*/
function sum(num1,num2){
	console.log(num1+num2)
}
function sum2(num1,num2=10){
	console.log(num1+num2)
}


//函数调用:和python一样
//函数调用的时候要保证每个参数都有值!
//支持位置参数,关键字参数,参数设置默认值(js6)
//注意:js中不支持不定长参数
sum(1,2)
sum(num2=10,num1=20 )
sum2(23)

//3.函数的返回值
//js中如果没有遇到return,函数的返回值是undefined
//注意:js中不能同时返回多个值
function func1(){
	console.log('func1')
	return 100,'abc'
}
console.log(func1())

//4.js中,函数也可以作为变量
var na = func1
na()


//5.另外一种声明函数的方式
/*
var 变量 =function(参数列表){
	函数体
}
*/
var func2 = function(num){
	console.log('这是一个函数类型的数据',num)
}
func2(23)

 var foucs = [
	function(){
		console.log('aaa')
	},100
]
foucs[0]()
