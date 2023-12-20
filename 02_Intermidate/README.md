**Decorators** : Decorators allow you to modify the behaviour of functions or classes. They provide a clean and efficient way to add functionality to existing code without modifying it directly. 

**Instance method** : Instance Methods are the most common type of methods in Python classes. They operate on an instance of the class and have access to the instance itself through the ‘self’ parameter. Instance methods can access and modify instance variables and are typically used for actions that depend on the attributes of the instance. 

**Static method** : Static Methods are defined using the ‘@staticmethod’ decorator. They don’t operate on instances or class variables. They are bound to the class and can be called on the class itself. Static methods are often used for utility functions that don’t depend on instance or class state.

**Class method** : Class Methods are defined using the ‘@classmethod’ decorator. They operate on the class itself and have access to the class and its attributes through the ‘cls’ parameter. Class methods are often used for methods that need to access or modify class-level attributes.   

**Duck typing** : A duck typing language means the data types of variables can change as long as the syntax is compatible. In other words, when you are working with objects in Python, you don’t need to check their types explicitly. 

**Abstract classes** : Abstract classes are classes that contain one or more abstract methods. An abstract method is a method that is declared, but contains no implementation. Abstract classes cannot be instantiated and require subclasses to provide implementation for the abstract method. 
Abstract classes are useful when you want to provide a common interface for all the classes in a specific category, but you want to enforce that the child classes provide specific implementation for certain methods. Abstract classes ensure that the derived classes implement the abstract methods, making your code more organised and maintainable.


**Destructors** :  A Destructor is a special method called ‘__del__’ that is used to clean up resources or perform other cleanup operations when an object is no longer in use or when the program exits. 

**Overloading** : Overloading is when two or more methods have the same name but different numbers of parameters or different types of parameters, or both. 

**Iterator** : An Iterator is an object that represents a stream of data. It adheres to the iterator protocol, which consist of two methods: ‘_ _ iter _ _ ()’ and  ‘_ _ next _ _ ()’. Iterators are used to loop through a collection of elements, one at a time, and are often more memory-efficient than storing the entire collection in memory. 

The difference between for loop it’s an iterator can modify a collection, which means removing an element or changing the content of an item stored in the collection. 

**Generator** : A generator It’s a function that returns an iterator that  produces a sequence of values when iterated over. Generators are useful when we want to produce a large sequence of values, but we don’t want to store all of them in memory at once. Generators provide a memory-efficient way to generate sequences of values on the fly. Unlike lists, which store all elements in memory, generators produce values one at a time, conserving resources

**Assert** : The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.

**Lambda** : Lambda functions, also known as anonymous functions, are concise one-line functions that don’t require a `def` statement. They are useful for writing small, single-use functions.

**Multithreading/multiprocessing** : Multithreading and Multiprocessing allows you to execute multiple tasks concurrently, enabling efficient utilisation of system resources and improved performance.

**Metaclasses** : Metaclasses provide a way to define the behaviour of classes themselves. They allow you to customise class creation and can be used for advanced purposes such as creating Domain Specific Languages or implementing frameworks.

**Closures** : Closure is a nested function that allows us to access variables of the outer function even after the outer function is closed.

**Regular expressions** : Regular expressions are sequences of characters that define a search pattern. They are used for pattern matching within strings and are incredibly powerful for text processing and manipulation. 

**Properties** : Properties are a way to control the access, modification, and deletion of class attributes. They allow you to define methods that can be accessed like attributes, providing a way to encapsulate the internal state of an object. Properties are created using the ‘property()’ function or the ‘@property’ decorator.

**Exception handling** : Exception handling enables you to gracefully handle errors and exceptions that may occur during program execution. By catching and handling exceptions, you can prevent your program from crashing.

**List Comprehensions** : List comprehension is an elegant way to define and create lists based on existing lists. List comprehension is generally more compact and faster than normal functions and loops for creating list:

**Walrus operator** : The walrus operator offers a way to accomplish two tasks at once: assigning a value to a variable, and returning that value.