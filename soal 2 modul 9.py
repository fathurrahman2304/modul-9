def buatfile():
    namafile = input('Masukkan Nama File: ')
    namamu = input('Masukkan Namamu: ')
    nim = input('Masukkan NIM kamu: ')
    angkatan = input('Masukkan Tahun Angkatanmu: ')
    file = open(f'{namafile}.txt','w')
    file.write(f'Nama: {namamu} \nNIM: {nim} \nTahun Angkatan: {angkatan}')
    file.close()
def nulisfile():
    namafile = input('Masukkan Nama File: ')
    print()
    file = open(f'{namafile}.txt','r')
    text = file.read()
    print(text)
    file.close()
def tambahan():
    namafile = input('Masukkan Nama File: ')
    sahabat = input('Masukkan Nama Sahabatmu: ')
    kata = input('Masukkan Catatan Tambahan Kamu: ')
    file = open(f'{namafile}.txt','a')
    file.write(f'\nNama Sahabat: {sahabat} \nCatatan: {kata}')
    file.close()
    print('\n\nData berhasil ditambahkan')
while True:
    print('\n==== Program File Handling ==== \n1. Membuat dan Menulis File \n2. Membaca File \n3. Menambahkan Text Pada File \n4. Keluar Dari Program')
    pilihan = int(input('\nMasukkan pilihan berupa angka (1/2/3/4): '))
    if pilihan == 1 :
        buatfile()
    elif pilihan == 2:
        nulisfile()
    elif pilihan == 3:
        tambahan()
    elif pilihan == 4:
        print('Program Selesai')
        break
    else:
        print('Mohon masukkan angka sesuai yang diminta')