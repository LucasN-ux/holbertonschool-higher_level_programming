# Everything is an Object in Python

![Python objects diagram](python_objects_diagram.svg)

## Introduction

This project made one idea impossible to ignore: in Python, almost everything is an object. Numbers, strings, lists, tuples, functions, and even classes all have an identity, a type, and a place in memory. That changes how you reason about variables, because a variable does not store the value directly in the way many beginners imagine; it points to an object. A quick example shows the mindset shift:

```python
a = 10
b = a

print(a)
print(b)
print(a is b)
print(id(a))
print(id(b))
print(type(a))
```

```text
10
10
True
1400...
1400...
<class 'int'>
```

That simple output already says a lot. `a` and `b` are different names, but they both reference the same integer object. The rest of the project kept returning to this same model: values are objects, and variables are references to those objects.

## Id and Type

`id()` and `type()` are two of the most useful tools for understanding Python’s object model. `id()` tells you the identity of the object, which is the thing the variable points to, while `type()` tells you what kind of object it is. If two variables have the same `id`, they refer to the same object; if they have the same `type`, they are objects of the same class, but not necessarily the same object.

```python
x = 42
y = 42
z = 42.0

print(id(x) == id(y))
print(type(x))
print(type(z))
print(x is y)
print(x == z)
print(x is z)
```

```text
True
<class 'int'>
<class 'float'>
True
True
False
```

This is where `is` and `==` stop meaning the same thing. `is` checks identity, while `==` checks value equality. Two different objects can compare equal, and two names can point to the exact same object. That distinction becomes important throughout the rest of the project.

## Integer Pre-allocation in CPython

CPython pre-allocates a small range of integer objects at startup. In the source code, these limits are controlled by two constants: `NSMALLNEGINTS` and `NSMALLPOSINTS`.

- `NSMALLNEGINTS = 5`
- `NSMALLPOSINTS = 257`

This means integers from `-5` to `256` are created once and reused, which gives `262` cached integers in total.

```python
a = 256
b = 256

print(a is b)  # usually True in CPython

x = int("257")
y = int("257")

print(x is y)  # usually False
print(x == y)  # True
```

```text
True
False
True
```

How these constants are used: when CPython needs an int in the cached range, it reuses an existing object instead of allocating a new one.

Why those values: these are the most frequently used integers in real programs (indexes, lengths, counters, flags, small offsets), so caching them reduces allocations and improves runtime performance.

## Mutable Objects

Mutable objects can change after they are created. Lists, dictionaries, and sets are the clearest examples. If two variables point to the same mutable object, a change through one name is visible through the other name because both names still point to the same object.

Common mutable built-in objects:
- `list`
- `dict`
- `set`
- `bytearray`

```python
my_list = [1, 2, 3]
alias = my_list

alias.append(4)

print(my_list)
print(alias)
print(my_list is alias)
```

```text
[1, 2, 3, 4]
[1, 2, 3, 4]
True
```

The same idea applies to dictionaries and sets:

```python
data = {"name": "Ada"}
same_data = data

same_data["language"] = "Python"

print(data)
print(same_data)
```

```text
{'name': 'Ada', 'language': 'Python'}
{'name': 'Ada', 'language': 'Python'}
```

Mutability is powerful, but it also creates subtle bugs when you forget that a function or another variable may be holding the same object.

## Immutable Objects

Immutable objects cannot be changed in place. Integers, floats, strings, tuples, and frozensets are the main examples covered here. If you “modify” one of these objects, Python actually creates a new object instead of editing the old one.

Common immutable built-in objects:
- numbers: `int`, `float`, `complex`
- `str`
- `tuple`
- `frozenset`
- `bytes`

```python
name = "Python"
new_name = name.upper()

print(name)
print(new_name)
print(name is new_name)
```

```text
Python
PYTHON
False
```

Tuples follow the same rule. You cannot change an element inside a tuple, because the tuple itself is immutable:

```python
point = (3, 4)
# point[0] = 10  # TypeError

print(point)
print(type(point))
```

```text
(3, 4)
<class 'tuple'>
```

This matters because immutable objects behave predictably in shared references: if a name “changes” to a new value, it now points to a different object rather than updating a shared object in place.

## Special Case: Immutable Container, Mutable Content

Tuples and frozensets are immutable containers, but they can still contain mutable objects. The container identity and structure stay fixed, while an inner mutable object can still change.

```python
t = ([1, 2], "immutable shell")
f = frozenset({("x", 1), ("y", 2)})

t[0].append(99)

print(t)
print(type(f))
```

```text
([1, 2, 99], 'immutable shell')
<class 'frozenset'>
```

You still cannot rebind tuple positions or modify a frozenset itself, but mutable items referenced inside a tuple can be mutated through their own methods.

## Why It Matters

Python treats mutable and immutable objects differently because the language optimizes for clarity, safety, and flexibility at the same time. With immutable objects, Python can safely reuse objects, compare values cleanly, and avoid accidental side effects. With mutable objects, Python lets you update state efficiently, but you must be careful about aliasing and shared references. That is why `is` and `==` are not interchangeable, and why slicing, copying, and reassignment are not the same thing.

```python
a = [1, 2]
b = a
c = a[:]

print(a is b)
print(a is c)
print(a == c)

b.append(3)
print(a)
print(c)
```

```text
True
False
True
[1, 2, 3]
[1, 2]
```

The first two variables share the same list. The sliced copy is a different list with the same values. That difference is the practical heart of the project: object identity and object value are separate ideas, and Python uses both.

## How Arguments Are Passed

Python passes arguments by assignment, which means a function receives a new local name bound to the same object that the caller passed. The function does not get a magical copy unless you explicitly create one. With mutable objects, that means the function can mutate the original object. With immutable objects, the function cannot change the caller’s object in place, so reassignment only affects the local name.

```python
def add_item(items):
    items.append(99)


numbers = [1, 2, 3]
add_item(numbers)

print(numbers)
```

```text
[1, 2, 3, 99]
```

Now compare that with an immutable value:

```python
def add_one(number):
    number += 1
    print("inside:", number)


value = 10
add_one(value)

print("outside:", value)
```

```text
inside: 11
outside: 10
```

Inside the function, `number` points to a new integer object after the addition. The original integer outside the function stays unchanged. This is the main implication of Python’s argument passing model: functions can mutate shared mutable objects, but rebinding a parameter never changes the caller’s variable itself.

## What I Learned From the Advanced Tasks

The advanced task around copying lists made the object model feel real instead of abstract. I implemented a list copy with slicing and tested how the original list and the copied list behave differently:

```python
def copy_list(my_list):
    return my_list[:]
```

```python
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
new_list = copy_list(my_list)

print(my_list)
print(new_list)
print(new_list == my_list)
print(new_list is my_list)
```

```text
[1, 2, 3]
[1, 2, 3]
True
False
```

That exercise taught me the exact difference between “same content” and “same object.” I also learned that copying a list only creates a shallow copy, which is fine for a flat list but still shares nested objects. That detail is easy to miss until you experiment with it:

```python
original = [[1, 2], [3, 4]]
clone = original[:]

clone[0].append(99)

print(original)
print(clone)
print(original is clone)
print(original[0] is clone[0])
```

```text
[[1, 2, 99], [3, 4]]
[[1, 2, 99], [3, 4]]
False
True
```

That is the kind of lesson this project delivers: Python’s object model is not just theory, it explains the output of real code. Once you understand identity, type, mutability, and argument passing, a lot of Python behavior becomes much easier to predict.