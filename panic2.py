phrase = "Don't panic!"
plist = list(phrase)
#plist1 = plist.copy[1: 8]
print(phrase)
print(plist)

new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])


#new_phrase = ''.join(plist)
print(plist)
print(new_phrase)