import threading
import time
import multiprocessing
import sqlite3


class FileContextManager:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()


# File name
file_path = "text.txt"

# Opening the file using the context manager
with FileContextManager(file_path, "w") as file:
    file.write("File opened")

# File is automatically closed outside the context manager


# context manager to open and close a database


class DatabaseConnection:
    def __init__(self, host):
        self.host = host
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()


# multiprocessing


def worker(duration):
    print(f'Starting process {multiprocessing.current_process().name}')
    time.sleep(duration)
    print(f'Exiting process {multiprocessing.current_process().name}')


if __name__ == '__main__':
    process1 = multiprocessing.Process(target=worker, args=(5,))
    process2 = multiprocessing.Process(target=worker, args=(10,))
    process1.start()
    process2.start()
    process1.join()
    process2.join()


# multithreading


def worker(duration):
    print(f'Starting thread {threading.current_thread().name}')
    time.sleep(duration)
    print(f'Exiting thread {threading.current_thread().name}')


if __name__ == '__main__':
    thread1 = threading.Thread(target=worker, args=(5,))
    thread2 = threading.Thread(target=worker, args=(10,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
