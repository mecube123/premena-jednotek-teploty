# toto je program na prevod fahrenheitu na stupne a naopak

# rovnica C na F: F = (9*C/5)+32
# rovnica F na C: C = 5*(F-32)/9


while True:
    try:
        otazka = int(input("co chcete premenit? (1 = fahrenheity na stupne; 2 = stupne na fahrenheity) ")) 
        if otazka == 1:
            F = int(input("pocet fahrenheitu: ")) # F - fahrenheit
            F_minus_tridsatdva = F-32
            C = 5*F_minus_tridsatdva/9
            print(C)
        elif otazka == 2:
            C = int(input("pocet stupnu celsia: ")) # S - stupen
            C_plus_tridsatdva = C+32-C
            F = 9*C//5+C_plus_tridsatdva
        else:
            print("spatne cislo")
    except ValueError:
        print("HEJ!!! JENOM cislo napis!")
