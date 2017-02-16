# Sokolov 14/02/17
# Maximizing production of subarray in string, two versions: dumb and less_dumber

import time
import random
from decimal import Decimal

def maxproduction_v1(input_array, subarray_length):
    # works at O(n^2)
    max_production = 0
    for i in range(len(input_array) - subarray_length + 1):
        li = input_array[i:i + subarray_length]
        current_production = 1
        for sym in li:
            current_production *= int(sym)
        if current_production > max_production:
            max_production = current_production

    return max_production


def maxproduction_v2(input_array, subarray_length):
    # works at O(n)
    max_production = 0
    current_production = 1

    for index, sym in enumerate(input_array):
        current_production *= int(sym)
        if index >= subarray_length:
            current_production /= Decimal(input_array[index - subarray_length])

        if current_production > max_production:
            max_production = current_production

    return max_production

def main():
    input_string = ''.join([str(random.randrange(1, 10)) for n in range(9001)])
    print('String is :\n{}'.format(input_string))
    sub_string = 1000

    start = time.time()
    result_1 = maxproduction_v1(input_string,sub_string)
    restime_1 = time.time() - start

    start = time.time()
    result_2 = maxproduction_v2(input_string,sub_string)
    restime_2 = time.time() - start

    print('First solution finishes in {:.5f} s ; second in {:.5f} s;\nRatio is {:.2f}'.format(restime_1,restime_2,restime_1/restime_2))


if __name__ == '__main__':
    main()