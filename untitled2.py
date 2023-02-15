# 27- dars. kiril-lotin telegram bot

from transliterate import to_cyrillic, to_latin


# print(to_latin('олмахон'))
# print(to_cyrillic('qariyalar uyidagi kampirlar'))

matn=input("Matn kiriting : ")
if matn.isascii():
    print(to_cyrillic(matn))
else:
    print(to_latin(matn))

6001798060:AAH_DuGUHu9fIebpbbBseBDz_1tY1txacHw







