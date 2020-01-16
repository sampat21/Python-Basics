class Stack:    # defining the Stack class
    def __init__(self):    # defining the constructor function
        print("Hi!")

stackObject = Stack()    # instantiating the object



'''
1. the constructor's name is always __init__;
2. it has to have at least one parameter (we'll discuss this later); the parameter is used to represent the newly created object - you can use the parameter to manipulate the object, and to enrich it with the needed properties; you'll make use of this soon;

note: the obligatory parameter is usually named self - it's only a convention, but you should follow it - it simplifies the process of reading and understanding your code.
'''