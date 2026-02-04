import csv
import datetime

FAILS = "/Users/evasakalo/programesana/gramatas.csv"
ATLAUTIE_ZANRI = ["romāns", "dzeja", "fantastika", "bērnu literatūra", "detektīvs", "trileris"]


# Palīgfunkcijas

def nolasit_visas_gramatas():
    """Nolasa visas grāmatas no CSV datnes un atgriež sarakstu ar rindām."""
    try:
        with open(FAILS, "r", newline="", encoding="utf-8") as f:
            return list(csv.reader(f, delimiter=";"))
    except FileNotFoundError:
        return []

def ir_dublikats(jauna_gramata, visas_gramatas):
    """Pārbauda, vai jauna grāmata jau ir sarakstā (salīdzina visus laukus)."""
    return jauna_gramata in visas_gramatas


# Datu ievade un validācija 

def ievadit_tekstu(uzdevums):
    """Ievada tekstu un pārbauda, lai tas nav tukšs."""
    teksts = input(uzdevums).strip()
    if teksts == "":
        print("Kļūda: lauks nedrīkst būt tukšs.")
        return None
    return teksts

def ievadit_gadu():
    """Ievada izdošanas gadu un pārbauda, vai tas ir derīgs."""
    try:
        gads = int(input("Ievadi izdošanas gadu: "))
    except ValueError:
        print("Kļūda: gadam jābūt veselam skaitlim.")
        return None

    tagadejais_gads = datetime.datetime.now().year
    if gads < 1900 or gads > tagadejais_gads:
        print("Kļūda: gads jābūt starp 1900 un esošo gadu.")
        return None

    return gads


def ievadit_zanru():
    """Ievada žanru un pārbauda, vai tas ir atļauto žanru sarakstā."""
    zanrs = input("Ievadi žanru (romāns/dzeja/fantastika/bērnu literatūra/detektīvs/trileris): ").strip().lower()
    if zanrs not in ATLAUTIE_ZANRI:
        print("Kļūda: nederīgs žanrs.")
        return None
    return zanrs


def ievadit_gramatu():
    """Ievada vienas grāmatas datus. Ja ir kļūda, atgriež None."""
    nosaukums = ievadit_tekstu("Ievadi grāmatas nosaukumu: ")
    if nosaukums is None:
        return None

    autors = ievadit_tekstu("Ievadi autoru: ")
    if autors is None:
        return None

    gads = ievadit_gadu()
    if gads is None:
        return None

    zanrs = ievadit_zanru()
    if zanrs is None:
        return None

    # Grāmatas dati vienā sarakstā (rinda CSV datnei)
    return [nosaukums, autors, str(gads), zanrs]


# CSV saglabāšana un izvade 

def saglabat_gramatu(gramata):
    """Saglabā grāmatu CSV datnē."""

    visas = nolasit_visas_gramatas()

    # Dublikātu pārbaude
    if ir_dublikats(gramata, visas):
        print("Paziņojums: šāda grāmata jau ir saglabāta (dublikāts).")
        return

    # Saglabāšana CSV datnē
    with open(FAILS, "a", newline="", encoding="utf-8") as f:
        rakstitajs = csv.writer(f, delimiter=";")
        rakstitajs.writerow(gramata)

    print("Grāmata saglabāta veiksmīgi!")



def paradit_gramatas():
    """Izvada konsolē visas grāmatas no CSV datnes."""
    visas = nolasit_visas_gramatas()

    if not visas:
        print("Datne ir tukša vai nepastāv.")
        return

    print("\n--- Grāmatu saraksts ---")
    for i, g in enumerate(visas, start=1):
        print(f"{i}. Nosaukums: {g[0]}, Autors: {g[1]}, Gads: {g[2]}, Žanrs: {g[3]}")


# Galvenā izvēlne 

def izvelne():
    """Galvenā izvēlne (komandrindas interfeiss)."""
    while True:
        print("\n1 - Pievienot grāmatu")
        print("2 - Parādīt visas grāmatas")
        print("3 - Iziet")

        izvele = input("Izvēlies darbību: ").strip()

        if izvele == "1":
            gramata = ievadit_gramatu()
            if gramata is not None:
                saglabat_gramatu(gramata)

        elif izvele == "2":
            paradit_gramatas()

        elif izvele == "3":
            print("Programma beidzas.")
            break

        else:
            print("Kļūda: nederīga izvēle.")


# Programmas starts
izvelne()