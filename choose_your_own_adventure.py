name=input("Type your name :")
print("Welcome",name,"to this my adventure!!")

answer=input("you are on a dirt road, it has come to an end you can go left or right?.Which way would you like to go ?:")
#toprak bir yoldasın yolun sonuna geldi sağa sola gidebilirsin hangi yöne gitmek istersin

if answer=="left":
    answer=input("you come to a river, you can walk around it or swim across?Type walk to walk around and swim to swim accross?:")
#bir nehre geldin, etrafından yürüyebilir veya yüzebilirsin? Yürümek için yürü, yüzerek karşıdan karşıya geçmek için mi? yazın
    if answer =="swim":
        print("your swam acrross and were eaten by an alligator.YOU LOSE")
#yüzerek karşıya geçtin ve bir timsah tarafından yenildin        
    elif answer =="walk":
        print("you walked for many miles,ran out of water and you lost the game.")
#kilometrelerce yürüdün su bitti ve oyunu kaybettin        
    else:
        print("not a valid option.You lose...")
#geçerli bir seçenek değil. Kaybedersin...        


elif answer =="right":
    answer=input("You come to a bridge,it looks wobbly,do you want to cross it or head back (cross/back)?:")
#Bir köprüye geldiniz, titrek görünüyor, onu geçmek mi istiyorsunuz yoksa geri mi gitmek istiyorsunuz?    
    if answer=="back":
        print("You go back and lose.")
    elif answer =="cross":
        answer=input("You cross the bridge and meet a stranger.Do you talk to them (yes/no)?:")
#Köprüyü geçersin ve bir yabancıyla tanışırsın.Onlarla konuşur musun? 
        if answer =="Yes":
            print("You talk to the stranger and they give you gold.You WİN!!!") 
#yabancıyla konuşursun ve sana altın verirler. sen kazanırsın            
        elif answer=="no":
            print("you ignore the and they are offended and you lose.")
#görmezden gelirsin ve kırılırlar ve kaybedersin            
        else:
            print("you lose...")                 