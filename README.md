'''
passw = input ("enter pass ")
pass_ret = input ("return pass ")
if passw == pass_ret:
    print ("Good job")
else:
    print ("not good job")
'''
'''
seat_nomer = int(input("Write nomer mesta"))
if seat_nomer <= 1 or seat_nomer > 54:
    print("takogo mesta net")
else:
    if seat_nomer <= 30:
        if seat_nomer % 2 == 0:
            print("verx kupe")
        else:
            print("niz kupe")
    else:
        if seat_nomer % 2 == 0:
            print ("verx bok")
        else:
            print("niz bok")
'''
'''
year = int(input("Kakoi God?"))
def f (year):
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        print ("God visokosni")
    else:
        print ("God  ne visokosni")
f(year)
'''

color1 = input("kakoi 1 color?").lower()
color2 = input("kakoi 2 color?").lower()
colors = {"красный" ,"синий","желтый"}
if color1 not in colors or color2 not in colors:
    print("net varianta")
else:
    if (color1 == "красный" and color2 == "синий") or (color2 == "красный" and color1 == "синий"):
        print("Fioletoviy")
    elif (color1 == "красный" and color2 == "желтый") or (color2 == "красный" and color1 == "желтый"):
        print ("Orange")
    elif (color1 =="желтый" and color2 == "синий") or (color2 =="желтый" and color1 == "синий"):
        print("Green")
    else:
        print ("vvel odni color")
