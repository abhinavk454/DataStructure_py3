#import section
import matplotlib.pyplot as plt
import time
import numpy as np
import matplotlib.animation as animation
import random

#bubble sort
def bubble(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i]<list[j]:
                temp=list[i]
                list[i]=list[j]
                list[j]=temp
            yield list
    #return list

list=[12,35,1,5,425,4,542,45,54,1,24,5,2,12]
bubble_generator=bubble(list)

#visualization function
fig,axis=plt.subplots()
axis.set_title("Bubble sort")
bar_rectangle=axis.bar(range(len(list)),list,align='edge')
iteration=[0]
text=axis.text(0.02,0.95,"",transform=axis.transAxes)
def update(list,rects,lteration):
    for rect,val in zip(rects,list):
        rect.set_height(val)
    iteration[0]+=1
    text.set_text("Operation :{}".format(iteration[0]))
animate=animation.FuncAnimation(fig,func=update,fargs=(bar_rectangle,iteration),frames=bubble_generator,interval=1,repeat=False)
plt.xlabel('index value :->')
plt.ylabel('Value :->')
plt.legend()
plt.show()
print(list)