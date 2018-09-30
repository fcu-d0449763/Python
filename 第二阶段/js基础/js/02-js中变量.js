//1.js中变量的声明
/*语法:var 变量名 或者var 变量名=初值
 * 说明:
 * a.var:是js中声明变量的关键字
 * b.变量名;标识符,不能是js中的关键字,驼峰式命名(第一个单词首字母小写,后面每个单词首字母大写),见名知义
 * c.初值:声明的时候可以赋初值,也可以不赋
 * 
 */
var age
var age = 10
console.log(age)

var studentCount = 100

//a.同时声明多个变量
var age; var name
var age1,name,studyId
var age = 10,name2

//b.一个变量可以存储多种类型的值
var name = '张三' 
name = 100 
console.log(name)
