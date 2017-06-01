"""This is an example answer from P'Kumamon. Please try to understand first"""
def kumamon():
    """This is an example answer from P'Kumamon. Please try to understand first"""
    ans = ["ABCD", "DCBA", "AABBCCDD", "AAAABBBBCCCCDDDD", "ABBACDDCABBACDDC","A","B","C","D","E"]
    count = [0, 0, 0, 0, 0]
    text = input().upper()
    for j in range(5):
        for i in range(len(text)):
            if text[i] == str(ans[j])[i%len(ans[j])]:
                count[j] += 1
        print("%s: %.2f%%"%(ans[j+5],(count[j]/len(text))*100))
kumamon()
