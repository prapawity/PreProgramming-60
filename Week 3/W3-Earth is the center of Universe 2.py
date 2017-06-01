"""This is an example answer from P'Kumamon. Please try to understand first"""
def kumamon(text,limits):
    """This is an example answer from P'Kumamon. Please try to understand first"""
    align = (limits-len(text)) // 2
    print("|", " "*align, text[:limits], " "*align, "|",sep="")
    print("FOR DEBUG: Space = %d   Text Length = %d\n"%(align,len(text)))

def kumamoto(text):
    kumamon(text,20)
    kumamon(text,50)
    kumamon(text,40)
    kumamon(text,30)
    kumamon(text,22)
    kumamon(text,14)
    kumamon(text,20)
    kumamon(text,42)
    kumamon(text,60)
    kumamon(text,70)

kumamoto(input())
