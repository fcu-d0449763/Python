'''
12.小明单位发了100元的购物卡，小明到超市买三类洗化用品，
洗发水（15元），香皂（2元），牙刷（5元）。
要把100元整好花掉，可如有哪些购买结合？
'''
hair_water = 15
soap = 2
tooth_brush = 5
for i in range(7):
	for j in range(50):
		for x in range(20):
			if hair_water*i + soap*j + tooth_brush *x ==100:
				print("可以买洗发水%d瓶，香皂%d块，牙刷%d只"%(i,j,x))
