from math import*

def f(x):
	return cos(x)

	fonk=input("lütfen cosinüs aralığını girin : ")

a = 0.001
for i in range(5):
	f1=(1-cos(a))

	if fonk == "5":
		print("cosinüs fonksiyonunun değeri" ,"%.5f" %f1)

	elif fonk == "10":
		print("cosinüs fonksiyonunun değeri" ,"%.10f" %f1)
	
	elif fonk == "15":
		print("cosinüs fonksiyonunun değeri" ,"%.15f" %f1)

