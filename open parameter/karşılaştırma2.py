#ikinci_metindeki ögeleri ilk metin ile karşılaştırabiliriz. bu karşılaştırmada aynı ögeye sahıp harfler çıkıyor bunu düzeltmek için fark adlı bir değişken oluşturuyoruz


ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"

ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"

fark = ""

for s in ikinci_metin:
	if not s in ilk_metin:
		if not s in fark:
			fark += s
print(fark, sep=".\t")
