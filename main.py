import time

ITERATIONS = 1000000


if __name__=="__main__":
    print("Program started")
    for i in range(ITERATIONS):
        if i % 1000 ==0:
            print(i)
        time.sleep(0.001)
        
    
    print("Progressing finished")
