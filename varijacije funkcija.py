# VARIJACIJA 1 - DOBAR REZULTAT
def main():
    return(input())

print (main())

# znaci ovde se prvo daje input pa se on napravi da je return od main funkcije. Pa se dole samo printa rezultat main-a
# ovaj nacin za razliku od nacina 2 je bolji jer main uvek kao rezultat daje input, a posle toga mi opcionalno biramo sta cemo da radimo sa tim input-om

#—————————————————————————————————————————————————

# VARIJACIJA 2 - DOBAR REZULTAT
def main(x):
    print(x)


main(input())

# ovde se daje input da se izvrsava main funkcija gde je input argument i samo se printa input
# ovaj nacin za razliku od prvog nacina je bolji u smislu da main uvek printuje svoj argument a posle toga mi opcionalno biramo sta ce da bude taj argument

#—————————————————————————————————————————————————


# VARIJACIJA 3 - DOBAR REZULTAT
def main():
    print(input("?"))

main()

# u ovoj funkciji se sve radi u sklopu main-a, printa se input.
# ova situacija je bolja od ostalih jer ovde se sigurno zna da treba da se input samo odstampa, a na primer kad bih hteo da se nesto da tim input-om uradi,
# --> da se izracuna nesto ili da se bilo sta radi onda je bolja situacija prva. Ako hocemo da nam se uvek stampa a da mi samo jednom za to stampanje unesemo input,
# --> onda je bolja situacija dva.
#fzsdfds
#dgf