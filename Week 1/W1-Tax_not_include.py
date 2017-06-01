"""This is an example answer from P'Kumamon. Please try to understand first"""
def main():
    """This is an example answer from P'Kumamon. Please try to understand first"""
    price, vat = int(input()), float(input())
    print("Subtotal:", price)
    print("Tax ("+str(vat*100)+"%):", int(price*vat))
    print("Total:", int(price+(price*vat)))
main()
