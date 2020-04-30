import time
time_start = time.time()

def find_factors(x):
    factors_list = []
    for i in range(2,x,1):
        if x % i != 0:
            factors_list.append(i)
    factors_list.append(x)
    for i in range(len(factors_list)-1,-1,-1):
        for z in range(i-1,-1,-1):
            if factors_list[i] % factors_list[z] == 0:
                factors_list.pop(z)
    return factors_list


def find_solution(x,y):
    z = find_factors(x)
    for i in range(20,y,20):
        if all(i % b == 0 for b in z):
            return i


if __name__=="__main__":
    print(find_solution(20,999999999999999999))
    elapsed_time = time.time() - time_start
    print(elapsed_time)


