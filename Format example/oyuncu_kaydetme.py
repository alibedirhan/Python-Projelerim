print("Oyuncu Kaydetme Programı")

ad = input("Oyuncunun Adı:")
soyad = input("Oyuncunun Soyadı:")
takım = input("Oyuncunun Takımı:")

bilgiler = [ad,soyad,takım]

print("Bilgiler Kaydediliyor...")

print("Oyuncunu Adı: {}\nOyuncunun Soyadı: {}\n Oyuncunun Takımı: {}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("Bilgiler Kaydedildi...")

print(bilgiler)
print("bilgilerin uzunluğu",len(bilgiler))
print("Bu verinin tipi",type(bilgiler))

bilgiler[0] = "bedirhan"

print(bilgiler)




