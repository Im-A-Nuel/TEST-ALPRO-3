suhu=float(input("suhu = "))
if suhu >=32 and suhu <=35.99:
    print("bahaya Hipotermia")
elif suhu >=36 and suhu <=37.99:
    print("Normal")
elif suhu >=38 and suhu <=41:
    print("Demam")
else:
    print("Meninggal")


suhu=float(input("suhu = "))
if suhu<32:
    print("Meninggal")
elif 32 <= suhu <= 36:
    print("bahaya Hipotermia")
elif 36 <= suhu <= 38:
    print("Normal")
elif 38 <= suhu <= 41:
    print("Demam")
else:
    print("Meninggal")
