parolis = 68913564
kļuda = 0
while True:
    turp = int(input("meiginajuma"))
    if turp == parolis:
        print("Piekļuve atļauta")
        break
    else:
        print("nepareizi")
        kļuda = kļuda + 1
    if kļuda == 3:
        print("Piekļuve bloķēta")
        break