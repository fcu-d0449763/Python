a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
c = a - b
print(c)
d = b - a
print(d)
e = {x for x in 'abracadabra' if x not in 'abc'}
print(e)

# f = set([1,7,8,5,6,4,9,8,2])
# for i in range(len(f)):
# 	print(f[i])
# 集合不支持下标