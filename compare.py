def unos():
    x=int(input("x? "))
    y=int(input("y? "))
    return (x,y)


def compared(m,n):
    if n>m: return n
    if n<m: return m
    if m==n: print("equal")


def main():
    print(compared(*unos()))

main()