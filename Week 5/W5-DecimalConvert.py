"""This is an example answer from P'Kumamon. Please try to understand first"""
def baseconvert(num, base):
"""This is an example answer from P'Kumamon. Please try to understand first"""
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s = ""
    while 1:
        r = int(num % base)
        s = digits[r] + s
        num = num / base
        if num < 1:
            break
    return s

def main():
"""This is an example answer from P'Kumamon. Please try to understand first"""
    num = int(input())
    for i in range(2,37):
        print("Base %d: %s"%(i,baseconvert(num,i)))

main()
