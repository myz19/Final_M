total=1
base=3
power=4
num_times=0

while num_times<power:
    total = total * base    #can also do total*=base
    num_times = num_times + 1   #can also do num_times+=1 but cannot do num_times++

print("Value of " + str(base) + " to power " + str(power) + " = " + str(total))