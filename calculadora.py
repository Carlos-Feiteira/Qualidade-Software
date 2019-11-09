"""
Carlos Feiteira  nº 16396
Mestrado em Engenharia Informatica
Qualidade de Software


Calculadora cientifica
"""

def allowedOperators(op):
    if "+" in op:
        return True
    elif "-" in op:
        return True
    elif "*" in op:
        return True
    elif "/" in op:
        return True
    elif "**" in op:
        return True
    elif "//" in op:
        return True
    elif "%" in op:
        return True
    else:
        return False

def allowedValues(val):
    if val.isnumeric() is True:
        return True
    else:
        return False

def teststring(val):
    cstr = val.split(" ")
    i = 0
    j = 1
    while i <= cstr.__len__() - 1:
        if allowedValues(cstr[i]) is False:
            return False
        else:
            i += 2

    
    while j <= cstr.__len__() - 1:
        if allowedOperators(cstr[j]) is False:
            return False
        else:
            j += 2   
    return True     



def main():
    s = True
    print("deve sempre haver espaços entre cada um dos elementos das expressões")
    print("inserir 'sair' para terminar")
    while(s):
        x = input()

        if "sair" in x:
            s = False
        
        if teststring(x):
            print("resultado : " + str(eval(x)))
        else:
            print("erro na string")


main()
