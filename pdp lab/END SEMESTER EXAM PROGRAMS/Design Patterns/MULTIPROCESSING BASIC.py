import multiprocessing as mp
import time

def count_numbers(name, limit):
    for i in range(1, limit + 1):
        print(f"{name}: {i**2}")
        time.sleep(1)

if __name__ == "__main__":
    # Create two processes
    process1 = mp.Process(target=count_numbers, args=("Process 1", 5))
    process2 = mp.Process(target=count_numbers, args=("Process 2", 5))

    # Start the processes
    process1.start()
    process2.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()
