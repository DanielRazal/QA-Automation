# r - read only

f = open('rundev.log','r')

x = f.readlines()

for i in x:
    print(i)

f.close()