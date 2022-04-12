class secret:

    def __init__(self, content, key, mode=0):
        self.content = content
        self.key = key
        self.mode = mode
        self.dict_b36_b10 = {
            '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
            'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22,
            'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33,
            'Y': 34, 'Z': 35
                            }
        self.dict_str_b10 = {32: 29, 39: 30, 44: 31, 46: 32}
        self.dict_b10_str = {29: 32, 30: 39, 31: 44, 32: 46}
        self.str_b10_b36 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def b36_b10(self, str, nb_vide=0):
        for i, c in enumerate(str[::-1]): nb_vide += self.dict_b36_b10[c] * (36 ** i)
        return nb_vide

    def b10_b36(self, nb, str=""):
        while nb != 0:
            str += self.str_b10_b36[nb % 36]
            nb //= 36
        return str[::-1]

    def str_b10(self, str, c=0):
        for a, b in enumerate(str):
            if 97 <= ord(b) <= 122:
                b = ord(b) - 94
            else:
                b = self.dict_str_b10[ord(b)]
            c += b * 34 ** (a + 2)
        return c

    def find_the_repet(self, phrase_, nbrepet=0, nbr_constru=0):
        while nbr_constru < phrase_:
            nbr_constru = 34 ** nbrepet
            nbrepet += 1
        return nbrepet - 2

    def find_the_good(self, power, nb):
        for looping in range(32, 1, -1):
            nb_a_test = looping * 34 ** power
            if nb // nb_a_test == 1: return looping, nb - nb_a_test
        return 0, 0

    def b10_str(self, phr, mot=[], str=""):
        nb = self.find_the_repet(phr)
        while phr != 0:
            resu = self.find_the_good(nb, phr)
            phr = resu[1]
            mot.append(resu[0])
            nb -= 1

        for a in mot[::-1]:
            if 3 <= a <= 28: str += chr(a + 94)
            else: str += chr(self.dict_b10_str[a])
        return str

    def enco(self): self.content, self.mode = self.b10_b36(self.str_b10(self.content) * (self.str_b10(self.key) * len(self.key) ** 5)), 1

    def deco(self): self.content, self.mode = self.b10_str(self.b36_b10(self.content) // (self.str_b10(self.key) * len(self.key) ** 5)), 0

    def show(self): print(self.content)

    def switch(self):
        try:
            self.enco()
            return
        except:
            pass
        try:
            self.deco()
            return
        except:
            pass

    def __str__(self): return self.content
