def unos():
    x=int(input("x? "))
    y=int(input("y? "))
    return (x,y)


def compared(m,n):
    if n>m: return n
    elif n<m: return m
    elif m==n: return "equal"


def main():
    print(compared(*unos()))

main()