def main():
    amount = 50

    while True:

        inserted = int(input('insert coin: '))

        if inserted is 10 or inserted is 25 or inserted is 5:
            amount = amount - inserted
            if amount <=0:
                print('Change Owed:', (-1)*amount)
                break
            print(f'Amount Due: {amount}')

        else:
            print(f'Amount Due: {amount}')


main()
