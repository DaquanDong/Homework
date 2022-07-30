from pysmx.SM3 import SM3
import random
import time
func=SM3()
L=[]
def RhoMethod(n):
    a=random.randint(0,0xfffff)
    b=str(a)
    List=[]
    for i in range(pow(2,32)):   
        func.update(b)
        c=func.hexdigest()
        L.append(c)
        char=L[0][:n]#结果切片
        List.append(char)
        a=2*a
        if char in List:
            print("寻找",n,"比特碰撞成功")
            return;
        print("寻找碰撞失败")
if __name__ == '__main__':
    startime=time.time()
    RhoMethod(8)
    endtime=time.time()
    time=endtime-startime
    time=time*1000
    print("用时", time, "ms")
