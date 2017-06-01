"""This is an example answer from P'Kumamon. Please try to understand first"""
result = "Kumamon"
lowest = 99999999.9
def main():
    """This is an example answer from P'Kumamon. Please try to understand first"""
    global result, lowest
    text = input()
    price, weight = float(input()), float(input())
    values = price/weight
    calculate = min(lowest, values) == values
    raw_result = (result * (not calculate)) + (text * calculate)
    lowest = (lowest * (not calculate)) + (values * calculate)
    result = raw_result
    #print("Text:", text, "Values:", values, "calculate", calculate, result, lowest) >> DEBUG LINE
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
print(result)
