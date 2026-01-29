## Python Introduction

#### Feb 2026

Toby Dussek

* 9:30 start
* 11:00 coffee until 11:15
* 12:00 Lunch until 1:00
* 3:00 tea until 3:15
* 4:30 end

All my code will be here:
  https://github.com/onionmccabbage/pythonIntroFeb2026

### Monday
- Welcome and intros
- where to write code: module (just a file) or immediate python
- architecture, structure, and professional code best practice
- print() and input()
- maths operators and data types
- indentation
- immutable strings
- lists and tuples (and memory efficiency)
- identifiers
- boolean True and False
- type and type conversion
- the if statement for conditional logic
- for, while, break and pass
- print formatting
- validate input (remember - all input is string)
- after lunch review exercise
- dictionaries (indexed iterable collections)
- import, libraries and modules
  to see what libraries are already installed: pip list
- functions
- packages (sinply a folder containing python files)

### Tuesday
- how to access course recordings
- if __name__ == '__main__'
- range, generators
- comprehensions
- to add libraries to python:
  - python -m ensurepip
  - python –m pip install requests (or any other library you need)
  or 
  - pip3 install requests
- using requests (to access web API via HTTP)
- strings with triple quotes
- exception handling (try-except etc.)
- debug tools   
- review exercise
- File input and output
- the nature of file access objects

### Wednesday
- quick review of where we got to
- in Python EVERTHING is an Object - every function, every class every module....
- any input or output is necessarily slow: I/O bound
- anything with __nnn__ is part of python (built in features) called 'dunder'
- functions live in classes, which live in modules which live in packages
- custom generator and yield
- global and local scope 
- data modelling structures: 
    use built in structures until they do not suit the purpose (then use classes)
- Objects and Classes (OOP)
  classes have properties (something belonging to the class) and methods (something the class can do)
- get/set as property decorators @property
- name mangling (__) and __slots__
- properties, methods, __str__
- inheritance
- we have no direct control over memory management in Python
  - we may choose efficient structures - e.g. always use a tuple unless you MUST use a list
  - remember to close file access (or use 'with')
  - we can reduce reliance on global objects (write as much code as possible within code blocks suc has functions or classes)
- review exercise
- end of course feedback


- where to go from here:
  https://learnpython.org/
  https://pynative.com/python-exercises-with-solutions/
  https://python.land

- Python official site https://python.org
- PEP8 style guide https://pep8.org/