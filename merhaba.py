# Kullanıcının adını metin (string) olarak alır ve 'ad' değişkenine kaydeder.
ad = input("Adınız nedir? ")
# Kullanıcının doğum yılını metin olarak alır ve int() ile tam sayıya (integer) çevirir.
dogum_yili = int(input("Doğum yılınız nedir? "))
# Yaş hesabında kullanmak üzere güncel yılı tam sayı olarak tanımlar.
guncel_yil = 2026
# Güncel yıldan doğum yılını çıkararak kullanıcının yaklaşık yaşını hesaplar.
yas = guncel_yil - dogum_yili
# Kullanıcının adı ve hesaplanan yaşıyla kişiye özel karşılama mesajı yazdırır.
print(f"Merhaba {ad}! 2026 yılı itibarıyla {yas} yaşındasın.")
# Kullanıcının yaşına göre farklı bir bilgilendirme mesajı gösterir.
if yas >= 18:
    # 18 yaş ve üzeri için ek mesaj yazdırır.
    print("Yetişkin dönemindesin; yeni hedefler ve keşifler için harika bir zaman!")
else:
    # 18 yaş altı için ek mesaj yazdırır.
    print("Henüz yolun başında genç bir dönemdesin; öğrenmeye devam!")
