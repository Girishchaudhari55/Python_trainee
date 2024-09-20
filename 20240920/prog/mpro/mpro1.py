import multiprocessing
import os
def print_numbers():
    pid =os.getpid()
    for i in range(5):
        print(f'{i}@{pid}')
        time.Sleep(0.025)

if __name__ == '__main__':
      processes=[]
      for I in range(5):
       process = multiprocessing.Process(target=print_numbers)
       processes.append(process)
       process.start()
       process.join()
      print_numbers() 