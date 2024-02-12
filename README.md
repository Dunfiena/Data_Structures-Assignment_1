# Data Structures #
## Assignment 1 ##

You said you weren't super familiar with python, so I wanted to give you a little guidance:
in the .venv directory, you will find the two .py files.  these are the main method, and the data class


### Class and constructor ###
In python, the class constructor is going to be written as an __init__(self): function.  Then we add a array_type which lets us pick what kinds of variables can be stored in the array.

<img width="369" alt="image" src="https://github.com/Dunfiena/Data_Structures-Assignment_1/assets/117761149/445ee7f6-dc55-4ec6-8317-50008ef3d63e">


### Append & Prepend ###
Failry self-explanatory append and insert at index 0

<img width="263" alt="image" src="https://github.com/Dunfiena/Data_Structures-Assignment_1/assets/117761149/8189f47f-f00b-4319-a100-1b8e23d9a179">


### Print Size, print contents ###
For getting the size of an array in python, we can use the len(x) function

<img width="198" alt="image" src="https://github.com/Dunfiena/Data_Structures-Assignment_1/assets/117761149/1c2a4301-46e6-4644-850c-882a7f1e561e">
<img width="216" alt="image" src="https://github.com/Dunfiena/Data_Structures-Assignment_1/assets/117761149/ec83883f-df4e-4a10-8957-31bb30975047">



### Array Accessing with head, tail and index ###
Python has an interesting aspect that I haven't seen in other languages, where the tail of the array is access by -0 instead of -1
<img width="216" alt="image" src="https://github.com/Dunfiena/Data_Structures-Assignment_1/assets/117761149/12571481-fece-4ca6-b721-23bc4905233d">


### Pop ###
Set the last value = to pop gets rid of the last value

<img width="353" alt="image" src="https://github.com/Dunfiena/Data_Structures-Assignment_1/assets/117761149/aeb6d0bf-1956-4c6b-9b2a-4ae2e7c46f4d">


### Searching ###
This gets interesting again, the contains function runs as return item in array. This will check if the item is in the array and return a boolean.
The index is also interresting for the ability to return two values, which I'll show later. First, you can see that the for loop has two values:
1) index is the number of iterations till the goal is met.
2) is the value of the node in the array.

After this we return both the item and the index

<img width="313" alt="image" src="https://github.com/Dunfiena/Data_Structures-Assignment_1/assets/117761149/7286d5d7-a374-40bf-a61d-7239907ac684">

### main.py ###
The main function in python is written as if __name__ = '__main__':

<img width="316" alt="image" src="https://github.com/Dunfiena/Data_Structures-Assignment_1/assets/117761149/46cb8861-a5b6-4957-9ac2-86007959831a">

### Each kind of function implemented ###
________________________________________________________________________________

<img width="379" alt="image" src="https://github.com/Dunfiena/Data_Structures-Assignment_1/assets/117761149/ab31a31c-b65b-4d9f-881b-719a46a54186">
<img width="218" alt="image" src="https://github.com/Dunfiena/Data_Structures-Assignment_1/assets/117761149/f452b78e-6f09-409d-988c-03cbb68a7fe6">

________________________________________________________________________________


<img width="379" alt="image" src="https://github.com/Dunfiena/Data_Structures-Assignment_1/assets/117761149/b03b2f24-45e4-4d70-b483-6f3e22ec6aa1">
<img width="218" alt="image" src="https://github.com/Dunfiena/Data_Structures-Assignment_1/assets/117761149/d526e3a4-26ae-4d20-b608-290e69847937">

________________________________________________________________________________

<img width="381" alt="image" src="https://github.com/Dunfiena/Data_Structures-Assignment_1/assets/117761149/29a411d1-e3fd-4246-b5e7-67367c79576a">
<img width="213" alt="image" src="https://github.com/Dunfiena/Data_Structures-Assignment_1/assets/117761149/db718d62-6112-4317-a45e-9c6a9e55d7f9">

________________________________________________________________________________

<img width="368" alt="image" src="https://github.com/Dunfiena/Data_Structures-Assignment_1/assets/117761149/b38d0785-345c-48e8-8e40-bfb412c38312">
<img width="219" alt="image" src="https://github.com/Dunfiena/Data_Structures-Assignment_1/assets/117761149/528c8f1c-4bcb-4ba0-acd2-7068eed5e2ef">

________________________________________________________________________________

<img width="372" alt="image" src="https://github.com/Dunfiena/Data_Structures-Assignment_1/assets/117761149/455eb224-ad0e-49be-be1d-e8aa97aaa865">

<img width="210" alt="image" src="https://github.com/Dunfiena/Data_Structures-Assignment_1/assets/117761149/aee18682-47a0-4ffb-9177-37090733c316">

________________________________________________________________________________

<img width="363" alt="image" src="https://github.com/Dunfiena/Data_Structures-Assignment_1/assets/117761149/b3ed4dd7-95df-468e-a06b-8676dd1bc012">
<img width="217" alt="image" src="https://github.com/Dunfiena/Data_Structures-Assignment_1/assets/117761149/88f5d11d-2393-4ca6-aa11-f66de6a23b84">

________________________________________________________________________________

<img width="374" alt="image" src="https://github.com/Dunfiena/Data_Structures-Assignment_1/assets/117761149/594bc5d2-d4ac-4197-a36a-bfd7324bcabb">
<img width="226" alt="image" src="https://github.com/Dunfiena/Data_Structures-Assignment_1/assets/117761149/cb5c3393-3d56-4b40-814b-0dba866033d8">

________________________________________________________________________________

<img width="400" alt="image" src="https://github.com/Dunfiena/Data_Structures-Assignment_1/assets/117761149/1a7774af-8295-422b-b166-239aef4f006b">
<img width="229" alt="image" src="https://github.com/Dunfiena/Data_Structures-Assignment_1/assets/117761149/673a62cc-ebe8-4bc7-9b4c-c0e8ff5d9851">

________________________________________________________________________________

<img width="427" alt="image" src="https://github.com/Dunfiena/Data_Structures-Assignment_1/assets/117761149/8c9f9a6e-3207-4e01-a224-2f86708e62e3">

<img width="246" alt="image" src="https://github.com/Dunfiena/Data_Structures-Assignment_1/assets/117761149/af1a339c-0c8a-454d-beaf-d05f3dbd30f3">



