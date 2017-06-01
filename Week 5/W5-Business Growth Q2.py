"""This is an example answer from P'Kumamon. Please try to understand first"""
def kumamon():
    """This is an example answer from P'Kumamon. Please try to understand first"""
    num = int(input())
    tmp = 1
    for ind in range(1, num+1):
        ans = 0
        for _ in range(ind):
            ans += tmp
        print("%02d - %d" % (ind, ans))
        tmp = ans
kumamon()
