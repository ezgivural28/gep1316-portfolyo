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
