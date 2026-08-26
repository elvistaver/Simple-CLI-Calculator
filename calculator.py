# CLI Calculator 
#branching
def calc():
    print("CALCULATOR📟")
    print("___________________________________________________________________________________ ")
    print("✅ Usage:First digit enter, Operation sign[➕ ➖ ✖️  ➗]enter and Second digit enter")
    print("___________________________________________________________________________________ ")
    print("[➕ ➖ ✖️  ➗]")
    print("🀫🀫🀫🀫🀫🀫🀫🀫🀫🀫🀫🀫🀫🀫")
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
calc()
