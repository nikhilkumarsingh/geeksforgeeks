# importing the multiprocessing module
import multiprocessing
 
def print_cube(num):
    """
    function to print cube of given num
    """
    print("Cube: {}".format(num * num * num))
 
def print_square(num):
    """
    function to print square of given num
    """
    print("Square: {}".format(num * num))
 
if __name__ == "__main__":
    # creating processes
    p1 = multiprocessing.Process(target=print_square, args=(10, ))
    p2 = multiprocessing.Process(target=print_cube, args=(10, ))
 
    # starting process 1
    p1.start()
    # starting process 2
    p2.start()
 
    # wait until process 1 is finished
    p1.join()
    # wait until process 2 is finished
    p2.join()
 
    # both processes finished
    print("Done!")
