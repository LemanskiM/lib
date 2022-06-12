def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


A = input("a:")
B = input("b:")
C = input("c:")

if not( check_int(A) and check_int(B) and check_int(C) ):
    print("a, b and c need to be int!")
else:
    A = int(A)
    B = int(B)
    C = int(C)
    if A == 0:
        print("to nie równanie kwadratowe")
    else:
        delta = B*B-(4*A*C)
        if delta < 0:
            print("delta ujemna brak rozwiązania")
        elif delta == 0:
            x1 = (-B-delta**0.5)/(2*A)
            print("%f" %(x1))
        else:
            x1 = (-B-delta**0.5)/(2*A)
            x2 = (-B+delta**0.5)/(2*A)
            print("%f %f" %(x1,x2))
