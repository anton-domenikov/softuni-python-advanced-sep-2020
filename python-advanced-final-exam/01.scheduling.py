from collections import deque

jobs = deque(map(int, input().split(', ')))
index = int(input())

cycles = 0
target_num = jobs[index]

while True:
    min_num = min(jobs)
    min_num_index = jobs.index(min_num)

    if min_num_index == index:
        cycles += min_num
        break

    if min_num_index < index:
        cycles += min_num
        del jobs[min_num_index]
        index -= 1

    if min_num_index > index:
        cycles += min_num
        del jobs[min_num_index]

print(cycles)
