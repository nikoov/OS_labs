#student name: Nikoo Vali
#student number: 83343012

import threading
import random  # is used to cause some randomness
import time    # is used to cause some delay in item production/consumption

class circularBuffer: 
    """ 
        This class implements a barebone circular buffer.
        Use as is.
    """
    def __init__ (self, size: int):
        """ 
            The size of the buffer is set by the initializer 
            and remains fixed.
        """
        self._buffer = [0] * size   # initialize a list of length size
                                    # all zeroed (initial value doesn't matter)
        self._in_index = 0   # the in reference point (where items will be inserted)
        self._out_index = 0  # the out reference point (where items will be removed)

    def insert(self, item: int):
        """ 
            Inserts the item in the buffer.
            The safeguard to make sure the item can be inserted
            is done externally (handled by the producer).
        """
        self._buffer[self._in_index] = item
        self._in_index = (self._in_index + 1) % SIZE  # Circular increment of in_index

    def remove(self) -> int:
        """ 
            Removes an item from the buffer and returns it.
            The safeguard to make sure an item can be removed
            is done externally (handled by the consumer).
        """
        item = self._buffer[self._out_index]
        self._out_index = (self._out_index + 1) % SIZE  # Circular increment of out_index
        return item

def producer() -> None:
    """
        The producer function to be used by the producer thread.
        It must correctly use full, empty and mutex to synchronize access to the buffer.
    """
    def waitForItemToBeProduced() -> int: # inner function; use as is
        # Simulate a delay to mimic the time taken to produce an item
        time.sleep(round(random.uniform(.1, .3), 2))  # random delay (100 to 300 ms)
        return random.randint(1, 99)  # generate a random item to be produced

    for _ in range(SIZE * 2): # Produce twice the buffer size for testing
        item = waitForItemToBeProduced()  # Wait for an item to be produced
        print(f"DEBUG: {item} produced")

        # Wait until there is an empty slot available (decrement the empty semaphore)
        empty.acquire()

        # Lock the critical section to ensure safe insertion
        mutex.acquire()
        buffer.insert(item)  # Safely insert the item into the buffer
        mutex.release()  # Release the lock

        # Signal that there is one more full slot available (increment the full semaphore)
        full.release()

def consumer() -> None:
    """
        The consumer function to be used by the consumer thread.
        It must correctly use full, empty and mutex to synchronize access to the buffer.
    """
    def waitForItemToBeConsumed(item) -> None: # inner function; use as is
        # Simulate a delay to mimic the time taken to consume an item
        time.sleep(round(random.uniform(.1, .3), 2))  # random delay (100 to 300 ms)

    for _ in range(SIZE * 2): # Consume twice the buffer size for testing
        # Wait until there is a full slot available (decrement the full semaphore)
        full.acquire()

        # Lock the critical section to ensure safe removal
        mutex.acquire()
        item = buffer.remove()  # Safely remove the item from the buffer
        mutex.release()  # Release the lock

        # Signal that there is one more empty slot available (increment the empty semaphore)
        empty.release()

        # Simulate the consumption of the item
        waitForItemToBeConsumed(item)
        print(f"DEBUG: {item} consumed")

if __name__ == "__main__":
    SIZE = 5  # Buffer size
    buffer = circularBuffer(SIZE)  # Initialize the buffer

    # Semaphores and mutex
    full = threading.Semaphore(0)         # Full semaphore: number of full buffers (starts at 0)
    empty = threading.Semaphore(SIZE)     # Empty semaphore: number of empty buffers (starts at SIZE)
    mutex = threading.Lock()  # Lock for protecting data on insertion or removal

    # Create producer and consumer threads
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    # Start the threads
    producer_thread.start()
    consumer_thread.start()

    # Wait for both threads to complete
    producer_thread.join()
    consumer_thread.join()

    print("Producer-Consumer operation completed.")

