a=int(input('Masukan a :'))
b=int(input('Masukan b :'))
c=int(input('Masukan c :'))
total=0
if a!= b and a!=c and b!=c:
    total=a+b+c
elif a==b and a==c and b==c :
    total=c
elif a==b:
    total=c
elif a==c:
    total=b
else:
    total=a
