from timeit import default_timer as timer
import random

def builtinDataTypes() :
    num = 7 # int
    f_num = 7.2 # float
    the_str= "CS301 Tutorial" # string (can also use ') 
    cond = True  # boolean (first letter capital)
    print(num, f_num, the_str, cond)
    num = "7" 
    print("num variable after change of reference :" , num, "\n")

def conditionals() :
    num = 7
    if num < 10 :
        print("Num is smaller than 10\n")
    elif num == 10 :
        print("Num is 10\n")
    else :
        print("Num is greater than 10\n")

def looping () :
    cnt = 0
    print("While loop")
    while cnt < 10 :
        print(cnt,end = " ")
        cnt = cnt + 1 # no cnt++ :)

    print("\n\nFor loop")
    for num in range(0,10) :
        print(num, end = " ")
    print("\n")

def operators() :
    cond1 = True # "true" does not work
    cond2 = False
    if cond1 and cond2 :
        print("and is not working as expected\n")
    elif cond1 or cond2 :
        print("or is working as expected\n")
    if not cond2 :
        print("not is working as expected\n")


def containerList () :
    my_list = [3,"CS301",7.2,True]
	# my_list = [] - for creating an empty list.
    print("List at the beginning : " , my_list)

    my_list.append("new item") # add an item to the end of the list.
    print("After an item added with append",my_list)

    my_list.insert(0,"first item changed") # change the item at location 1.
    print("After an item added with insert to 0th position",my_list)

    print("Last item was", my_list.pop(),"and it is popped")

    print("After pop :" , my_list)

    del my_list[3] # delete.
    print("After third item is deleted",my_list)

    numList=[6,8,2,4]
    print("List before sort",numList)

    numList.sort() # sorting function.
    print("List after sort",numList)

def containerDictionary () : # hashmap definition.
    my_dictionary = {"one" : 1 , "two" : 2} # be careful with the curly brackets (defines the hashmap).
    print("Dictionary : " , my_dictionary)
    print("Keys : ", my_dictionary.keys())
    print("Values ", my_dictionary.values())
    print("one :", my_dictionary["one"]) # instead of the index one can find the item with its key.

def inputing(): # gathering input.
    inp2 = input("Enter a number : ")
    print(type(inp2),"val :", inp2)
    num_inp2 = int(inp2)
    print(type(num_inp2), "val :", inp2)

def timing (): 
    i=256 # int(i) - converts i from string to int.
    while i < pow(2,20) :
        arr = []
        cnt = 0
        while cnt < i : # create an array with random i many element.
            arr.append(random.randint(0,i))
            cnt = cnt + 1
        start = timer()
        bubbleSort(arr)
        end=timer()
        print("Time passed for sorting ",i ," elements is : " , end - start)
        i=i*2
    

def main (): # "def" = function declaration - python does not execute this line.
    print("\nHello World")

    cont = input("Move on ?  \n")
    builtinDataTypes()

    cont = input("Move on ?  \n")
    conditionals()

    cont = input("Move on ?  \n")
    looping()

    cont = input("Move on ?  \n")
    operators()

    cont = input("Move on ?  \n")
    containerList()

    cont = input("Move on ?  \n")
    containerDictionary()

    cont = input("Move on ?  \n")
    inputing()

    cont = input("End ?\n")

if __name__ == "__main__":  # main function declaration, start from main.
    main()


