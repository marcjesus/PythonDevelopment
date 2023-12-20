**List** : A list is an ordered and changeable sequence of elements. It can hold integers, objects, etc.. 

**Dictionary** : A dictionary stores data values in key-values pairs. Dictionaries can be an array.

**Tuple**  : A tuple is similar to a list but it’s immutable, unlike a list which is mutable.

**Loops** : There are two main types of loops: ‘for’ and ‘while’ loops. 
A for loop is used to iterate over a sequence (that can be a list, tuple, dictionary, string, or other iterable objects) and execute a block of code for each element in the sequence.
A while loop is used to repeatedly execute a block of code as long as a condition is True. It continues iterating until the condition becomes False.

**Functions** : Function annotations and type hints allow you to provide additional information about function arguments and return values. They enhance code readability and help catch potential type-related errors during development. 

**Recursion** : When a defined function can call itself we call it recursion. This has the benefit of meaning that you can loop through data to reach a result. Every recursive function must have a base case, which defines the simplest version of the problem. When the function reaches the base case, it stops calling itself and starts returning values back up the chain of recursive calls.

**Shallow copy** : A shallow copy creates a new compound object and then adds a reference to the object found in the original, as a result, if the elements inside the original object are mutable, changes made to these elements will affect both the original object and the shallow copy. A deep copy creates a new object and creates a new copy of objects whose changes made to the objects inside the deep copy do not affect the original object, and vice versa. 

**Objects** : Objects are variables that contain data and functions that can be used to manipulate the data. A class is a code template for creating objects.We can check whether an object is an instance of a class by using the isinstance function, which will return True or False depending on whether the given object does indeed belong to the given class. A class method is a method that is bound to the class and not the object of the class, basically it’s a function written inside a class. 

**Method** : A method is a function that “belongs to” an object. List of objects have methods called append, insert, remove, sort, etc…

**Instance** : The variables that are defined inside of any class function are known as instance attributes.

**Inheritance** : Inheritance allows us to define a class that inherits all the methods and properties from another class. Parent class is the class being inherited from, also called base class. Child class is the class that inherits from another class, also called derived class. pass can be used in class or method definitions to indicate that it's intentional for the definition to do nothing. 

**Method overriding** : Method overriding is the practice of re-implementing a method in a child class. 

**Composition (Has-A)** : It’s possible to access the member of one class inside a class using composition(Has-A relation) by using the class name or by creating an object. It enables creating complex types by combining objects of other types. This means that a class Composite can contain an object of another class Component. 
To create has-a relationships in our code, we can use instance variables to refer to the related object.

**Aggregation** : Aggregation refers to a relationship between two classes where one class contains an object of another class. It is a way to achieve code reusability and maintainability by creating complex objects using simpler ones. 

**Arguments** :  An argument or parameter is information that is passed into a function. It’s the variable listed inside the parentheses in the function definition. Special symbols used for passing arguments in Python are : *args (Non-keyword Arguments), **Kwargs (Keyword arguments). A keyword argument is where you provide a name to the variable as you pass it into the function. 

**Constructors** : The task of constructors is to initialise (assign values) to the data members of the class when an object of class is created. In python __init()__ method is called the constructor and is always called when an objcect is created. It’s possible to store information in instances if the variable is initialised under __init__.  

**Encapsulation** : Encapsulation describes the act of combining data with the matching methods into a single entity.

**Self** : The self is used to represent the instance of the class. It binds the attributes with the given arguments. We have to pass the self parameter in an argument, and the argument needs to be the object we’re wanting to use the method with. 

**Super** : It’s used to give access to methods and properties of a parent or sibling class. The super() function returns an object that represents the parent class. Not every class will need to call super(), but when making a subclass of a class does some complicated setup, probably will need to use the super function to get at the methods of the parent class in order to be able to call them as part of the child class. 

**Wrapper** : A wrapper It’s a piece of code that is used to modify or extend the behaviour of an existing function, method, or class without modifying its source code.

