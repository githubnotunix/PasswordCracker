"""Cracker Program that bruteforces a password given only the known salt and hash
	Level 1: lowercase letters
	Level 2: " uppercase letters
	Level 3: " " numbers
	Level 4: " " " special characters
	Program is correct if bruteforce(hash(password + salt)) = actual_pw
"""
import hashlib
import time
import string
from brute import brute

#gets salt, hash, and user input
f = open("pwd.txt", "r")
pwd = f.read()
username, salt, hashed_pw = pwd.split(',')
pw_length = int(input('What is the length of the password? '))
level = input(
    'Which level of cracking do you want? (1, 2, 3, 4)\n')

#start of all the levels
if level == '1':
    counter = 0
    start = time.time()
    for x in brute(length = pw_length, letters = True, numbers = False, symbols = False):
        if x.islower():
            counter += 1
            if hashlib.sha256(salt.encode() + x.encode()).hexdigest() == hashed_pw:
                end = time.time()
                print('Found password: ' + x)
                print('%s %d tries' % ('In', counter))
                print('%s %f seconds' % ('Completed in', end-start))
                #print('ONE WORKS')
                break

if level == '2':
    counter = 0
    start = time.time()
    for x in brute(length = pw_length, letters = True, numbers = False, symbols = False):
        counter += 1
        if hashlib.sha256(salt.encode() + x.encode()).hexdigest() == hashed_pw:
            end = time.time()
            print('Found password: ' + x)
            print('%s %d tries' % ('In', counter))
            print('%s %f seconds' % ('Completed in', end-start))
            #print('TWO WORKS')
            break

if level == '3':
    counter = 0
    start = time.time()
    for x in brute(length = pw_length, letters = True, numbers = True, symbols = False):
        counter += 1
        if hashlib.sha256(salt.encode() + x.encode()).hexdigest() == hashed_pw:
            end = time.time()
            print('Found password: ' + x)
            print('%s %d tries' % ('In', counter))
            print('%s %f seconds' % ('Completed in', end-start))
            #print('THREE WORKS')
            break

if level == '4':
    counter = 0
    start = time.time()
    for x in brute(length = pw_length, letters = True, numbers = True, symbols = True):
        counter += 1
        if hashlib.sha256(salt.encode() + x.encode()).hexdigest() == hashed_pw:
            end = time.time()
            print('Found password: ' + x)
            print('%s %d tries' % ('In', counter))
            print('%s %f seconds' % ('Completed in', end-start))
            #print('FOUR WORKS')
            break
