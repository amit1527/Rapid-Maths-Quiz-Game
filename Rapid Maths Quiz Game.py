import random
def main():
    l = get_level()
    score = 0
    for i in range(10):
        x,y = generate_integer(l)
        z = x+y
        num = input(f"{x} + {y} =")
        if num.isdigit() and int(num)== z:
            score += 1
        else:
            attempts = 1
            print("EEE")
            while attempts<3:
                try:
                    num1 = int(input(f"{x} + {y} ="))
                    if num1== z:
                        score+=1
                        break
                    else:
                        print("EEE")
                        attempts +=1
                except ValueError:
                        attempts +=1
            if attempts ==3:
                print(f"{x} + {y} = {z}")
    print(f"Score: {score}")


def get_level():
    while True:
        l = input("Level: ")
        if l.isdigit() and int(l) in range(1,4):
            return int(l)
        else:
            pass

def generate_integer(level):
    if level == 1:
        x= random.randint(0,9)
        y= random.randint(0,9)
    elif level == 2:
        x= random.randint(10,99)
        y= random.randint(10,99)
    elif level == 3:
        x= random.randint(100,999)
        y= random.randint(100,999)
    return x,y


if __name__ == "__main__":
    main()
