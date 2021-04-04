if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maximo = max(arr)
    while max(arr) == maximo:
        arr.remove(max(arr))
    print(max(arr))
