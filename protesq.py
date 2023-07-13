
print("Yapacağın işlemi seç, toplama için : 1 , çıkarma için : 2, bölme için : 3, çarpma için : 4 ")
a= int(input("Yapacağınız işlemi giriniz : "))
run = True
while run: 
    if a==1:
        def topla(num1,num2):
            toplam = num1 + num2
            print(f'Toplam : {toplam}')
        num1 = int(input("Birincİ sayıyı giriniz:"))
        num2 = int(input("İkinci sayıyı giriniz:"))
        topla(num1,num2)
    elif a==2:
        def cikar(num1,num2):
            toplam = num1 - num2
            print(f'Sonuc : {toplam}')
        num1 = int(input("Birincİ sayıyı giriniz:"))
        num2 = int(input("İkinci sayıyı giriniz:"))
        cikar(num1,num2)
    elif a==3:
        def bolme(num1,num2):
            sonuc = num1 / num2
            print(f'Sonuc : {sonuc}')
        num1 = int(input("Birincİ sayıyı giriniz:"))
        num2 = int(input("İkinci sayıyı giriniz:"))
        bolme(num1,num2)
    elif a==4:
        def carp(num1,num2):
          sonuc = num1*num2
          print(f'Sonuc : {sonuc}')
        num1 = int(input("Birincİ sayıyı giriniz:"))
        num2 = int(input("İkinci sayıyı giriniz:"))
        carp(num1,num2)
    else :
      print("Hatalı işlem yaptınız.")