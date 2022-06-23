# -*- coding: utf-8 -*-
from collections import deque; """ stack veri yapısını kullanmak için deque import ediyoruz"""

"""
Spyder Editor

This is a temporary script file.
"""

#Düğüm sınıfımızın özellikleri

class node:
    def __init__(self,girdi=None):
        self.girdi=girdi #düğüm data
        self.next=None #düğüm next
        
class linked_list:
    def __init__(self):
        self.head=node()
        
    def ekle(self,girdi):
        yeni_node = node(girdi)
        mevcut = self.head
        while mevcut.next != None:
            mevcut = mevcut.next
        mevcut.next = yeni_node
        
    def sil(self,index):
        mevcut_idx=0 #node'lara girilen datalara ek index oluşturduk arama ve silme işlemi kolaylığı için.
        mevcut_node=self.head
        while True: 
            son_node = mevcut_node
            mevcut_node = mevcut_node.next
            if mevcut_idx == index:
                son_node.next = mevcut_node.next
                return
            mevcut_idx +=1 #index bilgisine göre aramaya devam etmek için her defasında 1 arttırıyoruz.
        
    def uzunluk(self): #bağlantılı listemizde toplam kaç adet node olduğunu belirlemek için uzunluk defi tanımlıyoruz.
        mevcut = self.head
        toplam = 0
        while mevcut.next != None:
            toplam +=1
            mevcut = mevcut.next
        return toplam 
    
    def yaz(self):
        girdiler = []
        mevcut_node = self.head
        while mevcut_node.next != None:
            mevcut_node = mevcut_node.next
            girdiler.append(mevcut_node.girdi)
        print(girdiler)
        
    def yakala(self,index):       #silme,undo ve redo işlemleri için istediğimiz data'yı yeni node eklerken veya çıkartırken saklamak amaçlı.
        mevcut_idx=0
        mevcut_node=self.head
        while True:
            mevcut_node=mevcut_node.next
            if mevcut_idx == index:
                return mevcut_node.girdi
            mevcut_idx +=1
            
    
listemiz = linked_list() #Bağlantılı listemizi classımıza tanımlıyoruz.
# listemiz.yaz() #Kontrol
temp =[] #Undo ve redo işlemlerinde dataları saklamak için kullandığımız liste.
print("Bir işlem seçiniz:\n(yaz)\n(undo)\n(redo)\nveya bir girdi veriniz:\t")

while True:
    
    islem = input()
    
    if islem =="yaz":
        listemiz.yaz()
        
    elif islem =="undo":
        if len(temp) < 5:
            temp.append(listemiz.yakala(listemiz.uzunluk()-1))
            listemiz.sil(listemiz.uzunluk()-1)
            #listemiz.yaz() #Kontrol
        else:
            temp.pop(0) 
            temp.append(listemiz.yakala(listemiz.uzunluk()-1))
            listemiz.sil(listemiz.uzunluk()-1)
            #listemiz.yaz() #Kontrol                  
                  
    elif islem =="redo":
        if len(temp)>=1:
            listemiz.ekle(temp[-1])
            temp.pop()
            #listemiz.yaz() #Kontrol
        else:
            print("Daha fazla redo işlemi yapılamaz!")
            #listemiz.yaz() #Kontrol
            
    else:
        if len(temp)>=1:
            for i in range(len(temp)):
                temp.pop(i)
            listemiz.ekle(islem)
            print(islem,"eklendi.")                
            #listemiz.yaz() #Kontrol    
        else :       
            listemiz.ekle(islem)       
            print(islem,"eklendi.")          
            #listemiz.yaz() #Kontrol
        


