def data(nama,Umur,alamat,email,dosenwali):
    file = open('Biodata.txt','w')
    file.write(f'Nama : {nama} \nUmur : {Umur} \nAlamat : {alamat} \nEmail : {email} \nDosen wali : {dosenwali}')
    file.close()
def baca():
    print('\nBerikut biodatamu')
    file = open('Biodata.txt','r')
    text = file.read()
    print(text)
    file.close()

nama = input('Masukkan Nama: ')
Umur = input('Masukkan Umur: ')
alamat = input('Masukkan alamat: ')
email = input('Masukkan email: ')
dosenwali = input('Masukkan dosen wali: ')
data(nama,Umur,alamat,email,dosenwali)
baca()