'''
10.这是经典的"百马百担"问题，
有一百匹马，驮一百担货，大马驮3担，中马驮2担，两只小马驮1担，
问有大，中，小马各几匹？
'''
big_horse = 3
middle_horse = 2
small_horse = 1/2
for i in range(33):
	for j in range(50):
		x = 100 - i -j
		if big_horse*i + middle_horse*j + small_horse*x==100:		
			print("大马有%d匹，中马有%d匹，小马有%d匹"%(i,j,x))			