def main():
    amount = 50

    while amount>0:

        print(f'Amount Due: {amount}')
        inserted = int(input('insert coin: '))

        if inserted is 10 or inserted is 25 or inserted is 5:
            amount = amount - inserted

    print('Change Owed:', (-1)*amount)

main()
