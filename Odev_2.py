
ad = input("Lütfen adınızı giriniz: ")
soyad = input("Lütfen soyadınızı giriniz: ")
yas= int(input("Lütfen yaşınızı giriniz: "))
yıl= int(input("Lütfen hangi yılda doğduğunuzu yazınız: "))

bilgiler = ad, soyad, yas, yıl

a= list(bilgiler)
print("-"*50)

for i in a:
  print(i)

print("-"*50)

if yas<18:
  print("you can't go out because it's too dangerous")
else:
  print("you can go out the street")