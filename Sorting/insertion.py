#import section
import matplotlib.pyplot as plt
import time
import random
import matplotlib.animation as animation
#insertion sort
def insertionsort(arr):
    for i in range(1,len(arr)):
        current=arr[i]
        j=i-1
        while j>=0 and arr[j]>current:
            arr[j+1]=arr[j]
            j-=1
            yield arr
        arr[j+1]=current
#main
if __name__=="__main__":
    n=int(input("Enter value of n:"))
    list=[x+1 for x in range(n)]
    random.seed(time.time())
    random.shuffle(list)
    #list=[548,465,455,5,5,4,54,12,545,12,45,5,7]
    merger=insertionsort(list)
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
