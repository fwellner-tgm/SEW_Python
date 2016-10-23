"""
@Autor: Florian Wellner
@Datum: 2016-10-10
@Zweck: Thread
"""
import threading
import random


def getMessage():
    while True:
        message = input("Enter a message you want to encrypt: \n")
        if len(message) < 1:
            print("Too short!")
        else:
            return message.lower()

def getRandom():
    return random.randint(0,10)

class ThreadEncrypt(threading.Thread):

    def __init__(self, begin, end):

        threading.Thread.__init__(self)
        self.begin = begin
        self.end = end

    def run(self):
        self.chooseMode()

    def chooseMode(self):
        while True:
            mode = input("1 = encrypt" + "\n" + "2 = decrypt" + "\n" + "0 = exit" + "\n")
            if mode.isdigit() and int(mode) >= 0 and int(mode) <= 2:
                if int(mode) == 1:
                    self.encrypt()
                elif int(mode) == 2:
                    self.decrypt()
                elif int(mode) == 0:
                    quit()
            else:
                print("Only 1,2 and 0 is acceptable!")

    def encrypt(self):
        threads = []
        message = getMessage()
        number_of_threads = input("How many threads should be used?" + "\n")
        for i in range(0, int(number_of_threads)):
            start = self.begin
            stop = self.end
            threads.append(message[start:stop])
        for i in message:
            if i != " ":
                message = message.replace(i, chr(ord(i) + getRandom()))
        print("Encrypted message: " + message.upper())
        self.chooseMode()

    def decrypt(self):
        message = input("What do you want to decrypt?" + "\n")
        for i in message:
            if i != " ":
                message = message.replace(i, chr(ord(i) - getRandom()))
        print("Decrypted message: " + message.upper())
        self.chooseMode()

swag = ThreadEncrypt(1,3)
swag.start()