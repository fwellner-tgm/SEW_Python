"""
@Autor: Florian Wellner
@Datum: 2016-10-24
@Zweck: Thread
"""
import threading
import random

class Crypt():

    def __init__(self):
        threading.Thread.__init__(self)

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
        """
        User is asked how many threads are used to encrypt and adds a part of that to the threads list
        :return:
        """
        threads = []
        result = ""
        while True:
            message = input("Enter a message you want to encrypt: \n")
            if len(message) < 1:
                print("Too short!")
            else:
                break

        while True:
            number_of_threads = input("How many threads should be used?" + "\n")
            if number_of_threads.isdigit() and int(number_of_threads) <= len(message) and int(number_of_threads) > 0:
                number_of_threads = int(number_of_threads)
                break
            else:
                print("Not a valid number!")

        for i in range(0, int(number_of_threads)):
            begin = i * int(len(message) / number_of_threads)
            end = begin + int(len(message) / number_of_threads)
            threads.append(ThreadEncrypt(message[begin:end]))

        for t in threads:
            t.start()
            result += t.result
            t.join()

    def decrypt(self):
        """
        User is asked how many threads are used to decrypt and adds a part of that to the threads list
        :return:
        """
        threads = []
        result = ""
        while True:
            message = input("Enter a message you want to decrypt: \n")
            if len(message) < 1:
                print("Too short!")
            else:
                break

        while True:
            number_of_threads = input("How many threads should be used?" + "\n")
            if number_of_threads.isdigit() and int(number_of_threads) <= len(message) and int(number_of_threads) > 0:
                number_of_threads = int(number_of_threads)
                break
            else:
                print("Not a valid number!")

        for i in range(0, int(number_of_threads)):
            begin = i * int(round(len(message) / number_of_threads))
            end = begin + int(round(len(message) / number_of_threads))
            threads.append(ThreadDecrypt(message[begin:end]))

        for t in threads:
            t.start()
            result += t.result
            t.join()

def getRandom():
    """
    'Random' number between 1 and 10
    :return int:
    """
    return random.randint(1, 10)

random_number = getRandom()

class ThreadEncrypt(threading.Thread):
    def __init__(self, message):

        threading.Thread.__init__(self)
        self.result = ""
        self.message = message

    def run(self):
        """
        Executed when thread gets started with thread.start()
        :return:
        """
        encrypted = ""
        for c in self.message:
            if c != " ":
                encrypted += chr(ord(c.lower()) + random_number)
            else:
                encrypted += " "
        print("Encrypted message: " + encrypted.upper())

class ThreadDecrypt(threading.Thread):

    def __init__(self, message):
        threading.Thread.__init__(self)
        self.result = ""
        self.message = message

    def run(self):
        """
        Executed when thread gets started with thread.start()
        :return:
        """
        decrypted = ""
        for c in self.message:
            if c != " ":
                decrypted += chr(ord(c.lower()) - random_number)
            else:
                decrypted += " "
        print("Decrypted message: " + decrypted.upper())


c = Crypt()