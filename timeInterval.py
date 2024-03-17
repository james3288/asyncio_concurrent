import time

def check_interval(func):
    def wrapper():
        print('wait for 10 seconds...')
        time.sleep(10)
        func()
        print('done..')

    return wrapper

if __name__ == '__main__':
    pass