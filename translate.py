from googletrans import Translator

sentence=str(input("say ......"))
translator=Translator()
translated_sentence=translator.translate(sentence,src="en",dest="tr")

print(translated_sentence)

#open powershell
#https://www.labnol.org/code/19899-google-translate-languages