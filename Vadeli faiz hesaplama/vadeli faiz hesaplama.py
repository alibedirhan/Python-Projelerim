print("-"*10,"*","-"*10)
while True: 
    anapara = int(input ("Anaparayı Giriniz : "))
    faiz_oranı = float(input("Faiz Oranını Giriniz : "))
    vade = int(input("Vade/Gün Sayısını Giriniz : "))


    def bürüt_faiz_oranı():
        bürüt_deger = anapara * faiz_oranı * vade/36500
        return bürüt_deger


    def net_faiz_oranı():
        bürüt_deger = bürüt_faiz_oranı()
        net_değer = bürüt_deger - (bürüt_deger * 5/100)
        return net_değer

    print("bürüt faiz oranı : ", bürüt_faiz_oranı())
    print("net faiz oranı : ", net_faiz_oranı())
    print("-"*10,"*","-"*10)
