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
    for i in range(0, numar_el):
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
    for i in range(0, numar_el):
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


def bit_count(n):
    """
    Funtctia calculeaza numarul de biti 1 din scriere parametrului in baza 2
    :param: un numar intreg
    :return: Returneaza un numar intreg ce reprezinta numarul de biti 1 din scriere parametrului in baza 2
    """
    cont = 0
    while n > 0:
        if n % 2 == 1:
            cont+=1
        n//=2
    return cont


assert bit_count(7) == 3
assert bit_count(8) == 1
assert bit_count(17) == 2
assert bit_count(0) == 0


def get_longest_same_bit_counts(l_init, numar_el_bit) -> list[int]:
    """
    Functia determina cea mai lunga secventa de numere care au acelasi numar de biti 1 in scrierea lor
        in baza 2, din lista citita
    Daca exista mai multe secvente de lungime maxima se va afisa prima secventa
    :param l_init: O lista care contine numere intregi
    :param n: Un numar natural nenul
    :return: Se returneaza o alta lista decat cea citita, ce contine secventa ceruta,
        sau None daca nu exista o astfel de secventa
    """
    l_fin = []
    contmax = 0
    cont = 0
    for i in range(0, numar_el_bit):
        if bit_count(int(l_init[i])) > 0:
            if cont == 0:
                cont += 1
            if i > 0:
                if bit_count(int(l_init[i])) == bit_count(int(l_init[i-1])):
                    cont += 1
                else:
                    if cont > contmax:
                        contmax = cont
                    cont = 1
    cont = 0
    for i in range(0, numar_el_bit):
        if bit_count(int(l_init[i])) > 0:
            if cont == 0:
                cont += 1
                l_fin.append(int(l_init[i]))
            if i > 0:
                if bit_count(int(l_init[i])) == bit_count(int(l_init[i-1])):
                    cont += 1
                    l_fin.append(int(l_init[i]))
                else:
                    if cont == contmax:
                        return l_fin
                    cont = 1
                    l_fin.clear()
                    l_fin.append(int(l_init[i]))


def test_get_longest_same_bit_counts():
    assert get_longest_same_bit_counts([0, 1, 2, 4, 6], 5) == [1, 2, 4]
    assert get_longest_same_bit_counts([90, 100, 10, 3, 5, 24, 19], 7) == [10, 3, 5, 24]
    assert get_longest_same_bit_counts([0, 0, 0], 3) is None
    assert get_longest_same_bit_counts([0, 1, 3, 0], 4) == [1]


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
            test_get_longest_same_bit_counts()
            numar_el_bit = int(input("Introducei numarul de elemente din lista: "))
            l_init = []
            for i in range(0, numar_el_bit):
                l_init.append(int(input("l_init[" + str(i) + "]: ")))
            print("Rezultat: ", get_longest_same_bit_counts(l_init, numar_el_bit))


if __name__ == '__main__':
    main()
