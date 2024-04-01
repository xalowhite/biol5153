size = int(input("Enter the size of your table: " ))
for i in range(1,size+1):
    for j in range(1, size+1):
        print('{:4d}'.format(i *j), end = "")
    print()