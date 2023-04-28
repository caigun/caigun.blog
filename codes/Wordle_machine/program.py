with open(r"D:\coding files\LaTeX\DDA2001\TP\words.txt") as f:
    words = f.read().split()
words.sort()

import itertools as it

# 0 means grey - wrong guess;
# 1 means yellow - wrong position;
# 2 means green - correct position.
cart = "012"*5

choice = []
for e in it.combinations(cart, 5):
    count_1 = 0
    count_2 = 0
    for i in e:
        if i == "2":
            count_2 += 1
        if i == "1":
            count_1 += 1
    if not (count_1 == 1 and count_2 == 4):
        choice.append("".join(e))

choice = list(set(choice))
choice.sort()

# This is the implimentation of a simple Wordle game.

import re


def check_answer(answer:str, guess:str):
    
    # answer is the correct word of today's wordle;
    # guess is the user's guess in this attempt
    
    # this function will return one of the patten in the list choice.
    
    ans = "00000"
    used = "00000" # this is to pin the letter that already used
    
    # check the letter at the correct position
    for i in range(5):
        if guess[i] == answer[i]:
            ans = ans[:i]+"2"+ans[i+1:]
            used = used[:i]+"1"+used[i+1:]
    
    # check the letter at the wrong position
    for i in range(5):
        if ans[i] == "2":continue
        for j in range(5):
#             if guess[i] == answer[j] and used[j] == "0":
#                 ans = ans[:i]+"1"+ans[i+1:]
#                 used = used[:j]+"1"+used[j+1:]
            if guess[i] == answer[j] and used[j] == "0":
                ans = ans[:i]+"1"+ans[i+1:]
            
    return ans


def check_valid(p_pattern):
    
    # this function is for regular expression to validate the input.
    
    while True:
        string = input('Enter a guess:')
        if re.match(p_pattern, string):
            return string
        else:
            print('Invalid input! Try again.')
            

def print_board(history:list):
    
    # history is a list consist of tuples:
    # history = [(first guess, first board pattern), (second guess, second board pattern), ...]
    
    # this function will print the UI of the game board
    # for the board pattern, "_" means grey, "+" means yellow, "$" means green
    # refer to the color description for details
    
    for board in history:
        print(board[0])
        for i in board[1]:
            if i == "0":
                print("_", end = '')
            elif i == "1":
                print("+", end = '')
            else:
                print("$", end = '')
        print()
    
    
def play_game(answer:str):
    
    # answer is the correct word
    
    # this function will initialize the game and allow the player to play.
    
    pattern = "00000"
    attempt = 0
    history = []
    avalible_words = words[:]
    
    while pattern != "22222" and attempt <= 6:
        attempt += 1
        guess = check_valid(r"^[a-zA-Z]{5}$")
        pattern = check_answer(answer, guess)
        history.append((guess, pattern))
        print_board(history)
    
    if pattern == "22222":
        print("Congrats! You Win! Total attempts: {0}".format(attempt))
    else:
        print("Out of attempts!")

import math

def calculate_information(_avalible_words:list):
    
    # this function is to calculate the information of choosing any word in the avalible_words list
    # avalible_words is a list containing all the words that satisfying the criteria
    # this function will return a list of all the information of choosing the word as the next guess respectively.
    
    global words
    
    n = len(_avalible_words)
    Information_word = {}
    
    for wd in words:
        
        I = {}
        for pattern in choice:
            I[pattern] = 0
            
        for wd1 in _avalible_words:
            pattern = check_answer(wd1, wd)
            I[pattern] += 1
        
        p = I.values()
        information = sum([-math.log(i/n,2)*(i/n) for i in p if i != 0])
        Information_word[wd] = information
        
    return Information_word
        
    

# def take_guess(history:list, _avalible_words:list):
    
#     # this function is to combine all the hints from the previous guess
#     # and will return the next guess will largest information
    
#     # history is a list consist of tuples:
#     # history = [(first guess, first board pattern), (second guess, second board pattern), ...]
#     # avalible_words is all the avalible words of the last guess
#     # if this is the first guess, then the avalible_words are the whole word list
    
#     last_guess = history[-1]
#     avalible = check_avalible(last_guess[0], last_guess[1], _avalible_words[:])
    
    

    
def check_avalible(guess:str, pattern:str, _avalible_words:list):

    # this function will check the avalibility of the words in the word list
    # according to the guess and the result shown on the board

    # check the letter that will no longer appear in the rest of the blank (besides the correct guesses)
    no_letter = []
    for i in range(5):
        if pattern[i] == "0":
            no_letter.append(guess[i].lower())
            no_letter.append(guess[i].upper())
    
#     print(no_letter)
    
    new_avalible_words = []
    for wd in _avalible_words:
        ava = True
