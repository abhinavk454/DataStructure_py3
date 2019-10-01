#import section
import matplotlib.pyplot as plt
import time
import random
import matplotlib.animation as animation
#selection sort
def selectionsort(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[min_index]>arr[j]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
        yield arr
#main
if __name__=="__main__":
    n=int(input("Enter value of n:"))
    list=[x+1 for x in range(n)]
    random.seed(time.time())
    random.shuffle(list)
    #list=[548,465,455,5,5,4,54,12,545,12,45,5,7]
    merger=selectionsort(list)
    fig,axis=plt.subplots()
    axis.set_title("Insertion sort")
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