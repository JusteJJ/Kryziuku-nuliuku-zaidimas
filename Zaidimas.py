def Zaidimas():
    lentele = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    SkaiciuMasyvas = [2, 7, 6, 9, 5, 1, 4, 3, 8]

    def PrintLentele():
        print()
        print('', lentele[0], "|", lentele[1], "|", lentele[2])
        print("---|---|---")
        print('', lentele[3], "|", lentele[4], "|", lentele[5])
        print("---|---|---")
        print('', lentele[6], "|", lentele[7], "|", lentele[8])
        print()

    def GautiSkaicius():
        while True:
            skaicius = input()
            try:
                skaicius = int(skaicius)
                if skaicius in range(1, 10):
                    return skaicius
                else:
                    print("\nSkaičiaus nėra tarp pasirinkimų")
            except ValueError:
                print("\nĮvedėte ne skaičių, bandykite dar kartą.")
                continue

    def Ejimas(zaidejas):
        indeksuojama_vieta = GautiSkaicius() - 1
        if lentele[indeksuojama_vieta] == "X" or lentele[indeksuojama_vieta] == "O":
            print("\nLangelis jau užimtas. Pasirinkite kitą langelį")
            Ejimas(zaidejas)
        else:
            lentele[indeksuojama_vieta] = zaidejas

    def TikrintiLaimejima(zaidejas):
        count = 0

        for x in range(9):
            for y in range(9):
                for z in range(9):
                    if x != y and y != z and z != x:
                        if lentele[x] == zaidejas and lentele[y] == zaidejas and lentele[z] == zaidejas:
                            if SkaiciuMasyvas[x] + SkaiciuMasyvas[y] + SkaiciuMasyvas[z] == 15:
                                print("Žaidėjas", zaidejas, "laimėjo!\n")
                                return True

        for a in range(9):
            if lentele[a] == "X" or lentele[a] == "O":
                count += 1
            if count == 9:
                print("Žaidimas baigėsi lygiosiomis\n")
                return True

    while not end:
        PrintLentele()
        end = TikrintiLaimejima("O")
        if end == True:
            break
        print("Parinkite langelį žaidėjui X")
        Ejimas("X")

        PrintLentele()
        end = TikrintiLaimejima("X")
        if end == True:
            break
        print("Parinkite langelį žaidėjui O")
        Ejimas("O")


Zaidimas()
