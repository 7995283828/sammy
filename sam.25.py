def findMedian(s, h):
    sorted(s)
    if h % 2 != 0:
        return float(s[h/2])

    return float((s[int((h-1)/2)] +
                  s[int(h/2)])/2.0)
s = [ 1, 3, 4, 2, 7, 5, 8, 6 ]
h = len(s)
print("The Median is:", findMedian(s, h))