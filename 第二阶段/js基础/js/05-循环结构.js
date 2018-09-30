//js中的循环结构分为:for循环和while循环
//1.for-in循环:(和python的for循环一样)
/*
 for var 变量 in 序列{
 	循环体
 }
 执行过程:依次从序列中取元素对应的索引,取完为止,每取一次执行依次循环体
 */
//变量字符串,取得是字符对应的下标
var str = 'abcd'
for (var i in str){
	console.log(str[i])
	
}

//遍历对象,取得是属性名(key)
for(var x in{a:'abc',name:'小明'}){
	console.log(x)
}
//2.for循环:(和C语言的for循环一样)
/*
for(表达式1;表达式2;表达式3){
	循环体
}
执行过程:先执行表达式1,然后再判断表达式2的结果是否为true,就执行循环体,执行完循环体再执行表达式3
然后再判断表达式2的结果是否为true,如果为true,又执行循环体,执行完循环体再执行循环体3,依次循环,直到表达式2的结果是false为止

*/
//计算1加到100
for(var i=1,sum = 0;i<=100;i++){
	sum +=i
}
console.log(sum)

//3.while循环:(和python一样)
/*
while(条件语句){
	循环体
}
 */

var sum = 0
var i = 1
while(i<=100){
	sum += i
	i+=1
}
console.log(sum)
//4.do-while:
/*
do{
	循环体	
}while(条件语句)

执行:先执行一次循环体,然后再判断条件语句是否为true,为true又执行循环体,依次类推,直到条件语句为false,循环就结束

*/
var sum = 0
var i = 1
do{
	sum +=i
	i++
}while(i<=100)
console.log(sum)

