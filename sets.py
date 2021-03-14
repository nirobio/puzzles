def average(array):
    setArr = set(arr)
    mean = (sum(setArr) / len(setArr))
    return mean


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
