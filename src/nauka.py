def aktualizacja(listadodaj, listausun):
    plik = open("odmm.txt", 'r')
    zawartosc = plik.readlines()
    tabela = []
    zapis = []
    for z in zawartosc:
        if (z.find('''\n''') > 0):
            tabela.append(z[0:(z.find('''\n'''))])


    for a in tabela:
        if a in listausun:
            print("usunalem", a)
            pass
        else:
            zapis.append(a)

    for b in listadodaj:
        print("dodałem", b)
        zapis.append(b)

    pisz = open('odmm.txt', 'w')
    for z in zapis:
        pisz.write("%s\n" % z)


def zrobliste(tabela):  # przekonwertuj string na liste slow
    tabela = tabela[0]
    tabeltalista =  []
    spacje = [-1]
    l = 0
    for a in tabela:  # do list "spacje" dodajemy indeksy na któych znajduja sie \n
        if a == '\n':
            spacje.append(l)
        l += 1
    for b in range(len(spacje) -1): #tworzymy liste dzielac String w miejscach gdzie sa \n
        tabeltalista.append(tabela[spacje[b] + 1:spacje[b + 1]])
        if b == len(spacje)-2:
            tabeltalista.append(tabela[spacje[b+1]+1:len(tabela)])

    for c in tabeltalista:
        for d in c:
            if d == ' ':
                try:
                    tabeltalista.remove(c)
                except:
                    pass
    print("Wynik ze strony", tabeltalista, "\n\n")
    return tabeltalista


def cyfrynaslowa(wykonaj, lista):
    wykonajslowem = wykonaj.copy()
    for a in range(len(wykonajslowem)):
        wykonajslowem[a] = list(wykonajslowem[a])
    for t in range(len(wykonajslowem)):
        for y in range(len(wykonajslowem[t])):
            (wykonajslowem[t])[y] = lista[(wykonajslowem[t])[y]]
    for x in range(len(wykonajslowem)):
        wykonajslowem[x] = ''.join(wykonajslowem[x])
    return wykonajslowem


def dodajusun(wykonajslowem,
              tabelalista):  # stworz 2 listy: słow do usunięcia ze słownika oraz słow do dodania do słownika
    dodaj = []
    usun = []
    for slowo in wykonajslowem:
        if slowo not in tabelalista:
            usun.append(slowo)
    for slowoo in tabelalista:
        if slowoo not in wykonajslowem:
            dodaj.append(slowoo)
    print("Do dodania", dodaj, "\n\n")
    print("Do usunięcia", usun, "\n\n")
    aktualizacja(dodaj, usun)


def nauka(tabela, wykonaj, lista):
    dodajusun(cyfrynaslowa(wykonaj, lista), zrobliste(tabela))


