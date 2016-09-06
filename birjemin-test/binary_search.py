def binarySearch(l, t):
    start = 0
    end = len(l)
    while(start < end):
        midd = int((start + end) / 2)
        print start, end, midd
        if l[midd] > t:
            end = midd
        elif l[midd] < t:
            start = midd + 1
        else:
            return l[midd]
if __name__ == '__main__':
    l = [1, 4, 12, 45, 66, 99, 120, 444]
    print(binarySearch(l, 45))
