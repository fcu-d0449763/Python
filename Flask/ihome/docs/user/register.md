# 请求参数
mobile str  
password str

# 响应
成功响应  
{'code':200,'msg':'请求成功'}

失败响应  
{'code':1001,'msg':'参数不完整'}  
{'code':1002,'msg':'手机号不正确'}  
{'code':1003,'msg':'两次密码不一致'}  
{'code':1004,'msg':'该手机号已注册'}  
{'code':500,'msg':'注册失败'}  

# 响应参数  
name str 账号  
password str 密码