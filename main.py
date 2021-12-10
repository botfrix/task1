import time
if __name__ == '__main__':
    distance_between_stops = int(input('distance between stops: '))
    distance_traveled_by_SvetOchka = int(input('distance traveled by SvetOchka: '))
    time_start = time.time()
    next_stop_in = distance_traveled_by_SvetOchka % distance_between_stops
    previous_stop_in = distance_between_stops - next_stop_in
    nearest_stop_in = min(next_stop_in, previous_stop_in)
    print('distance to nearest stop:', nearest_stop_in)
    print('execution time:', time.time()-time_start)