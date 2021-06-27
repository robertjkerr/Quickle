# Quickle

### A Python "quick pickle" module

Allows you to store variables and objects quickly and easily, inspired by the "save" and "load" functions in MathWorks MATLAB.

To save two variables `a` and `b`, first, writing the following wrapper is advisable:
```
import quickle

save = lambda filename, *args: quickle.save(globals(), locals(), filename, *args)
```

Then use `save` exactly as used in MATLAB, except replacing he `.mat` file extension with `.pkl`, e.g.:
```
a = 1
b = [1, 2, 3]

save('save_name.pkl', 'a', 'b')
```
This pickles the variables/objects in `save_name.pkl`.


To load the objects into the workspace, there are two options. First is to create a wrapper for `implicit_load()`:
```
load = lambda filename, *args: quickle.implicit_load(locals(), filename, *args)
```

This can be used exactly as in MATLAB, but with `.pkl`:
```
load('save_name.pkl', 'a', 'b')

print(a, b)
```
However, although this works in practice, your editor may dislike that the loaded variables haven't been explicitly defined, and you will see a 'variable undefined' error.  

In solution to this, you can use `explicit_load`, which, explicitly assigns the loaded objects to names:
```
load = lambda filename, *args: quickle.explicit_load(filename, *args)

a, b = load('save_name.pkl', 'a', 'b')
```
This is dissimilar to the MATLAB function, but doesn't throw the 'undefined variable' error.

Congrats, you've just quickled some objects!

