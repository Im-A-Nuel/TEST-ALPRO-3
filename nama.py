#input 3 nama
nama1=input('Masukan nama 1 :')
nama2=input('Masukan nama 2 :')
nama3=input('Masukan nama 3 :')

#proses
panjang1=len(nama1)
panjang2=len(nama2)
panjang3=len(nama3)

if panjang1>panjang2 and panjang1>panjang3:
    print(nama1)
elif panjang2>panjang1 and panjang2>panjang3 :
    print(nama2)
else :
    print(nama3)
