from datetime import datetime  
#form kütüphane import araç  Böylece kodun içinde her seferinde datetime.datetime.now() yazmak yerine sadece datetime.now() yazabiliyoruz.

with open("server.log","r",encoding="utf-8") as dosya:
    #Açmak istediğimiz dosyanın adı
    #"read" Dosyayı sadece okuma modunda açtığımızı, içindeki yazıları silmeyeceğimizi belirtir.
    #encoding="utf-8": İçinde Türkçe veya özel karakterler varsa hata almamak için eklediğimiz bir güvenlik önlemidir.
    #takma adı "dosya"

    error_sayac = 0
    failed_sayac = 0
    sayac_404 = 0
    warning_sayac =0

    for satir in dosya:
        if  "ERROR" in satir:
            print(satir)
            error_sayac +=1

        if  "FAILED LOGIN" in satir:
            print(satir)
            failed_sayac +=1

        if  "404" in satir:
            print(satir)
            sayac_404 +=1
        if  "WARNING" in satir:
            print(satir)
            warning_sayac +=1
    print(f"Toplam \"ERROR\" Hata sayısı: {error_sayac}")
    print(f"Başarısız Giriş sayısı: {failed_sayac}")
    print(f"Bulunamayan Sayfa sayısı: {sayac_404}")
    print(f"Toplam \"WARNING\" Hata sayısı: {warning_sayac}")
now = datetime.now()
timestamp = now.strftime("%d.%m.%Y  %H:%M:%S") 

with open ("rapor.txt","w",encoding="utf-8") as rapor:
    rapor.write(f"Analysis Date: {timestamp}\n")
    rapor.write("-"*60+"\n")  #görsel çizgi

    rapor.write(f"Toplam {error_sayac} adet \"ERROR\" Hatası Saptandı!\n")
    rapor.write(f"Toplam Başarısız Giriş sayısı {failed_sayac} olarak tespit edildi!\n")
    rapor.write(f"Bulunamayan Sayfa sayısı {sayac_404} olarak tespit edildi!\n")
    rapor.write(f"Toplam \"WARNING\" Hata sayısı: {warning_sayac}")