#         print(re.match(no_letter, wd) == True)
#         if re.match(no_letter, wd) == True:
#             new_avalible_words.append(wd)
        for i in range(5):
            if pattern[i] != "2" and wd[i] in no_letter:
                ava = False
        if ava == True:
            new_avalible_words.append(wd)
    
    _avalible_words = new_avalible_words[:]
    new_avalible_words = []
    
    # check the letter that at the correct position
    yes_letter = "00000"
    wrong_letter = "00000"
    for i in range(5):
        if pattern[i] == "2":
            yes_letter = yes_letter[:i]+guess[i]+yes_letter[i+1:]
        elif pattern[i] == "1":
            wrong_letter = wrong_letter[:i]+guess[i]+wrong_letter[i+1:]
            
    for wd in _avalible_words:
        ava = True
        for i in range(5):
            if yes_letter[i] != "0" and wd[i] != yes_letter[i]:
                ava = False
                break
            elif wrong_letter[i] != "0" and wd[i] == wrong_letter[i]:
                ava = False
                break
        if ava == True:
            new_avalible_words.append(wd)
                
    _avalible_words = new_avalible_words[:]
    new_avalible_words = []
    
    # check the letters exist, but at the wrong position
    for wd in _avalible_words:
        ava = True
        charactors = []
        for i in range(5):
            if pattern[i] == "2":
                continue
            else:
                charactors.append(wd[i])
        for i in range(5):
            if pattern[i] == "1" and guess[i] not in charactors:
                    ava = False
        if ava == True:
            new_avalible_words.append(wd)
    
    # here we obtain the list new_avaliblie_words containing all the words satisfying the condition.
    return new_avalible_words

def existing_words_first(all_words:list, existing_words:list):

    # this function is to try to return the guess that has the maximun information that in the existing word list
    # if there are many words containing same information, this function will priorly return words in the
    # existing words. If the existing words are not the words with largest information, then just simply return
    # the word with largest information.

    # all_words is the word list with information.
    # existing_words is the existing words that can be the answer.

    i = 0
    exist = [all_words[i][0]]
    while all_words[i][1] == all_words[i+1][1]:
        exist.append(all_words[i][0])
        i += 1
    for wd in existing_words:
        if wd in exist:
            return wd, all_words[0][1]
    return exist[0], all_words[0][1]

def wordle_machine_ui():

    # this function is to call the UI for users to get the best guess

    # The result for the first guess is already calculated and stored in the file "First_Guess.txt"
    with open(r"LaTeX\DDA2001\TP\FIRST_GUESS.txt") as f:
        first_guess_information = {}
        for line in f:
            wd, information_value = line.split()
            first_guess_information[wd] = float(information_value)

    aval = sorted(first_guess_information.items(), key=lambda item: item[1], reverse=True)
    print("Suggested first guess: {0}".format(aval[0][0]))

    lis = [i[0] for i in aval]
                                    
    while True:
        new_guess = check_valid(r"^[a-zA-Z]{5}$")

        # guess_result = check_answer(ans, new_guess)
        # print(guess_result)

        guess_result = check_valid(r"^[012]{5}$")

        lis = check_avalible(new_guess, guess_result, lis)
        print("Possible word count: {0}".format(len(lis)))
        print(lis)
        if len(lis) == 1:
            print("The answer is {0}".format(lis[0]))
            break
        new = sorted(calculate_information(lis).items(), key=lambda item: item[1], reverse = True)
        guess, information = existing_words_first(new, lis)
        print("The suggested guess is: {0}, the information of choosing this word is: {1:.4f}".format(guess, information))

def wordle_machine_test(correct_word:str):
    
    # this function is to call the UI for users to get the best guess

    # The result for the first guess is already calculated and stored in the file "First_Guess.txt"
    with open(r"LaTeX\DDA2001\TP\FIRST_GUESS.txt") as f:
        first_guess_information = {}
        for line in f:
            wd, information_value = line.split()
            first_guess_information[wd] = float(information_value)

    aval = sorted(first_guess_information.items(), key=lambda item: item[1], reverse=True)
    new_guess = aval[0][0]

    lis = [i[0] for i in aval]
    iter = 1
                                    
    while True:
        guess_result = check_answer(correct_word, new_guess)
        if guess_result == "22222":
            return iter
        lis = check_avalible(new_guess, guess_result, lis)
        if len(lis) == 1:
            return iter+1
        new = sorted(calculate_information(lis).items(), key=lambda item: item[1], reverse = True)
        new_guess = existing_words_first(new, lis)[0]
        iter += 1

# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_quality(data_csv:str):
    attempt = []
    df = pd.read_csv(data_csv)
    for _wd in df["answer"]:
        if _wd.lower() not in words:
            print("Word not found: {0}".format(_wd))
            attempt.append(7)
            continue
        print(_wd.lower(), end = ' Attempt = ')
        wd_test_attempt = wordle_machine_test(_wd.lower())
        attempt.append(wd_test_attempt)
        print(wd_test_attempt)
    return attempt

wordle_machine_ui()

# result = test_quality(r"D:\coding files\LaTeX\DDA2001\TP\History answer.csv")
# plt.hist(result, bins = [0,1,2,3,4,5,6,7,8], density=True)
# print(result)
# plt.show()