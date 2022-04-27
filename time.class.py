
class  Time:
    def __init__(self,h,m,s):
        self.hour=h
        self.minute= m
        self.second=s
    def show(self):
        print(self.hour,":",self.minute,":",self.second)
    def add(self,B):
        R=Time(0,0,0)
        R.hour=self.hour+B.hour
        R.minute=self.minute+B.minute
        R.second=self.second+B.second
        return R
    def sub(self,B):
        R=Time(0,0,0)
        R.hour=self.hour-B.hour
        R.minute=self.minute-B.minute
        R.second=self.second-B.second
        R.fix_sub()
        return R
    def fix(self):
        if self.second>=60:
            self.second-=60
            self.minute+=1
        if self.minute>=60:
            self.minute-=60
            self.hour+=1
    def fix_sub(self):
        if (self.minute<0):
            self.minute+=60
            self.hour-=1
        if self.second<0:
            self.second+=60
            self.minute-=1

    def make_time(self,B):
        R=Time(0,0,0)
        self.hour=int(self.second/3600)
        self.minute=int((self.second-(self.hour*3600))/60)
        self.second=(self.second-(self.hour*3600+self.minute*60))
        R.hour=self.hour
        R.minute=self.minute
        R.second=self.second
        print("seconds to time : ")
        return R
    def convert_to_second(self,B):
        print( "time to second: ",self.hour*3600+self.minute*60+self.second)
       
t1= Time(2,59,4)
t2=Time(1,7,10)
t3=Time(1,0,55)
t4=Time(0,0,5500)
t1.show()
t2.show()
t3.show()
output1=t1.add(t2)
output1.fix()
output1.show()
output2=t1.sub(t2)
output2.fix()
output2.show()
output3=t3.convert_to_second(t3)
output4=t4.make_time(t4)
output4.show()



           
