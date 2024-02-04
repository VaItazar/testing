def main():

    camelCase = input("camelCase: ")
    snake_case = snake_cased(camelCase)

    print("snake_case:", snake_case)



def snake_cased(text):

    for char in text:

        if char.isupper():
            sss = text.replace(char, f'_{char.lower()}')

        else:
            continue

        newsss = sss



    for char in newsss:

        if char.isupper():
            newsss = newsss.replace(char, f'_{char.lower()}')


    return newsss

# checker daje sve :) rezulate ali ove dve for petlje mogu da se spoje da se fuse-uju jer ovo je nepotrebno dve petlje ja mislim

main()