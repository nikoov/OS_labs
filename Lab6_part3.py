# student name: Nikoo Vali
# student number: 83343012

import multiprocessing
import random  # used to add randomness 
import time    # used to add delay for thinking/eating times

def philosopher(id: int, chopstick: list): 
    """
    Implements a thinking-eating philosopher with an asymmetric deadlock avoidance strategy.
    id: Identifier for philosopher #id (0 to numberOfPhilosophers-1)
    chopstick: List of semaphores representing each chopstick
    """
    
    def eatForAWhile():  # simulates eating with a random delay
        print(f"DEBUG: philosopher{id} eating")
        time.sleep(round(random.uniform(.1, .3), 2))  # random delay (100 to 300 ms)
    
    def thinkForAWhile():  # simulates thinking with a random delay
        print(f"DEBUG: philosopher{id} thinking")
        time.sleep(round(random.uniform(.1, .3), 2))  # random delay (100 to 300 ms)

    for _ in range(6):  # finite loop to facilitate testing
        leftChopstick = id
        rightChopstick = (id + 1) % 5

        # Asymmetric approach: even philosopher picks right first, odd philosopher picks left first
        if id % 2 == 0:  # Even philosopher (0, 2, 4): pick right chopstick first
            chopstick[rightChopstick].acquire()
            print(f"DEBUG: philosopher{id} has chopstick{rightChopstick}")
            chopstick[leftChopstick].acquire()
            print(f"DEBUG: philosopher{id} has chopstick{leftChopstick}")
        else:  # Odd philosopher (1, 3): pick left chopstick first
            chopstick[leftChopstick].acquire()
            print(f"DEBUG: philosopher{id} has chopstick{leftChopstick}")
            chopstick[rightChopstick].acquire()
            print(f"DEBUG: philosopher{id} has chopstick{rightChopstick}")

        # Eating phase with both chopsticks in hand
        eatForAWhile() #use this line as is

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

    philosopherProcessList = list()
    for i in range(numberOfPhilosophers):  # instantiate processes representing philosophers
        philosopherProcessList.append(multiprocessing.Process(target=philosopher, args=(i, semaphoreList)))
    for j in range(numberOfPhilosophers):  # start all child processes
        philosopherProcessList[j].start()
    for k in range(numberOfPhilosophers):  # join all child processes
        philosopherProcessList[k].join()
