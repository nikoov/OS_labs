# student name: Nikoo Vali
# student number: 83343012

import multiprocessing
import random  # is used to cause some randomness 
import time    # is used to cause some delay to simulate thinking or eating times

def philosopher(id: int, chopstick: list, table_limit):
    """
    Implements a thinking-eating philosopher with a deadlock avoidance mechanism.
    id: Identifier for philosopher #id (0 to numberOfPhilosophers-1)
    chopstick: List of semaphores associated with the chopsticks
    table_limit: Semaphore limiting number of philosophers at the table to 4
    """
    
    def eatForAWhile():  # simulates eating with a random delay
        print(f"DEBUG: philosopher{id} eating")
        time.sleep(round(random.uniform(.1, .3), 2))  # random delay (100 to 300 ms)
    
    def thinkForAWhile():  # simulates thinking with a random delay
        print(f"DEBUG: philosopher{id} thinking")
        time.sleep(round(random.uniform(.1, .3), 2))  # random delay (100 to 300 ms)

    for _ in range(6):  # finite loop to test deadlock avoidance
        leftChopstick = id
        rightChopstick = (id + 1) % 5  # using modulo for circular arrangement

        # Acquire table limit to allow only 4 philosophers at the table at once
        table_limit.acquire()

        # Try to pick up the left and right chopsticks
        chopstick[leftChopstick].acquire()
        print(f"DEBUG: philosopher{id} has chopstick{leftChopstick}")
        chopstick[rightChopstick].acquire()
        print(f"DEBUG: philosopher{id} has chopstick{rightChopstick}")

        # Eating phase with both chopsticks in hand
        #using this line as is
        eatForAWhile()

        # Release both chopsticks after eating
        print(f"DEBUG: philosopher{id} is to release chopstick{rightChopstick}")
        chopstick[rightChopstick].release()
        print(f"DEBUG: philosopher{id} is to release chopstick{leftChopstick}")
        chopstick[leftChopstick].release()

        # Release table limit to allow another philosopher to join
        table_limit.release()

        # Thinking phase
        #using this line as is
        thinkForAWhile()

if __name__ == "__main__":
    semaphoreList = list()  # holds one semaphore per chopstick
    numberOfPhilosophers = 5

    # Create a semaphore for each chopstick (initially available)
    for i in range(numberOfPhilosophers):             
        semaphoreList.append(multiprocessing.Semaphore(1))

    # Table limit semaphore allows only 4 philosophers at the table simultaneously
    table_limit = multiprocessing.Semaphore(4)

    philosopherProcessList = list()
    for i in range(numberOfPhilosophers):  # instantiate all processes representing philosophers
        philosopherProcessList.append(multiprocessing.Process(target=philosopher, args=(i, semaphoreList, table_limit)))
    for j in range(numberOfPhilosophers):  # start all child processes
        philosopherProcessList[j].start()
    for k in range(numberOfPhilosophers):  # join all child processes
        philosopherProcessList[k].join()
