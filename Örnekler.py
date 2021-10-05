#Yıldızlarla şekil çizmece *********************

sayi=int(input("Kac yıldız olsun:"))
yildiz=""
for i in range(sayi):
    yildiz=yildiz+"* "
    print(yildiz)

##Bir class tanımı,fonksiyonlarla *******************
class Matematik:
    
    def __init__(self,sayi1,sayi2):
        self.sayi1=sayi1
        self.sayi2=sayi2
        
    def topla(self):
        return self.sayi1+self.sayi2
    
    def cikar(self):
        return self.sayi1-self.sayi2
    
    def carp(self):
        return self.sayi1*self.sayi2
    
    def bol(self):
        return self.sayi1/self.sayi2
    
i=""
while(i!="q"):
    print("***********************")
    print("İşlem seçiniz:")
    print("1-Toplama")
    print("2-Çıkarma")
    print("3-Çarpma")
    print("4-Bölme")
    print("Çıkış:q")
    islem=input("İşlem:")
    if(islem=="q"):
        print("Hesap makinesi kapanıyor...")
        break
    sayi1=int(input("Sayı 1 :"))
    sayi2=int(input("Sayı 2 :"))
    
    
    if(islem=="1"):
        matematik=Matematik(sayi1,sayi2)
        print("İşlem sonucu: " + str(matematik.topla()))
    
    elif(islem=="2"):
        matematik=Matematik(sayi1,sayi2)
        print("İşlem sonucu: " + str(matematik.cikar()))

    elif(islem=="3"):
        matematik=Matematik(sayi1,sayi2)
        print("İşlem sonucu: " + str(matematik.carp()))

    elif(islem=="4"):
        matematik=Matematik(sayi1,sayi2)
        print("İşlem sonucu: " + str(matematik.bol()))
        
    


import math
#1'den 1000000'a kadar olan asal sayıları algoritmik yazdırma *******************
##%% #Algoritmik
for x in range(1,1000000):
    a=0
    for i in range(2,int(math.sqrt(x))):
        if(x%i==0):
            a=1
            
        if(a==0):
            print(x)
##%% #Performansız yol
for x in range(1,1000000):
    a=0
    for i in range(2,x):
        if(x%i==0):
            a=1
            
        if(a==0):
            print(x)
            




    
    

