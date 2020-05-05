sayaç = 0

for i in dir(""):
	if "_" not in i[0]:
		sayaç += 1
		print(i)
print("Toplam {} adet metot ile ilgileniyoruz.".format(sayaç))
