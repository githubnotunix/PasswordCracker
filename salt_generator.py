""" Generates random salt and hash(password + hash)
"""
import random
import string
import hashlib

username = input('Enter a username: ')
pw = input('Enter a password: ')

def hash_pw(pw):
    salt = ''.join(
        [random.choice(string.ascii_letters + string.digits) for n in range(10)])

    return hashlib.sha256(salt.encode() + pw.encode()).hexdigest() + ':' + salt


def hashed_pw(pw_hash):
    pw, salt = pw_hash.split(':')
	
    return pw


def get_salt(pw_hash):
    pw, salt = pw_hash.split(':')
    return salt
	
pw_hash = hash_pw(pw)
print('\nUsername: ' + username)
print('Password: ' + pw)
print('Salt: ' + get_salt(pw_hash))
print('Hash from password + salt: ' + hashed_pw(pw_hash))
pwdFile = open("pwd.txt", "w")
pwdFile.write(username + ',' + get_salt(pw_hash) + ',' + hashed_pw(pw_hash))