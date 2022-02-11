
def menuSecim():
    print("[1]. listele")
    print("[2]. ekle")
    print("[3]. sil")
    print("[4]. ara")
    print("[5]. çıkış")
    menuSec=0
    while menuSec != 5:
        menuSec=int(input("seçiminiz nedir:"))
        if menuSec ==1:
            listele()
        elif menuSec ==2:
            ekle()
        elif menuSec ==3:
            sil()
        elif menuSec ==4:
            ara()
        elif menuSec ==5:
            çıkış()
        else:
            print("Lütfen 1 ile 5 arasında sayı giriniz: ")

# numaralar={}

# def listele():
    # print("Telefon Rehberim:")
    # for x in numaralar.keys():
    #    print("Ad-Soyad: ", x , "\tNumara:", numaralar[x]) 
    #    print()

# def ekle():
    # print("Ad-Soyad ve Numara Ekle:") 
    # ad=input("Ad-Soyad:")
    # tlfn=input("Numara:")  
    # numaralar[ad]= tlfn  

# def sil():
    # ad=input("rehberdeki silinicek kayıt: ")
    # if ad in numaralar:
        # del numaralar[ad]
        # print("silindi")
    # else:
        # print(ad,"bulunamadı")

# def ara():
    # ad=input("aradığınız isim:")
    # if ad in numaralar:
        # print("numarası",numaralar[ad])       
    # else:
        # print(ad," bulunamadı")     

# def cikis():
    # print("program sonlandırıldı")
    # raise SystemExit() 

# if __name__ == "__main__":
    # menuSecim()



