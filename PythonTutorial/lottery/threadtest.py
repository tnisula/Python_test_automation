#
#    Thread follows directory
#

# Importoidut modulit
import threading
import os
import time
import datetime

# exitflag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
      
    def run(self):
        print("Starting " + self.name)
        observeDirectory(self.name)
        print("Exiting " + self.name)


def observeDirectory(threadName):
    print("observeDirectory start!")
    while True:
        time.sleep(15)
        for root, dirs, files in os.walk("./logitus"):
            for name in files:
                print(name)
                if(name == "filu.txt"):
                    stamp = time.time()
                    os.rename(root+"/filu.txt", root+"/filu_" + str(stamp) + ".txt")
    print("observeDirectory stop!")

# Main program here

thread1 = myThread(1, "FollowDir")

thread1.start()
thread1.join()

# print("Thread is finished!")
