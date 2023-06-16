import time

def sleep():
    time.sleep(1)

def num_check(num):
    start = time.time()
    for i in range(1, num):
        print(i)
        sleep()
    
    end = time.time()
    print(end - start)

def main():

    start = time.time()    
    res1 = num_check(5)
    res2 = num_check(5)

    end = time.time()

    print(f'총 시간 = {end - start}')

if __name__ == "__main__":
    main()