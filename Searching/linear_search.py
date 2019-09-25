#linear searching2d O(n^2)
#linear searching1d O(n)
def linearsearch2D(Array,value):
    for i in range(len(Array)):
        for j in range(len(Array[i])):
            if Array[i][j]==value:
                return 1
    return 0
def linearsearch1D(Array,value):
    for i in range(len(Array)):
        if Array[i]==value:
            return 1
    return 0