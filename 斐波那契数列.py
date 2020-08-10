# Python 斐波那契数列实现
 
def fib(n):
    
    res = []
    n0 = 0
    n1 = 1
    n2 = 1
    count = 0

    if n <= 0:
        print("请输入一个正整数。")
    else:
        res.append(n1)
        for i in range(2,n+1):
            nt = n0 + n1
            res.append(nt)
            n0 = n1
            n1 = nt
        print(res)
