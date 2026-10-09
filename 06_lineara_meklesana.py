skaitli = [4, 7, 2, 9, 7, 1]
try:
    skaitlis = int(input('ievada skaitlis kuru mekle'))
    for i in range (len(skaitli)):
        if skaitli[i] == skaitlis:
            atr_indeks = i + 1
            print(f"indeks {atr_indeks}")
        if skaitlis != skaitli:
            print(f"nav skaitļa {skaitlis}")
except ValueError:
    print("ķluda skaitlis ir ne derigs")

