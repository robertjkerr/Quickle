# Quickle

### A Python "quick pickle" module

Allows you to store variables and objects quickly and easily, inspired by the "save" and "load" functions in MathWorks MATLAB.

For two variables `a` and `b`, to save them:  
`from quickle import quickle_save`  
`save = lambda *args: quickle_save(globals(), locals(), *args)`  
`save('file_name.pkl', 'a', 'b')`  

To load variables:  
`from quickle import load`  
`(a, b) = load('file_name.pkl', 'a', 'b')`  
