# CLI Calculator 
#branching
def play():
    print("Calculator📟")
    print("[➕ ➖ ✖️  ➗]")
    print()
    a=int(input())
    select=input()
    b=int(input())
    if select == "+":
        print("=",a+b)
    elif select=="-":
        print("=",a-b)
    elif select=="*":
        print("=",a*b)
    elif select=="/":
        print("=",a/b)
    else:
        print("wrong input")
play()
