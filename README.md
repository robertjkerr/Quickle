# Quickle

### A Python "quick pickle" module

Allows you to store variables and objects quickly and easily, inspired by the "save" and "load" functions in MathWorks MATLAB.

To save two variables `a` and `b`, first, writing the following wrapper is advisable:
```
from quickle import qsave

save = lambda filename, *args: qsave(globals(), locals(), filename, *args)
```

Then use `save` exactly as used in MATLAB, except replacing he `.mat` file extension with `.pkl`, e.g.:
```
a = 1
b = [1, 2, 3]

save('save_name.pkl', 'a', 'b', nocompression=False)
```
This pickles the variables/objects in `save_name.pkl`. The keyword argument `nocompression` (default `False`) will disable BZ2 file compression if `True`.


The method to load saved objects is different to MATLAB, as the called objects have to be explicitly assigned to variables. But, otherwise the process is the same; provide the file name and the names of the objects to be loaded:

```
from quickle import load

a, b = load('save_name.pkl', 'a', 'b')
```

The file will automatically be decompressed if required.

Congrats, you've just quickled some objects!

