"""This is an example answer from P'Kumamon. Please try to understand first"""
def kumamon():
    """This is an example answer from P'Kumamon. Please try to understand first"""
    text = bin(int(input()))[2:]
    print((max(8 - len(text), 0)*"0" + text)[-8:])
kumamon()
