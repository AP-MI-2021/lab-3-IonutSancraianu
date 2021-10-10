def is_palindrome(n) -> bool:
    """
    Functia determina daca un numar este palindrom sau nu
    Metoda: verificarea elemtelor simetrice din lista, in functie de mijlocul listei
    :param n: variabila de tip string ce poate contine un numar
    :return: True daca elementul este palindrom, False daca nu este palindrom
    """
    le = len(n)
    for i in range(0, le // 2):
        if len(n) % 2 == 1:
            if n[i] != n[le-i-1]:
                return False
        elif n[i] != n[le-i-1]:
            return False
    return True


assert is_palindrome("121") is True
assert is_palindrome("12345") is False
assert is_palindrome("12344321") is True
assert is_palindrome("12") is False
assert is_palindrome("4") is True


def get_longest_all_palindromes(l_init, numar_el):
    """
    Functia determina cea mai lunga secventa de numere palindrom din lista citita
    Daca exista mai multe secvente de lungime maxima se va afisa prima secventa
    :param l_init: O lista care contine numere intregi
    :param n: Un numar natural nenul
    :return: Se returneaza o alta lista decat cea citita, ce contine secventa ceruta,
        sau False daca nu exista secventa ceruta
    """
    contmax = 0
    cont = 0
    for i in range(0, len(l_init)):
        if is_palindrome(str(l_init[i])):
            cont += 1
        else:
            cont = 0
        if cont > contmax:
            contmax = cont
    cont = 0
    l_fin = []
    if contmax == 0:
        return None
    for i in range(0, len(l_init)):
        if is_palindrome(str(l_init[i])):
            cont += 1
            l_fin.append(int(l_init[i]))
        else:
            cont = 0
            l_fin.clear()
        if cont == contmax:
            return l_fin
    l_init.clear()


def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([12, 121, 1331, 56765, 1234], 5) == [121, 1331, 56765]
    assert get_longest_all_palindromes([12, 76, 45, 89], 4) is None
    assert get_longest_all_palindromes([678, 78, 3, 111], 4) == [3, 111]
    assert get_longest_all_palindromes([100, 293, 69], 3) is None


def main():
    shouldRun = True
    while shouldRun:
        print("Alegeti optiunea 1 sau 2 in functie de exercitiul ales"
              " sau x daca doriti sa iesiti")
        optiune = input("Scrieti optiunea: ")
        if optiune == "x":
            shouldRun = False
        if optiune == "1":
            test_get_longest_all_palindromes()
            numar_el = int(input("Introducei numarul de elemente din lista: "))
            l_init = []
            for i in range(0, numar_el):
                l_init.append(input("l_init[" + str(i) + "]: "))
            print("Rezultat: ", get_longest_all_palindromes(l_init, numar_el))
        if optiune == "2":
            print("N-avem inca")


if __name__ == '__main__':
    main()
