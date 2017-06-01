"""This is an example answer from P'Kumamon. Please try to understand first"""
def main():
    """This is an example answer from P'Kumamon. Please try to understand first"""
    var_x, var_y, var_z = int(input()), int(input()), int(input())
    var_max = max(max(var_x, var_y), var_z)
    var_min = min(min(var_x, var_y), var_z)
    var_mean = (var_x+var_y+var_z)-var_max-var_min
    print("Max:", var_max)
    print("Min:", var_mean)
    print("Mean:", var_min)
