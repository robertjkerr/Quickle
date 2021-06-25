# Quickle

### A Python "quick pickle" module

Allows you to store variables and objects quickly and easily, inspired by the "save" and "load" functions in MathWorks MATLAB.

To save two variables `a` and `b`, first write the following wrapper:
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

To load the objects into the workspace, create another wrapper:
```
load = lambda filename, *args: quickle.load(locals(), filename, *args)
```
Once again, use the same as in MATLAB, but with `.pkl`:
```
load('save_name.pkl', 'a', 'b')

print(a, b)
```

Congrats, you've just quickled some objects!

