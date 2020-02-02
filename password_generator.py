import random


def convert(p):
    str1 = ''
    return str1.join(p)


def pass_gen(p_len):
    p = []
    char_sp = chr(random.randint(33, 47) or random.randint(58, 64)
                  or random.randint(91, 96) or random.randint(123, 126))
    p.append(char_sp)
    char_lower = chr(random.randint(97, 122))
    p.append(char_lower)
    char_upper = chr(random.randint(65, 90))
    p.append(char_upper)
    char_num = chr(random.randint(48, 57))
    p.append(char_num)
    p_len -= 4
    while p_len > 0:
        p.append(chr(random.randint(33, 126)))
        p_len -= 1
    random.shuffle(p)
    pass_str = convert(p)
    return pass_str


while True:
    p_len = int(input("Enter the length of password required: "))
    if(p_len < 6):
        print("\nMinimum number of characters= 6\n\n")
    else:
        break
password = pass_gen(p_len)

print(f"\n\nPassword :  {password}")
