# Python program to illustrate 
# the concept of race condition
# in multiprocessing
import multiprocessing
 
# function to withdraw from account
def withdraw(balance):    
    for _ in range(10000):
        balance.value = balance.value - 1
 
# function to deposit to account
def deposit(balance):    
    for _ in range(10000):
        balance.value = balance.value + 1
 
def perform_transactions():
 
    # initial balance (in shared memory)
    balance = multiprocessing.Value('i', 100)
 
    # creating new processes
    p1 = multiprocessing.Process(target=withdraw, args=(balance,))
    p2 = multiprocessing.Process(target=deposit, args=(balance,))
 
    # starting processes
    p1.start()
    p2.start()
 
    # wait until processes are finished
    p1.join()
    p2.join()
 
    # print final balance
    print("Final balance = {}".format(balance.value))
 
if __name__ == "__main__":
    for _ in range(10):
 
        # perform same transaction process 10 times
        perform_transactions()
