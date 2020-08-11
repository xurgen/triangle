'''屏幕打印字符等腰三角形'''

def strprint(xstr,n):
    a=1
    num=n*2+1
    while True:
        a=a+2
        n=n-1
        for i in range(0,n):   #定位打印第一个字符的位置
            print(" ",end="")  #打印第一个字符前的的空格
        for j in range(2,a):   #每行打印的字符个数
            print(xstr,end="")  #打印“*”号
        print("")
        if a==num:
            break
    

def main():
    xstr = input("请输入要打印的任意单个英文字符或符号： ")
    n=int(input("请输入要打印三角形的层数(小于40）： "))
    strprint(xstr,n)

if __name__ == "__main__":
    main()

    
	    
