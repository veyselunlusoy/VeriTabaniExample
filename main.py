import sqlite3
baglan=sqlite3.connect('veri.db')
if baglan:
    print('Bağlantı Başarılı')
else:
    print('Bağlantı Başarısız')
#bağlantı cümlesi
veri=baglan.cursor()

veri=baglan.cursor()
ogr= veri.execute('SELECT * FROM  ogrenci WHERE ogrenci_No= 5')
#print(ogr.fetchall())

for i in ogr.fetchall():
    print("Öğrenci No: %s -- İsmi: %s -- Soyadı: %s -- Sınıfi: %s" %i)


print('Kayıt eklendiii')
baglan.commit()
baglan.close()
