"""This is an example answer from P'Kumamon. Please try to understand first"""
def kumamon():
    """This is an example answer from P'Kumamon. Please try to understand first"""
    text = input().upper()
    count = len(text)
    print("A: %2.2f%% (%d/%d)"%((text.count('A')/count)*100,text.count('A'),count))
    print("B: %2.2f%% (%d/%d)"%((text.count('B')/count)*100,text.count('B'),count))
    print("C: %2.2f%% (%d/%d)"%((text.count('C')/count)*100,text.count('C'),count))
    print("D: %2.2f%% (%d/%d)"%((text.count('D')/count)*100,text.count('D'),count))
    print("E: %2.2f%% (%d/%d)"%((text.count('E')/count)*100,text.count('E'),count))
kumamon()
