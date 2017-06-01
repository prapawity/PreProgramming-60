"""This is an example answer from P'Kumamon. Please try to understand first"""
def main(text):
    """This is an example answer from P'Kumamon. Please try to understand first"""
    text = text+" #"
    multiplier(text, 0)
    multiplier(text, 50)

def multiplier(text, number):
    """This is an example answer from P'Kumamon. Please try to understand first"""
    multiplier2(text, number+0)
    multiplier2(text, number+10)
    multiplier2(text, number+20)
    multiplier2(text, number+30)
    multiplier2(text, number+40)

def multiplier2(text, number):
    """This is an example answer from P'Kumamon. Please try to understand first"""
    multiplier3(text, number)
    multiplier3(text, number+5)

def multiplier3(text, number):
    """This is an example answer from P'Kumamon. Please try to understand first"""
    print(text+str(number+1),\
          text+str(number+2),\
          text+str(number+3),\
          text+str(number+4),\
          text+str(number+5),sep="\t\t")

main(input())
