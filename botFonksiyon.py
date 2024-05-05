import random


def sifreOlusturucu(uzunluk):
    sifre = ""
    karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    for i in range(uzunluk):
        sifre += random.choice(karakterler)

    return sifre

def yaziTura():
    rastgeleSayi = random.randint(1, 2)

    if rastgeleSayi == 1:
        return("Yazı")
    if rastgeleSayi == 2:
        return("Tura")