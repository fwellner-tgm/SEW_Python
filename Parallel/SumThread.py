
import threading

class ThreadCounter(threading.Thread):
    """
    returns the sum of a number each thread counts to, for example: number = 10, threads = 3 -> sum = 30
    """

    #global counter so every thread can access it (local variables can't be accessed by every thread)
    counter = 1
    #a lock is required to sync threads
    lock = threading.Lock()

    def __init__(self, countTo):
        """
        initialisation method
        :param countTo: the number each thread counts to
        """
        self.countTo = countTo
        threading.Thread.__init__(self)

    def run(self):
        """
        method which runs threads
        """

        for i in range(self.countTo):
            with ThreadCounter.lock:
                print(str(ThreadCounter.counter))
                ThreadCounter.counter += 1

#user defines the number every thread counts to
while True:
    countTo = input("The number each thread counts to: ")
    #input has to be a number
    if countTo.isdigit():
        countTo = int(countTo)
        break

#definies how many threads should be used
while True:
    threadCount = input("How many threads? (default = 3) ")
    #if user enters nothing, default = 3 is used
    if threadCount == "":
        threadCount = 3
        break
    #checks if input is a number
    elif threadCount.isdigit():
        threadCount = int(threadCount)
        break

#list named threads
threads = []

#initialize threads (default = 3) and start them
for i in range(0, threadCount):
    #new thread
    thread = ThreadCounter(countTo)
    #each thread gets individually added to the threads list
    threads += [thread]
    thread.start()

#waits for execution
for x in threads:
    x.join()