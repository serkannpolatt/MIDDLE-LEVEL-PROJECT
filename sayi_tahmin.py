import random
maxtahsayi=13
tensayac=0
sixsayac=0
foursayac=0
nettahminsayi=0
sayiDyerD=0
sayiDyerY=0

tenlist=[]
sixchoicelist=[]
fourchoicelist=[]


while tensayac < 10:
    tennumgen=int(random.random()*100)
    tenlist.append(tennumgen)
    tensayac+=1

while sixsayac <6:
    sixchoice=random.choice(tenlist)
    sixchoicelist.append(sixchoice)
    sixsayac+=1

while foursayac <4:
    fourchoice=random.choice(sixchoicelist)
    if fourchoicelist.count(fourchoice)==0:
        
        fourchoicelist.append(fourchoice)
        foursayac+=1

print("10 sayısının:",tenlist)
print("10 sayıdan seçilen 6sı :",sixchoicelist)
print("6 saydıdan seçilen 4 sayımız :",fourchoicelist)    


while nettahminsayi < maxtahsayi:
    sayitahmin=int(input("lütfen sayıyı tahmın ediniz"))
    yertahmin=int(input("lütfen yerini tahmin ediniz"))
    print("{} tahmin hakkınız kaldı".format(maxtahsayi-nettahminsayi))
    nettahminsayi+=1

    sayitahminsayac=fourchoicelist.count(sayitahmin)
    try:
        yertahminsayac=fourchoicelist.index(sayitahmin)

    except:
        print("başarısız deneme")


    if sayitahminsayac >0 and yertahminsayac == yertahmin:
        sayiDyerD+=1   

    elif sayitahminsayac >0 and yertahminsayac !=yertahmin:
        sayiDyerY+=1

    print("D:",sayiDyerD)
    print("Y:",sayiDyerY)