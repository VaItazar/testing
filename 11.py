def square():
    return print("Tvoj br^2 je:",round(float(input("koji je tvoj broj? "))**2, 3))

def cao():
    return print("Cao,", input("Kako se zoves? ").title().strip())

def main():
    print("Welcome.")
    square()
    cao()
    
# koristim pozivanje obe funkcije jer ne moze da se returnuju obe funkcije, moze samo jedna


main()


 # ----- Kako kod moze da izgleda kada bih pozivao funkcije sa drugim argumentom: -----

def square1(n):
    print("Tvoj br^2 je:",n)

def cao1(name):
    print("Cao,",name)

def main1():
    ime=input("Kako se zoves opet? ")
    x=int(input("koji je tvoj drugi broj? "))
    square1(x**2)
    cao1(ime)

main1()