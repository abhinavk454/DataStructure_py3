#import section
import matplotlib.pyplot as plt
import time
import random
import matplotlib.animation as animation
#merge sort
def mergesort(A, start, end):
    if end <= start:
        return
    mid = start + ((end - start + 1) // 2) - 1
    yield from mergesort(A, start, mid)
    yield from mergesort(A, mid + 1, end)
    yield from merge(A, start, mid, end)
    yield A
def merge(A, start, mid, end):
    merged = []
    leftIdx = start
    rightIdx = mid + 1
    while leftIdx <= mid and rightIdx <= end:
        if A[leftIdx] < A[rightIdx]:
            merged.append(A[leftIdx])
            leftIdx += 1
        else:
            merged.append(A[rightIdx])
            rightIdx += 1
    while leftIdx <= mid:
        merged.append(A[leftIdx])
        leftIdx += 1
    while rightIdx <= end:
        merged.append(A[rightIdx])
        rightIdx += 1
    for i, sorted_val in enumerate(merged):
        A[start + i] = sorted_val
        yield A
if __name__=="__main__":
    n=int(input("Enter value of n:"))
    list=[x+1 for x in range(n)]
    random.seed(time.time())
    random.shuffle(list)
    #list=[548,465,455,5,5,4,54,12,545,12,45,5,7]
    merger=mergesort(list,0,len(list)-1)
    fig,axis=plt.subplots()
    axis.set_title("Merge sort")
    bar_rectangle=axis.bar(range(len(list)),list,align='edge')
    iteration=[0]
    text=axis.text(0.02,0.95,"",transform=axis.transAxes)
    def update(list,rects,lteration):
        for rect,val in zip(rects,list):
            rect.set_height(val)
        iteration[0]+=1
        text.set_text("Operation :{}".format(iteration[0]))
    animate=animation.FuncAnimation(fig,func=update,fargs=(bar_rectangle,iteration),frames=merger,interval=1,repeat=False)
    plt.xlabel('index value :->')
    plt.ylabel('Value :->')
    #plt.legend()
    plt.show()