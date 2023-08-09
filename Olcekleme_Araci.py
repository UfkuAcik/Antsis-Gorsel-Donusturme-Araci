import cv2
import glob
import os
from tkinter.filedialog import askdirectory

print("Hosgeldiniz!!")
print("Bu program sectiginiz klasorun icindeki tüm görselleri seri sekilde yeniden boyutlandıracak.")
print("Donusturulmus gorseller,Donusturulmus Klasoru(Kaynak Klasor ile komsu) icinde depolanacak.")
print("KAYNAK KLASOR ADRESI SAKIN TURKCE KARAKTER ICERMESIN!!!!!")
print("Ornegin: Masa(u)st(u)\Yeni klas(o)r")
print("NOT:SECILEN KLASORUN ALTINDAKI KLASORLER ICIN GORSELLER DONUSTURULMEYECEKTIR.")
print("Alt klasorler icindeki gorselleri donusturmek icin")
print("Programı yeniden calistiriniz.")
i=0
while(True):
  if(i>0):
   print("Basa Donduk Dizin Seciniz")
  if(i==0):
      print("Dizin Seciniz")
  dizin = '{}'.format(askdirectory(title='Donusturulecek Gorsellerin Klasorunu Seciniz', mustexist=True))
  print("Girdiginiz Dizin:"+dizin)

  yatay = input("Yatay Oran(%) Gir Gardas: ")
  dikey = input("Dikey Oran(%) Gir Gardas: ")
  print("Girdiginiz Yatay Oran(%) :" + yatay + " ; " +"Girdiginiz Dikey Oran(%) :" + dikey)

  print("1:AREA")
  print("2:CUBIC")
  print("3:LANCZOS4")
  print("4:LINEAR")
  print("5:LINEAR_EXACT")
  print("6:NEAREST")
  print("7:NEAREST_EXACT")

  yonteminput = input("Interpolasyon Yontemi Gir Gardas: ")

  if(yonteminput=="1"):
     yontem = "AREA"
     interpolation=cv2.INTER_AREA
  if(yonteminput=="2"):
     yontem = "CUBIC"
     interpolation = cv2.INTER_CUBIC
  if(yonteminput=="3"):
     yontem = "LANCZOS4"
     interpolation = cv2.INTER_LANCZOS4
  if(yonteminput=="4"):
     yontem = "LINEAR"
     interpolation = cv2.INTER_LINEAR
  if(yonteminput=="5"):
     yontem = "LINEAR_EXACT"
     interpolation = cv2.INTER_LINEAR_EXACT
  if(yonteminput=="6"):
     yontem = "NEAREST"
     interpolation = cv2.INTER_NEAREST
  if(yonteminput=="7"):
     yontem = "NEAREST_EXACT"
     interpolation = cv2.INTER_NEAREST_EXACT

  print("Sectiginiz Yontem:" , yontem)


  inputFolder = dizin

  os.mkdir(dizin + "_" + yontem + '_' + '%' + yatay + '_' + '%' + dikey)


  for x in glob.glob(inputFolder + "/*.png"):
     path=str(x)
     img = cv2.imread(x)

     width = int((img.shape[1] * int(yatay)) / 100)  # dim integer olmak zorunda
     height = int((img.shape[0] * int(dikey)) / 100) # % olarak kucultme oranı
     dim = (width, height)

     resized = cv2.resize(img, dim, interpolation)

     pathname, extension = os.path.splitext(path)
     file = pathname.split('\\')
     print("Suan Duzenlenen Dosya:" + file[-1] + ".png")

     cv2.imwrite(dizin + "_" + yontem + '_' + '%' + yatay + '_' + '%' + dikey +'/' + file[-1] +".png", resized)

  for y in glob.glob(inputFolder + "/*.jpg"):
     path=str(y)
     img = cv2.imread(y)

     width = int((img.shape[1] * int(yatay)) / 100)  # dim integer olmak zorunda
     height = int((img.shape[0] * int(dikey)) / 100) # % olarak kucultme oranı
     dim = (width, height)

     resized = cv2.resize(img, dim, interpolation)

     pathname, extension = os.path.splitext(path)
     file = pathname.split('\\')
     print("Suan Duzenlenen Dosya:" + file[-1] + ".jpg")

     cv2.imwrite(dizin + "_" + yontem + '_' + '%' + yatay + '_' + '%' + dikey +'/' + file[-1] +".jpg", resized)

  for z in glob.glob(inputFolder + "/*.bmp"):
     path=str(z)
     img = cv2.imread(z)

     width = int((img.shape[1] * int(yatay)) / 100)  # dim integer olmak zorunda
     height = int((img.shape[0] * int(dikey)) / 100) # % olarak kucultme oranı
     dim = (width, height)

     resized = cv2.resize(img, dim, interpolation)

     pathname, extension = os.path.splitext(path)
     file = pathname.split('\\')
     print("Suan Duzenlenen Dosya:" + file[-1] + ".bmp")

     cv2.imwrite(dizin + "_" + yontem + '_' + '%' + yatay + '_' + '%' + dikey +'/' + file[-1] +".bmp", resized)

  for m in glob.glob(inputFolder + "/*.jpeg"):
     path=str(m)
     img = cv2.imread(m)

     width = int((img.shape[1] * int(yatay)) / 100)  # dim integer olmak zorunda
     height = int((img.shape[0] * int(dikey)) / 100) # % olarak kucultme oranı
     dim = (width, height)

     resized = cv2.resize(img, dim, interpolation)

     pathname, extension = os.path.splitext(path)
     file = pathname.split('\\')
     print("Suan Duzenlenen Dosya:" + file[-1] + ".jpeg")

     cv2.imwrite(dizin + "_" + yontem + '_' + '%' + yatay + '_' + '%' + dikey +'/' + file[-1] +".jpeg", resized)
  i=i+1
  Devam = input("Devam etmek ister misiniz?  (E/H): ")
  if(Devam == "H"):
      break
