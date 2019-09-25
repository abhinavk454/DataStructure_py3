def binary_search(Array,value):
    if len(Array==1):
        return
    else:
        midd=len(Array)//2
        if value==Array[midd]:
            return 1
        elif value>Array[midd]:
            return binary_search(Array[midd:],value)
        else:
            return binary_search(Array[:midd],value)
