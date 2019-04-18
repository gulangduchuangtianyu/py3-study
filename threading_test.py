'''
多线程类似于同时执行多个不同程序，多线程运行有如下优点：
使用线程可以把占据长时间的程序中的任务放到后台去处理。
用户界面可以更加吸引人，比如用户点击了一个按钮去触发某些事件的处理，可以弹出一个进度条来显示处理的进度
程序的运行速度可能加快
在一些等待的任务实现上如用户输入、文件读写和网络收发数据等，线程就比较有用了。在这种情况下我们可以释放一些珍贵的资源如内存占用等等。

使用Thread类，可以有多种方法创建线程：

1.创建Thread类的实例，传递一个函数
2.创建Thread类的实例，传递一个可调用的类实例
3.派生Thread类的子类，并创建子类的实例

一般的，我们会采用第一种或者第三种方法。如果需要一个更加符合面向对象的接口时，倾向于选择第三种方法，否则就用第一种方法。

'''
import threading
from time import sleep,ctime

#创建两个线程分别在不同的时间段执行（用来演示多线程下是并发执行的，顺序是乱的），并把这些常量放进列表loops中
loops=[4,2]

def handel_excel(nloop,nsec):
    print('子线程：'+str(nloop),'开始执行excel任务了','at:',ctime())
    sleep(nsec)
    print('子线程：'+str(nloop),'结束执行excel任务了','at',ctime())

def handel_word(nloop,nsec):
    print('子线程：'+str(nloop),'开始执行word任务了','at:',ctime())
    sleep(nsec)
    print('子线程：'+str(nloop),'结束执行word任务了','at',ctime())

'''第一种方式创建'''
def main_first():
    print('子线程开始工作于：',ctime())
    threads=[]
    nloops=range(len(loops))
    
    for i in nloops:
        #循环 实例化2个Thread类，传递函数及其参数，并将线程对象放入threads列表中,这个列表主要是为了后续便于实现阻塞主线程，
        #让主线程等待所有的子线程都把任务执行完毕了才往下执行
        if i ==0 :
            t=threading.Thread(target=handel_excel,args=(i,loops[i]))
        else :
            t=threading.Thread(target=handel_word,args=(i,loops[i]))
        threads.append(t)
        
    for i in nloops:
        threads[i].start()  #循环 开始线程
        
    for i in nloops:
        threads[i].join()   #循环 join()方法可以让主线程等待所有的子线程都执行完毕才会往下执行，除非添加时间 join(时间秒)，表示多少秒后往下执行。
        
    print('主线程任务完成于：',ctime())



'''第三种方式创建'''
class Mythread(threading.Thread):
    """docstring for Mythread"""
    def __init__(self,func,args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        
    def run(self):  #重写run方法  run是运行线程需要处理的函数
        self.func(*self.args)   


def main_third():
    ths = []
    for i in range(len(loops)):
        if i ==0 :
            th  = Mythread(handel_excel,(i,loops[i]))
        else :
            th  = Mythread(handel_word,(i,loops[i]))
        ths.append(th)
        th.start()
    for i in range(len(loops)):
        ths[i].join()
        
    print('主线程任务完成于：',ctime())

def tupelFunc(*args) :
    for i in args:
        print(i)  
if __name__=='__main__':
    '''提示：用tupel类型传参需要在前面加*'''
    # tupelFunc(*('tuple','test')) 

    # main_first()
    main_third()
    