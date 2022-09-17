# 3

def miniMaxSum(arr):
    arr.sort()
    array_size = len(arr)
    print(sum(arr[0:array_size-1]), sum(arr[(array_size - 1)*-1:]))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
