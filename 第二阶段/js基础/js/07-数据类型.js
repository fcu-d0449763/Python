//new 类型名(值) --->可以将其他的类型的数据转换成相应类型的值()
//1.数字类型(Number):所有的数字对应的类型
//不能转换的结果是NaN
console.log(typeof(10))
var num1 = 100
var num2 = new Number('12')
console.log(num2+100,num1)

//2.布尔:true和false
//数字->布尔 NaN和0是false
//总结:所有为0为空的转换成布尔是false
var bool =  new Boolean(NaN)
console.log(bool)

//3.字符串(String):Unicode编码
//a.获取单个字符:通过字符串[下标]
//b.注意:
//		js中的下标支持0到长度-1,不支持负值
//		js中不支持切片
var str1='abcde'
console.log(str1[1])

//c.长度:字符串.length
console.log(str1.length)

//d.运算符:比较和+ 
//比较和python一样
//+:如果是其他的数据类型和字符串相加,都是先将其他数据类型转换成字符串,然后做字符串拼接操作
console.log('abc'+'123')  //abc123

console.log(123+'abc') //123abc

//e.其他的方法(自己查)
//String对象方法:字符串.方法()

//4.数组(相当于python中的列表)
//a.有序,可变的,元素的类型可以是任意类型的数据
var array = [1,'abc',true,[1,2,3]]

//查
console.log(array[1])

//增
array.push('aa')
console.log(array)

//删除
//pop():删除最后一个元素
array.pop()
console.log(array)
//shift():删除第一个元素
array.shift()
console.log(array)

//splice(删除的开始下标,删除的元素的个数)
var array = [1,'abc',true,[1,2,3]]
array.splice(1,1)
console.log(array)
//splice(被删除的下标/添加的开始下标,添加个数,被添加的元素列表)
var array = [1,'abc',true,[1,2,3]]
array.splice(0,2,'aa','bb')
console.log(array)

//改
var array = [1,'abc',true,[1,2,3]]
array[0]=100
console.log(array)
