
def ziValida(prima_cifra_an, a_doua_cifra_an, prima_cifra_luna, a_doua_cifra_luna, prima_cifra_zi, a_doua_cifra_zi):
    zi = ""
    zi += prima_cifra_zi
    zi += a_doua_cifra_zi
    luna = ""
    luna += prima_cifra_luna
    luna += a_doua_cifra_luna
    an = ""
    an += prima_cifra_an
    an += a_doua_cifra_an
    if luna in ["01", "03", "05", "07", "08", "10", "12"]:
        if int(zi) > 31:
            return False
    elif luna == "02":
        if int(an) % 4 == 0:
            if int(zi) > 28:
                return False
        else:
            if int(zi) > 29:
                return False
    else:
        if int(zi) > 30:
            return False
    return True

def isGender(string):
    if string != 0:
        return True

def isMonth(string):
    string = list(string)
    nr = 0
    if int(string[0]) == 0:
        nr = int(string[0]) + int(string[1])
        if nr <= 12:
            return True
        else:
            return False

    elif int(string[0]) == 1:
        nr = int(string[0])*10 + int(string[1])
        if nr <= 12:
            return True
        else:
            return False
    else:
        return False

def cod_judet(prima_cifra, a_doua_cifra):
    nr = ""
    nr += prima_cifra
    nr += a_doua_cifra
    if nr == "00":
        return False
    elif int(nr) > 52:
        return False
    return True

def cod_birouri_de_evidenta(prima_cifra, a_doua_cifra, a_treia_cifra):
    nr = ""
    nr += prima_cifra
    nr += a_doua_cifra
    nr += a_treia_cifra
    if nr == "000":
        return False
    return True

def cifra_de_control(cnp, cifra_control):
    nr = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]

    cnp_list = [int(x) for x in cnp]
    result = [x * y for x, y in zip(nr, cnp_list)]
    if sum(result) % 11 == 10:
        cifra_corecta = 1
    else:
        cifra_corecta = sum(result) % 11
    if cifra_corecta != int(cifra_control):
        return False
    else:
        return True

cnp = input("Introdu CNP-ul tau: ")

cnp_list = list(cnp)

if len(cnp_list) == 13 and isGender(cnp_list[0]) and isMonth(cnp_list[3:5]) and cod_judet(cnp_list[7], cnp_list[8]) and cod_birouri_de_evidenta(cnp_list[9], cnp_list[10], cnp_list[11]) and cifra_de_control(cnp_list, cnp_list[12]):
    print("Your CNP is valid.")
else:
    print("Your CNP is invalid.")
