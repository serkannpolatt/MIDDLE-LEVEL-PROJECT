






def mailcreate(nickname,mailtype="gmail.com"):
    mailadresi="@".join([nickname,mailtype])
    return mailadresi

nickname=input("lütfen kullanıcı adını giriniz : ")
mail=input("lütfen mail tipini giriniz : ")
if mail:
    print("mail adresi: ", mailcreate(nickname, mail))
else:
    print("mail adresi : ",mailcreate(nickname))

