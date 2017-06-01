"""cramer's rule Example from N' กวิสรา บัณเย็น"""
def main():
    """input and calculate"""
    num_x1 = float(input())
    num_y1 = float(input())
    num_z1 = float(input())
    num_a1 = float(input())
    num_x2 = float(input())
    num_y2 = float(input())
    num_z2 = float(input())
    num_a2 = float(input())
    num_x3 = float(input())
    num_y3 = float(input())
    num_z3 = float(input())
    num_a3 = float(input())
    ans_x = (num_a1*num_y2*num_z3+num_y1*num_z2*num_a3+
             num_z1*num_a2*num_y3-num_a3*num_y2*num_z1-
             num_y3*num_z2*num_a1-num_z3*num_a2*num_y1)/(num_x1*num_y2*num_z3+num_y1*num_z2*num_x3+
                                                         num_z1*num_x2*num_y3-num_z1*num_y2*num_x3-
                                                         num_x1*num_z2*num_y3-num_y1*num_x2*num_z3)
    ans_y = (num_x1*num_a2*num_z3+num_a1*num_z2*num_x3+
             num_z1*num_x2*num_a3-num_x3*num_a2*num_z1-
             num_a3*num_z2*num_x1-num_z3*num_x2*num_a1)/(num_x1*num_y2*num_z3+num_y1*num_z2*num_x3+
                                                         num_z1*num_x2*num_y3-num_z1*num_y2*num_x3-
                                                         num_x1*num_z2*num_y3-num_y1*num_x2*num_z3)
    ans_z = (num_x1*num_y2*num_a3+num_y1*num_a2*num_x3+
             num_a1*num_x2*num_y3-num_x3*num_y2*num_a1-
             num_y3*num_a2*num_x1-num_a3*num_x2*num_y1)/(num_x1*num_y2*num_z3+num_y1*num_z2*num_x3+
                                                         num_z1*num_x2*num_y3-num_z1*num_y2*num_x3-
                                                         num_x1*num_z2*num_y3-num_y1*num_x2*num_z3)
    print(round(ans_x, 2))
    print(round(ans_y, 2))
    print(round(ans_z, 2))
main()
