dilekçe = """
							tarih : {}
T.C.
{} ÜNİVERSİTESİ
{}Fakültesi Dekanlığına

Fakülteniz {} Bölümü {} numaralı öğrencisiyim. Ekte sunduğum belgede belirtilen mazeretim gereğince {} Eğitim-Öğretim Yılı {}. yarıyılında öğrenime ara izin (kayıt dondurma) istiyorum.

		Bilgilerinizi ve gereğini arz ederim.

	İmza
Ad		:{}
Soyad		:{}
T.C. Kimlik No	:{}
Adres		:{}
Tel.		:{}
Ekler		:{}
"""


tarih = input("Tarih : ")
üniversite = input("Üniversite : ")
fakülte =input("Fakülte : ")
bölüm = input ("Bölüm : ")
öğrenci_no = input("Öğrenci Numarası : ")
öğretim_yılı = input("Öğretim Yılı : ")
yarıyıl = input("yarıyıl: ")
ad = input("öğrencinin adı: ")
soyad = input("öğrencinin soyadı: ")
tc_kimlik_no = input("TC Kimlik no. :")
adres = input("adres: ")
tel = input("telefon: ")
ekler = input("ekler: ")


print(dilekçe.format(tarih, üniversite, fakülte, bölüm,
öğrenci_no, öğretim_yılı, yarıyıl,
ad, soyad, tc_kimlik_no,
adres, tel, ekler))
