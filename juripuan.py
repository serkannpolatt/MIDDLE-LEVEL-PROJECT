
juripuanlist=[]
def jurisoru():
    
    sayac=1
    while sayac < 6:
        
        juripuanlar=int(input("{}.juri Puan giriniz:".format(sayac)))
        juripuanlist.append(juripuanlar)
        sayac+=1



def ortalamahesapla(defaultliste):
    
    top=0
    elemansayi=len(defaultliste)
    for i in juripuanlist:
        top=i+top
    return top / elemansayi

def yorumlar():
    if ortalama >= 1 and ortalama <=2.5:
        print("başaramadınız")
    
    elif ortalama >=3 and ortalama <=5.5:
        print("biraz daha çalış")

    elif ortalama >=5 and ortalama <=7.5:
        print("Tebrikler geçtiniz".format(ortalama))

    
jurisoru()
ortalama=ortalamahesapla(juripuanlist)
yorumlar()
