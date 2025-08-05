def toplama(a, b):
    return a+b
def cixma(a, b):
    return a-b
def vurma(a, b):
    return a*b
def bolme(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error: 0-a bolmek mumkun deyil"

print("secmek istediyiniz emeliyyatin nomresini daxil edin")
print("1.toplama")
print("2.cixma")
print("3.vurma")
print("4.bolme")
print("")
try:
    nomre=int(input())
    a=int(input("ilk ededi daxil edin: "))
    b=int(input("ikinci ededi daxil edin: "))
    if nomre==1:
        print("Netice:",toplama(a,b))
    elif nomre==2:
        print("Netice:",cixma(a,b))
    elif nomre==3:
        print("Netice:",vurma(a,b))
    elif nomre==4:
        print("Netice:",bolme(a,b))
    else:
        print("duzgun nomre daxil edin")
except ValueError:
    print("Error: Sadece reqem daxil edin")