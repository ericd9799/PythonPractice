# PythonPractice
* Numeric: Integer or float
* String: Immutable, sequence of characters
* List: Mutable 
* Tuple: Immutable 
* Dictionary: Key, value mapping

* break: Breaks out of the current closest enclosing loop
* continue: Goes to the top of the closets enclosing loop
* pass: Does nothing at all

* zip: zip together elements of list to form tuple. zip will only go as far as matching number of items in all lists.

* list take third parameter for step size.

* *args - argument; allow to pass in as many arguments as want; arguments treated as tuple; "args" is arbitrary name
```python
def myFunc(*args):
  return sum(args) * 0.05
```
* **kwargs - keyword argument; treated as dictionary; "kwargs" is arbitrary name
```python
def myFunc(**kwargs):
  if 'fruit' in kwargs:
    print('My fruit of choice is {}'.format(kwargs['fruit']))
    
myFunc(fruit = 'apple', veggie = 'lettuce')
```

* able to set argument default when initializing arguments in function name line.
```python
def myFunc(a, b, c = 0, d = 0):
  return sum((a, b, c, d)) * 0.05
```
