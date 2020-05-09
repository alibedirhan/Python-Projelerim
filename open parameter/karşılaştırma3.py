d1 = open("/home/ali/Masaüstü/isimler.txt") #dosyayı açıyoruz
d1_satırlar = d1.readlines() #satırları okuyoruz

d2 = open("/home/ali/Masaüstü/isimler2.txt")
d2_satırlar = d2.readlines()

for i in d2_satırlar:
	if not i in d1_satırlar:
		print(i)

d1.close()
d2.close()
