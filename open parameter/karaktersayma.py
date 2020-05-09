metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin Python olmasına aldanarak, bu programlama dilinin, adını piton yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından gelmez. Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz komedi grubunun, Monty Python’s Flying Circus adlı gösterisinden esinlenerek adlandırmıştır. Ancak her ne kadar gerçek böyle olsa da, Python programlama dilinin pek çok yerde bir yılan figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır."""

harf = input("Sorgulamak istediğiniz harf : ")

sayı = ''

for s in metin:		#metin içinde s adını verdiğimiz herbir öge için
	if harf ==s:	#eğer kullanıcıdan gelen harf s ile aynıysa
	   sayı += harf #kullanıcıdan gelen bu harfi sayı değişkenine yolla
print(len(sayı))

#metin değişkeni içine bir paragraf yazdık ve daha sonra kullanıcıya hangi harfi sorgulamak istediğini sorduk.

# burada tanımlanan sayı adlı değişken , sorgulanan harfi, metinden geçtiği sayıda içinde barındıracaktır. 
