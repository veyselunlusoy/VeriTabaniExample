import sqlite3
baglan=sqlite3.connect('veri.db')
if baglan:
    print('Bağlantı Başarılı')
else:
    print('Bağlantı Başarısız')

veri=baglan.cursor()
veri.execute('''
INSERT INTO sinif(            
            sinif_no,
	        sinif_adi)
             VALUES(
             1,
             '10A'
             )     
	        
''')
print('Kayıt eklendi')
baglan.commit()
baglan.close()
