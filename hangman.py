import random


def get_rand_word(min_len):
    words = []
    with open(r"C:\Users\USER\Desktop\PYTHON\Words_hangman.txt", mode='r') as word_file:
        for word in word_file:
            word = word.strip().lower()
            if len(word) < min_len:
                continue
            words.append(word)

    return random.choice(words)


def convert(word_l):
    str1 = ''
    return (str1.join(word_l))


def get_diplay_word(displa, gues, i):
    word_list = []
    for x in range(len(displa)):
        if displa[x] == "*":
            if x != i:
                word_list.append("*")
            else:
                word_list.append(gues)
        else:
            word_list.append(displa[x])
    w = convert(word_list)
    return w


print("Starting a game of Hangman...")
while True:
    num_attempt = input("How many incorrect attempts? (1-25) : ")
    try:
        num_attempt = int(num_attempt)
        if 1 <= num_attempt <= 25:
            print("Selecting a word...")
            break
        else:
            print("Enter a number in range [1-25] !")

    except (TypeError, ValueError) as err:
        print("Enter valid number of attempts!")
        continue

req_word = get_rand_word(num_attempt)
print("\n\n"+req_word+"\n\n")
req_word_len = len(req_word)

display = ('*') * req_word_len
guessed = req_word_len
prev = ''
guess = ''

print(guessed)

while num_attempt > 0 and guessed > 0:
    print("\n\nWord: " + display)
    print(f"Attempts remaining: {num_attempt}")
    print(f'Previous guess: {prev}')
    while True:
        guess = (input("Choose the next letter:"))
        if guess == prev:
            print(f"{guess} has been guessed before!")
        else:
            break
    flag = 0
    for i in range(0, req_word_len):
        if guess == req_word[i]:
            display = get_diplay_word(display, guess, i)
            guessed -= 1
            flag += 1
        else:
            continue

    if flag != 0:
        print(f"{guess} is in the word!")
    else:
        print(f"{guess} is NOT in the word!")
        num_attempt -= 1

    prev = guess

if guessed == 0:
    print("You Win!")

elif num_attempt == 0:
    print("You lose! You've run out of attempts!")

print(f"\n \n Word : {req_word}")
