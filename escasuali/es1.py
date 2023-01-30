def my_fun (n):
    my_list_1 = [0]
    my_list_2 = [1]
    for i in range(n):
        print ("___\n")
        print ("i = {}" .format (i))
        print (i+i)
        print (i*i)
        print (i**i)
        print ("___")
        print ("")
        print ("...")
        print ("")
        my_list_1.append(i)
        my_list_2.append(i**i)
        
    my_sum (my_list_1, 0)
    my_diff (my_list_2, 0)
    

def my_sum (my_list, sum):
    for item in my_list:
        sum = sum + item
    print ("§§§")
    print ("")
    print (sum)
    print ("")
    print ("§§§")
    print ("")
    return (sum)

def my_diff (my_list, diff):
    for item in my_list:
        if (item == 9**9):
            diff = diff + item
        else:
            diff = diff - item
        
    print ("@@@")
    print ("")
    print (diff)
    print ("")
    print ("@@@")
    return (diff)
    
    
my_fun(10)