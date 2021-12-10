import time
if __name__ == '__main__':
    K = int(input('distance between stops: '))
    N = int(input('distance traveled by SvetOchka: '))
    time_start = time.time()
    next_stop_in = N % K
    previous_stop_in = K - next_stop_in
    nearest_stop_in = min(next_stop_in, previous_stop_in)
    print('distance to nearest stop:', nearest_stop_in)
    print('execution time:', time.time()-time_start)