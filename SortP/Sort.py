import random
import time


def bubble(num):
    for i in reversed(range(len(num))):
        for j in range(i):
            # print(num)
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    return num


def insertion(num):
    for i in range(1, len(num)):
        tmp = num[i]
        # print(num)
        if num[i - 1] > tmp:
            j = i
            while j > 0 and num[j - 1] > tmp:
                num[j] = num[j - 1]
                j -= 1
            num[j] = tmp
    return num


def selection(num):
    for i in range(len(num)):
        # print(num)
        min_index = i
        for j in range(i, len(num)):
            if num[min_index] > num[j]:
                min_index = j
        num[i], num[min_index] = num[min_index], num[i]
    return num


def shaker(num):
    for i in range(len(num) // 2):
        # print("right")
        for j in range(i, len(num) - 1 - i):
            # print(num)
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
        # print("left")
        for k in reversed(range(i + 1, len(num) - 1 - i)):
            # print(num)
            if num[k - 1] > num[k]:
                num[k - 1], num[k] = num[k], num[k - 1]
    return num


def quick(num):
    pass

###############################################################


def merge_sort(num):
    if len(num) <= 1:
        return num

    mid = len(num) // 2

    left = num[:mid]
    right = num[mid:]
    # print("num_left" + str(left))
    # print("num_right" + str(right))
    right = merge_sort(right)
    left = merge_sort(left)
    return merge(left, right)


def merge(left, right):
    left_i, right_i = 0, 0
    merged = []
    # print("left:" + str(left))
    # print("right:" + str(right))
    while left_i < len(left) and right_i < len(right):
        if left[left_i] <= right[right_i]:
            merged.append(left[left_i])
            left_i += 1
        else:
            merged.append(right[right_i])
            right_i += 1

    if left_i < len(left):
        merged.extend(left[left_i:])
    elif right_i < len(right):
        merged.extend(right[right_i:])
    # print("merged" + str(merged))

    return merged

###############################################################


def bogo(num):
    while True:
        random.shuffle(num)

        for i in range(len(num) - 1):
            if num[i] > num[i + 1]:
                break
            elif i == len(num) - 2:
                return num


if __name__ == "__main__":
    num = [random.randint(0, 10000) for _ in range(10000)]
    start = time.time()
    # print("bubble:" + str(bubble(num)))
    # print("Bubble:"+str(bubble(num)))
    # print("Insertion:"+str(insertion(num)))
    # print("Selection:"+str(selection(num)))
    # print("Shaker:"+str(shaker(num)))
    # print("Merge:"+str(merge_sort(num)))
    # print("Bogo: + str(bogo(num))
    print(time.time() - start)
