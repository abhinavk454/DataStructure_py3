class hashtable(object):
    def __init__(self,value):
        self.size=value
        self.slot=[None]*self.size#for storing key
        self.data=[None]*self.size
    
    def putdata(self,key,data):
        indexval=self.hashfunc(key,len(self.slot))
        if self.slot[indexval]==None:
            self.slot[indexval]=key
            self.data[indexval]=data
        else:#stops collid by finding and setting data in empty slot
            nextslot=self.rehash(indexval,len(self.slot))
            while self.slot[nextslot]!=None and self.slot[nextslot]!=key:
                nextslot=self.rehash(nextslot,len(self.slot))
            if self.slot[nextslot]==None:
                self.slot[nextslot]=key
                self.data[nextslot]=data
            else:
                self.data[nextslot]=data
    def getdata(self,key):
        startindex=self.hashfunc(key,len(self.slot))
        data=None
        stop=False
        found=False
        pos=startindex
        while self.slot[pos]!=None and not found and not stop:
            if self.slot[pos]==key:
                found=True
                data=self.data[pos]
            else:
                pos=self.rehash(pos,len(self.slot))
                if pos==startindex:
                    stop=True
        return data
                
    def hashfunc(self,key,size):
        return key%size
    
    def rehash(self,oldhash,size):
        return (oldhash+1)%size
    
    def __getitem__(self,key):
        return self.getdata(key)
    
    def __setitem__(self,key,data):
        self.putdata(key,data)

Hash=hashtable(10)
Hash[1]='abhi'
Hash[1]='nav'
print(Hash.data)
print(Hash.slot)