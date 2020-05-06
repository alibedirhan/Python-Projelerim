print("*"*15 ,"\nNot Hesaplama\n","*"*15)

while True:
    vize1 = int(input("İlk Vizenizi giriniz :"))
    vize2 = int(input("İkinci Vizenizi giriniz :"))
    final = int(input("final Vizenizi giriniz :"))


    toplam_not = (vize1 * 30) / 100 + (vize2 * 30) / 100 + (final * 40) / 100

    if (toplam_not >= 90):
        print("AA")

    elif (toplam_not >= 85):
        print("{} ile BA aldınız.".format(toplam_not))

    elif (toplam_not >= 80):
        print("{} ile BB aldınız.".format(toplam_not))

    elif (toplam_not >= 75):
        print("{} ile CB aldınız.".format(toplam_not))

    elif (toplam_not >= 70):
        print("{} ile CC aldınız.".format(toplam_not))

    elif (toplam_not >= 65):
        print("{} ile DC aldınız.".format(toplam_not))

    elif (toplam_not >= 60):
        print("{} ile DD aldınız.".format(toplam_not))

    elif (toplam_not >= 55):
        print("{} ile FD aldınız.".format(toplam_not))

    elif (toplam_not < 55):
        print("{} ile FF alıp kaldınız.".format(toplam_not))

    else:
        print("geçerli bir not giriniz!")







