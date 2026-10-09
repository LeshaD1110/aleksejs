try:
    total = 0
    n = int(input("ievada veselu pozitīvu skaitli"))
    for i in range (1, n + 1):
        total = total + i
        print (f"skaitlis no 1 lidz n ir{total}")
except ValueError:
    print("jus ievada nepareizo skaitļu")

