"""This is an example answer from P'Kumamon. Please try to understand first"""
import math
def main():
    """Try to diverge the function as much as possible."""
    r,pi = float(input()),math.pi
    print(str(int(2*pi*r))+" cm",str(int(pi*r**2))+" cm^2",str(int((4/3)*pi*(r**3)))+" cm^3",sep='\n')
main()
