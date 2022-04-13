import string
import random


LETTERS=string.ascii_letters
NUMBERS=string.digits
PUNCTUATIONS=string.punctuation


def pass_generator(length=8):
    ALL=f"{LETTERS}{NUMBERS}{PUNCTUATIONS}"
    ALL=list(ALL)
    random.shuffle(ALL)
    random_pass=random.choices(ALL,k=length)
    random_pass=''.join(random_pass)
    return random_pass

def number_characters():
    while True:
        length=input("Please enter length of password:")
        if int(length)>=8:
            return int(length)
            
        else:
            print('Length of password must >=8!!!!!')
            continue

def main():
    l=number_characters()
    password=pass_generator(l)
    print(f"Your password:{password}")



if __name__=="__main__":
    main()