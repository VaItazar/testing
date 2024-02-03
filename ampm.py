def main():

    time = input("What time is it? ")
    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")



def convert(old_time):

    x,y = old_time.strip().split(' ', 1)
        # --> "1:45" "p.m"
    
    hours, minutes = x.strip().removeprefix('0').split(':',1)
        # --> "1" "45"
    
    float_time = (1/60)*float(minutes) + float(hours)

    if 'p' in y:
        float_time += 12

    return float_time


if __name__ == "__main__":
    main()
