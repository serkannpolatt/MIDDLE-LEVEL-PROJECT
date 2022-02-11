import urllib.request

adres="http://shallowsky.com/python/lesson5.txt"
f=urllib.request.urlopen(adres)
dosya=f.read().decode()
print(dosya)
