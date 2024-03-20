def main():
    t=input("Camel case: ")
    print ("snake_case: ", end="")
    
    for c in t:
        if c.isupper() :
            c=c.lower()
            print("_"+c, end="")
        else:
            print (c, end="")

main()