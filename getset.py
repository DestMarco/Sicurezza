n=100000000

ds=[0 for i in range(0,n)]

for i in range (1,n):
    ds [i]=True
for i in range (0,n):
    ds[i]=False

input("Ti aspetto")


"""while True:
    cmd=input("Get o Set[G/S]:")
    if cmd == "G" or cmd =="g":
        pos =int(input("Posizione"))
        print(ds[pos])
    elif cmd == "S" or cmd =="s":
        pos=int(input("Posizione"))
        val=int(input("valore[0/1]:"))
        ds [pos] = True if val == 1 """