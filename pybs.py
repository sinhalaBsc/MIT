

class binarySearch:
    def __init__(self):
        pass


    def initiate(self,value,array):
        self.v=value
        self.arr=array
        self.arrlen=len(array)
        self.l=0
        self.r=len(array)-1

    def compare(self,m):       
        if self.v==self.arr[m]:
            direction=0
            point=m
            return direction,point
        if self.v>self.arr[m]:
            direction=1
            point=int((self.r+m)/2)+1
            self.l=m
            return direction,point
        else:
            direction=-1
            point=int((self.l+m)/2)
            self.r=m
            return direction,point


    def binarySearch(self,v,arr):
        self.initiate(v,arr)
        self.l=0
        self.r=self.arrlen-1    
        midpoint=int((self.arrlen-1)/2)
        p=midpoint
        #print(midpoint)
        d=True 
        while d:
        #for j in range(5):
            #print('direction -: ',d)
            #print('point     -: ',p)
            d,p=self.compare(p)
        return p
