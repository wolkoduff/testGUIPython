dva = 0
odin = 0
otvet = 0

while True:
    try:
        odin=int(input("введите 1 число: "))
        dva=int(input("введите 2 число: "))
        znak=input("введите знак(/,*,+,-,^,max,min): ")
        #print(dva)
        #print(odin)
        #print(znak)
        if znak == '/':
            otvet = odin / dva
        elif znak == '*':
            otvet = odin * dva
        elif znak == '+':
            otvet = odin + dva
        elif znak == '-':
            otvet = odin - dva
        elif znak == '^':
            otvet = pow(odin, dva)
        elif znak == 'max':
            otvet = max(odin,dva)
        elif znak == 'min':
            otvet = min(odin,dva)
        elif znak == "q" or odin == "q" or dva == 'q':
            break
        else:
            print("Неверный знак!!!!")
        print(otvet)
    except Exception as ex:
        #print("Это было не число")
        print(str(ex))