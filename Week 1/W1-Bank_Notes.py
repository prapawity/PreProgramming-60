"""This is an example answer from P'Kumamon. Please try to understand first"""
def main():
    """This is an example answer from P'Kumamon. Please try to understand first"""
    money = int(input())
    money = calculator(money, 1000)
    money = calculator(money, 500)
    money = calculator(money, 100)
    money = calculator(money, 50)
    money = calculator(money, 20)

def calculator(money, multiplier):
    """This is an example answer from P'Kumamon. Please try to understand first"""
    calculate = money // multiplier
    print(calculate)
    money -= calculate * multiplier
    return money

main()
