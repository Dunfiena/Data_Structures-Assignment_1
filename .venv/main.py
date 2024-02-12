from Data_structure import data


if __name__ == '__main__':
    #Create data structure with type 'i' (integer)
    arr = data('i')


    #Append test
    print("\nAppend test: \n--------------------------------")
    arr.append(12)
    arr.append(1)
    arr.append(4)
    arr.append(9)
    arr.append(11)
    arr.print()


    #Prepend Test
    print("\nPrepend test:\n-------------------------------- ")
    arr.prepend(4)
    arr.print()


    #Head print test
    print("\nHead test: \n--------------------------------")
    print(arr.head())


    #Tail print test
    print("\nTail test: \n--------------------------------")
    print(arr.tail())


    #Pop test
    arr.pop()
    print("\nPop test: \n--------------------------------")
    arr.print()


    #Index test
    print("\nIndex test:\n--------------------------------")
    print(arr.index(0))
    print(arr.index(2))

    #Size test
    print("\nSize test: \n--------------------------------")
    print(arr.size())

    #Contains test
    print("\nContains test: \n--------------------------------")
    print(arr.contains(4))
    print(arr.contains(42))
    print(arr.contains(9))

    #Find test
    print("\nFind test: \n--------------------------------")
    index, value = arr.find(9)
    print("index: ", index, "   value: ", value)




