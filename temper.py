#TemperConvert.py
for i in range (3):
    val = input("Please input a number(for exameple 32C): ")
    if val[-1] in ['C', 'c']:
        f = 1.8*float(val[0: -1]) + 32
        print("The convert num %fF" %f);
    elif val[-1] in ['F', 'f']:
        c = (float(val[0: -1]) - 32) / 1.8
        print("The convert number %fC" %c)
    else:
        print("The intput num is error")

    
        
