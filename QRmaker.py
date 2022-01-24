import qrcode
print("QR Kod oluşturucuya hoş geldiniz,Burada bir linki QR Kod olarak bilgisayarınıza kaydedebilirsiniz.")
qrlink = input("Lütfen linki giriniz: ")
img = qrcode.make(qrlink)
qrisim = input("QR kodunuzu hangi isimde kaydetmek istiyorsunuz?   ")
#jpg olarak kaydediliyor buradan isterseniz değiştirebilirsiniz.
img.save(qrisim + ".jpg")
print("QR kodunuz başarılı bir şekilde oluşturulmuştur.")
#QR kod python dosyasının olduğu yere kaydediliyor.