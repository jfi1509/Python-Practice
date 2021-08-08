import math
import time

def special_num(num_list):
    count = 0
    for number in num_list:
        for i in range(1, number/2+1):
            if(i + int(str(i)[::-1]) == number):
                count += 1
                break

    return count

def special_num_js(num_list):
    count = 0
    for number in num_list:
        i = int(math.floor(number/2))
        j = int(math.ceil(number/2))

        while(i > 0):
            if(i == int(str(j)[::-1])):
                count += 1
                break
            i -= 1
            j += 1
    return count

def special_num_max(num_list):
    max_num = max(num_list)
    magic_number_memo = set()

    for number in range(1, max_num+1):
        for i in range(1, number/2 +1):
            if(i + int(str(i)[::-1]) == number):
                magic_number_memo.add(number)

    result = list(filter(lambda x: x in magic_number_memo, num_list))
    print(len(result))

if __name__ == '__main__':
    num_list = [1,100,10000000]

    # initial_time = time.time()
    # special_num(num_list)
    # print(initial_time, time.time() - initial_time)


    # initial_time_js = time.time()
    # special_num(num_list)
    # print(initial_time_js, time.time() - initial_time_js)

    initial_time_max = time.time()
    special_num(num_list)
    initial_time_max = time.time()
    print(time.time() - initial_time_max)

# 1000
# 0.147863864899 
# 0.144988059998
# 0.146052122116


# 10000
# 15.4672920704 - normal check method
# 15.4801330566 - floor ceil method
# 14.9468569756 - filter approach