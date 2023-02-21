#input
ubin1= int(input('Masukan jumlah ubin 1 : '))
ubin5= int(input('Masukan jumlah ubin 5 : '))
panjang= int(input('Masukan panjang lantainya : '))

#proses
if panjang <= (ubin1*1 + ubin5*5):
    if (panjang // 5) <= ubin5 and (panjang%5==0):
        print('bisa')
    elif (panjang % 5) <= ubin1 :
        print('Bisa')        
else:
    print((panjang % 5 <=ubin1),'Tidak bisa')


# def make_bricks(small, big, goal):
#       if goal > small + big * 5:
#         return False
#       else:
#         return goal % 5 <= small
    
# print(make_bricks(3,1,8))
