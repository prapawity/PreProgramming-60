"""grade cal - Example from N' ธีรภัทร ไกรศรีสิริกุล"""
def gradecal():
    """boolean cal"""
    scr = int(input())
    gr00 = (0 <= scr <= 49)
    gr10 = (50 <= scr <= 54)
    gr15 = (55 <= scr <= 59)
    gr20 = (60 <= scr <= 64)
    gr25 = (65 <= scr <= 69)
    gr30 = (70 <= scr <= 74)
    gr35 = (75 <= scr <= 79)
    gr40 = (80 <= scr <= 100)
    print("0"*gr00+"1"*gr10+ "1.5"*gr15+"2"*gr20+"2.5"*gr25+"3"*gr30+"3.5"*gr35+"4"*gr40)
gradecal()
