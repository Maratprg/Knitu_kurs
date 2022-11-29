# This is a sample Python script.
def all_symbols():
    for i in range(97, 120): print(chr(i) , i)

def k_output(mask, my_income):
    if (mask^0b1010 == 0b1111):
        i=0
        while (i < len(my_income)):
            print(chr(my_income[i]), end='')
            i += 1

#all_symbols()

#104 101 108 108 111 32 119 111 114 108 100
my_list = [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]
k_output(0b0101, my_list)


