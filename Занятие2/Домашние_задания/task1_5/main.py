from string import ascii_lowercase, ascii_uppercase, digits
from random import sample

if __name__ == "__main__":
    # print(ascii_lowercase)
    # print(ascii_uppercase)
    # print(digits)
    our_bank = str(ascii_lowercase + ascii_uppercase + digits)
    our_bank_list = [i for i in our_bank]
    gener = sample(our_bank_list, 8)
    gener_str = ''.join(gener)
    # no_commas = gener_str.replace(', ', '')
    # print(no_commas)
    print(gener_str)
