def bubble(num):
    for i in reversed(range(len(num))):
        for j in range(i):
            print(num)
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    return num
def insertion(num):
    for i in range(1,len(num)):
        tmp = num[i]
        print(num)
        if num[i - 1] > tmp:
            j = i
            while j > 0 and num[j - 1] > tmp:
                num[j] = num[j - 1]
                j -= 1
            num[j] = tmp
    return num
def selection(num):
    for i in range(len(num)):
        print(num)
        min_index = i
        for j in range(i,len(num)):
            if num[min_index] > num[j]:
                min_index = j
        num[i], num[min_index] = num[min_index], num[i]
    return num
def shaker(num):
    for i in range(len(num)):
        print("right")
        for j in range(i,len(num) - 1):
            print(num)
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j];
        print("left")
        for k in reversed(range(i + 1,len(num))):
            print(num)
            if num[k] < num[k - 1]:
                num[k], num[k - 1] = num[k - 1], num[k]
    return num
def quick(num):
    pass
    
if __name__ == "__main__":
    num = [11,2,-2,1,32,5,7,3,2,5,7,9,5,-2,-32,5,2,1,7,3,4]
    print("None:"+str(num))
    #print("Bubble:"+str(bubble(num)))
    #print("Insertion:"+str(insertion(num)))
    #print("Selection:"+str(selection(num)))
    print("Shaker:"+str(shaker(num)))
