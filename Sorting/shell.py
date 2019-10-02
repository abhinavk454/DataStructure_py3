#import section
import matplotlib.pyplot as plt
import time
import random
import matplotlib.animation as animation
#shell sort
def shell(arr):
    n=len(arr)
    gap=n//2
    while gap>0:
        for i in range(gap,n):
            #time.sleep(3)
            current=arr[i]
            j=i
            while j>=gap and arr[j-gap]>current:
                arr[j]=arr[j-gap]
                j-=gap
            arr[j]=current
            yield arr
        gap//=2
#main
if __name__=="__main__":
    n=int(input("Enter value of n:"))
    list=[x+1 for x in range(n)]
    random.seed(time.time())
    random.shuffle(list)
    #list=[548,465,455,5,5,4,54,12,545,12,45,5,7]
    merger=shell(list)
    fig,axis=plt.subplots()
    axis.set_title("Shell sort")
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