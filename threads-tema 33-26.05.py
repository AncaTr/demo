import threading

# Shared variables
counter = 0
rounds = 100000

# Lock for synchronizing access to the shared counter
counter_lock = threading.Lock()

class Counter(threading.Thread):
    def run(self):
        global counter
        for _ in range(rounds):
            with counter_lock:
                counter += 1

# # Create and start two threads
thread1 = Counter()
thread2 = Counter()

thread1.start()
thread2.start()

# # Wait for both threads to finish
thread1.join()
thread2.join()

# Check the result of the counter
print(f"The final value of counter is: {counter}")

