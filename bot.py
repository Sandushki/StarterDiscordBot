"""
Discord için bir bot yazmak istiyorsak discord kütüphanesini bilgisayarımıza indirmemiz gerekiyor.
Bunu, sakın dış kaynaklardan indirmeyelim.
Terminal kullanarak indirelim.
Terminal --> Kodlarımızın çıktısını gördüğümüz yer. Terminal açmak için ctrl + shift + " --> Terminal açılıyor

Terminalden indirmek için, Pyhton'ın Python Paket Yönetim Sistemi'ni kullanmamız gerekir --> Python Install Package --> pip install
Terminalde bu paket yönetim sistemini güncellemek --> pip install --upgrade pip

Bilgisayarımıza herhangi bir kütüphaneyi indirmek istiyorsak, pip install <indireceğiniz kütüphanenin adı>
Discord modülü indirmek için, pip install discord yazacağız.
"""

# Discord botu oluşturmak için Discord kütüphanesini içe aktaralım.
import discord

# Benim farklı bir Python belgemden istediğim fonsiyonu çekmek içim from fonksiyonu kullanılır.
# İmport anahtar kelimesinden sonra teker teker fonksiyonların adını yazabiliriz ama bütün fonksiyonları almak için * sembolünü kullanırız.
from botFonksiyon import *
# Botun ayrıcalıklarını depolayacak bir değişken oluşturalm. --> intents = ayrıcalıklar
intents = discord.Intents.default()

# Mesajları okuma ayrıcalığını vermemiz gerekir.
intents.message_content = True

# İstemci(Client) değişkeni ile bot oluşturalım.
client = discord.Client(intents=intents)

"""
def anahtar kelimesi definition(tanımlama) anlamına gelir.
on_ready() fonksiyonu, bizim Discord'a giriş yaptıüımız anda botun hazır olduğuhnu belirten bir mesajı yayımlamak için kullanılan fonksiyondur.

Dekaratör: Bazı fonksitonların belirli eylemler gerçekleştikten sonra çalışmasını sağlar.
Bir dekaratör oluşturmak için @ işaretiyle başlarız.

@client.event deklaratörü on_ready() fonksiyonunun bot tarafından işleneceğini ve bu şekilde işleneceğini belirtir.
fonksiyonların senkronize bir şekilde çalışmasını sağlamak için async anahtar kelimesi kullanılır.
"""
@client.event
async def on_ready():
    print(f'{client.user} olarak Discord\'a uçtuk!')


# on_message() fonksiyonu bizim bota gönderdiğimiz mesajları algılayan ve buna cevap yazılacak işlemlerin yazıldığı fonksiyondur.
@client.event
async def on_message(message):
    if message.author == client.user:
        # Yanıtları geri döndürür.
        return
    # Eğer mesaj içeriği ... ile başlarsa
    # prefix --> botun mesajı algılayabilmesi için anahtar sembol
    if message.content.startswith('$merhaba'):
        # await anahtar kelimesi ile birkaç saniye bekliyoruz.
        # message.channel.send() fonksiyonu discord sunucusuna bir mesaj gönderir.
        await message.channel.send("Hoş geldiniz!")

    elif message.content.startswith('$görüşürüz'):
        await message.channel.send("Güle güle!")

    elif message.content.startswith('$şifre oluştur'):
        await message.channel.send("Sizin için oluşturduğumuz 15 haneli şifre: " + sifreOlusturucu(15))

    elif message.content.startswith('$yazı tura'):
        await message.channel.send("Sonucunuz: " + yaziTura())

    elif message.content.startswith('$emoji'):
        await message.channel.send(emoji())

    elif message.content.startswith('$Temizle'):
        await message.channel.send(temizle())

    elif message.content.startswith('$'):
        await message.channel.send("Bu komut hatalı.\nLütfen aşağıdaki komutlardan birini kullanın:\n\n" + komutCikar())

# Botu çalıştırmak --> .run() fonksiyonu botu çalıştırmamızı sağlar.
# API --> token
# Yazarken bunun veri türünü string olarak kullanmamız gerekir.
client.run('') # Why would I tell the token?
