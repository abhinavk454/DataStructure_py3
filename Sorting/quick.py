#import section
import matplotlib.pyplot as plt
import time
import random
import matplotlib.animation as animation
#quick sort
def quicksort(A, start, end):#inplace quick sort
    if start >= end:
        return
    pivot = A[end]
    pivotIdx = start
    for i in range(start, end):
        if A[i] < pivot:
            A[i],A[pivotIdx]=A[pivotIdx],A[i]
            pivotIdx += 1
        yield A
    A[end],A[pivotIdx]=A[pivotIdx],A[end]
    yield A

    yield from quicksort(A, start, pivotIdx - 1)
    yield from quicksort(A, pivotIdx + 1, end)
#main
if __name__=="__main__":
    n=int(input("Enter value of n:"))
    list=[x+1 for x in range(n)]
    random.seed(time.time())
    random.shuffle(list)
    #list=[548,465,455,5,5,4,54,12,545,12,45,5,7]
    merger=quicksort(list,0,len(list)-1)
    fig,axis=plt.subplots()
    axis.set_title("Quick sort")
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