try:
    skaitlis = int(input("cik skaitlis grib?"))
    if skaitlis <= 0:
        print("Kļuda nevar but mazak 0")
    else:
        for i in range (skaitlis):
            skaitlis = int(input(f"Ievadi {i + 1} skaitlis"))
            if i == 0:
                mazakais = skaitlis
                lielakais = skaitlis
            else:
                if skaitlis < mazakais:
                    mazakais = skaitlis
                if skaitlis > lielakais:
                    lielakais = skaitlis
        print(f"mazakais skaitlis{mazakais}")
        print(f"lielkais skaitlis{lielakais}")
except ValueError:
    print("Kļuda ievadita nederiga skaitļa")

        

    