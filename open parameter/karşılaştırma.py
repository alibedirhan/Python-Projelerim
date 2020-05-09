# ilk_metin adlı değişkende bulunan ama ikinci_metin adlı değişken içinde bulunan ögeleri ayıklamak istiyoruz. ilk_metin adlı değişkende olup da ikinci_metin adlı değişkende olmayan ögeler bu program ile listelenir.

ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"

ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"

for s in ilk_metin: #ilk_metindeki s adını verdiğimiz bütün ögerel için
	if not s in ikinci_metin: #eğer s adlı bu öge ikinci_metinde yoksa
		print(s) # s adlı ögeyi ekrana bas

