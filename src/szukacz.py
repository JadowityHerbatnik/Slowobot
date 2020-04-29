import itertools
import nauka

listaliter = []
malelitery = []
wynik = []
listaslow = []


def indeksyliter(litera):  # sprawdź które klocki zawierają daną literę
    indeksy = []
    for a in range(16):
        if listaliter[a] == litera.upper():
            indeksy.append(a)
    return indeksy


def wspolrzedne(i):  # przeliczenie indeksu litery na wspolrzedne na planszy (początek w punkcie [1,1])
    wspa = (i % 4)
    wspb = (i // 4)
    wspolrzedne = [wspa, wspb]
    return wspolrzedne


def czysasiad(ind1, ind2):  # czy dwa klocki o podanych wspolrzednych sasiaduja ze soba (bokiem albo rogiem)
    wsp = wspolrzedne(ind1)
    wsp2 = wspolrzedne(ind2)
    odleglosc = ((wsp[0] - wsp2[0]) ** 2 + (wsp[1] - wsp2[1]) ** 2) ** 0.5
    if odleglosc <= 2**0.5:
        return True
    else:
        return False


def przygotowanie(listaliter):
    malelitery.clear()
    listaslow.clear()
    for x in listaliter:
        malelitery.append(x)
    plik = open("odmm.txt", "r", encoding='utf-8')
    for p in plik:
        listaslow.append(p.strip())


def wszystkeislowa():  # wszystkie mozliwe do zbudowania slowa z liter na planszy (niekoniecznie sasiadujacych)
    wynik.clear()
    for l in listaslow:
        string = str(l)
        listar = malelitery.copy()
        for a in range(len(string)):
            if not (string[a] in listar):
                break
            else:
                listar.remove(string[a])
                if a == (len(string) - 1):
                    wynik.append(string)
    return wynik


def czymozliwe(wynik):  # ktore sposrod wszystkich slow mozna zbudowac z sasiadujacych bloczkow
    wynikostateczny = []

    for slowo in wynik:
        listaslowa = []
        for a in slowo:
            listaslowa.append(indeksyliter(a))
        kombinacje = list(itertools.product(*listaslowa))
        # kombinacje to wszystkie mozliwosci stworzenia slowa na planszy (niekoniecznie z sasiadujacych bloczkow)
        for k in kombinacje:
            for x in range(len(k) - 1):
                if (czysasiad(k[x], k[x + 1])) == False:
                    break
                else:
                    if x == (len(k) - 2):
                        wynikostateczny.append(k)
    for x in wynikostateczny:
        if len(x) != len(set(x)):
            wynikostateczny.remove(x)
    return wynikostateczny


def usunduplikaty(wynikostateczny):  # usun dupliakty slow
    usunieteduplikaty = []
    for x in wynikostateczny:
        if len(x) != len(set(x)):
            pass
        else:
            usunieteduplikaty.append(x)

    porzadek = sorted(usunieteduplikaty, key=lambda l: (len(l), l), reverse=True)

    tuplenaliste = [] # tuple cyfr przekonwertowane na liste slow (aby usunac duplikaty slowne)
    porzadekcyframi = [] # po usunieciu duplikatow slownych, konwertujemy z powrotem na cyfry

    for z in range(len(porzadek)):
        tuplenaliste.append(list(porzadek[z]))
    for t in range(len(tuplenaliste)):
        for y in range(len(tuplenaliste[t])):
            (tuplenaliste[t])[y] = listaliter[(tuplenaliste[t])[y]]
    porzadekcyframi.append(porzadek[0])
    for u in range(len(tuplenaliste)):
        for z in range(u):
            if tuplenaliste[u] == tuplenaliste[u - z - 1]:
                break
            else:
                if z == u - 1: # czyli jeśli u-z-1 == 0
                    porzadekcyframi.append(porzadek[u])
    literami = nauka.cyfrynaslowa(porzadekcyframi, listaliter)
    print("Znalezione w słowniku", literami, "\n\n")
    return porzadekcyframi


def konwerstujnaslowa(lista):
    global listaliter
    listaliter = lista.copy()
    przygotowanie(listaliter)
    wynikostateczny = usunduplikaty(czymozliwe(wszystkeislowa()))
    return wynikostateczny


