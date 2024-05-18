cenaMleka=int(input("Unesi cenu mleka u dinarima"))
kolicinaMleka=int(input("Unesi kolicinu mleka"))
daoNovca=int(input("Platite u eurima"))
daoNovcaUDinarima=daoNovca*117.12
racun= cenaMleka * kolicinaMleka
if(daoNovcaUDinarima>racun):
    print("Kusur je",daoNovcaUDinarima-racun)
else:
    print("Niste dali dovoljno para")
