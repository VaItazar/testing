def square():
    print("Tvoj br^2 je:",round(float(input("koji je tvoj broj? "))**2, 3))

def cao():
    print("Cao,", input("Kako se zoves? ").title().strip())

def main():
    print("Welcome.")
    square()
    cao()
    
# koristim pozivanje obe funkcije jer ne moze da se returnuju obe funkcije, moze samo jedna


main()


 # ----- Kako kod moze da izgleda kada bih pozivao funkcije sa drugim argumentom: -----

def square1():
    return int(input("koji je tvoj drugi broj? "))**2

def cao1():
    return input("Kako se zoves opet? ")


def main1():
    print("Tvoj br^2 je:",square1())
    print("Cao,",cao1())

main1()