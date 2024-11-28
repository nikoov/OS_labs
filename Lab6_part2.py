# student name: Nikoo Vali
# student number: 83343012

import multiprocessing
import random  # is used to cause some randomness 
import time    # is used to cause some delay to simulate thinking or eating times

def philosopher(id: int, chopstick: list, lock):
    """
    Implements a thinking-eating philosopher with deadlock avoidance by only picking up both chopsticks if both are available.
    id: Identifier for philosopher #id (0 to numberOfPhilosophers-1)
    chopstick: List of semaphores representing each chopstick
    lock: A lock to control checking and acquiring chopsticks as a single action
    """
    
    def eatForAWhile():  # simulates eating with a random delay
        print(f"DEBUG: philosopher{id} eating")
        time.sleep(round(random.uniform(.1, .3), 2))  # random delay (100 to 300 ms)
    
    def thinkForAWhile():  # simulates thinking with a random delay
        print(f"DEBUG: philosopher{id} thinking")
        time.sleep(round(random.uniform(.1, .3), 2))  # random delay (100 to 300 ms)

    for _ in range(6):  # finite loop for easier testing
        leftChopstick = id
        rightChopstick = (id + 1) % 5  # calculating the right chopstick index

        # Use lock to check and acquire both chopsticks if available
        with lock:
            chopstick[leftChopstick].acquire()  # acquire the left chopstick
            acquired_right = chopstick[rightChopstick].acquire(block=False)  # try to acquire right chopstick without blocking
            if not acquired_right:  # if right chopstick isn't available
                chopstick[leftChopstick].release()  # release left chopstick
                continue  # retry the loop in the next iteration

        # Both chopsticks are now acquired
        print(f"DEBUG: philosopher{id} has chopstick{leftChopstick} and chopstick{rightChopstick}")
        #eating phase
        eatForAWhile()  #use this line as is

        # Release both chopsticks after eating
        print(f"DEBUG: philosopher{id} is to release chopstick{rightChopstick}")
        chopstick[rightChopstick].release()
        print(f"DEBUG: philosopher{id} is to release chopstick{leftChopstick}")
        chopstick[leftChopstick].release()
        
        #thinking phase
        thinkForAWhile()  #use this line as is

if __name__ == "__main__":
    semaphoreList = list()  # list to hold one semaphore per chopstick
    numberOfPhilosophers = 5

    # Initialize one semaphore for each chopstick
    for i in range(numberOfPhilosophers):             
        semaphoreList.append(multiprocessing.Semaphore(1))

    # Lock to coordinate checking and acquiring chopsticks
    lock = multiprocessing.Lock()

    philosopherProcessList = list()
    for i in range(numberOfPhilosophers):  # instantiate processes representing philosophers
        philosopherProcessList.append(multiprocessing.Process(target=philosopher, args=(i, semaphoreList, lock)))
    for j in range(numberOfPhilosophers):  # start all child processes
        philosopherProcessList[j].start()
    for k in range(numberOfPhilosophers):  # join all child processes
        philosopherProcessList[k].join()
