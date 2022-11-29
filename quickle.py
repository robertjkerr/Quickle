import pickle as _pickle
import bz2 as _bz2

#Finds the variable associated with a variable name
def _get_obj(globals, locals, arg):
    try:
        try:
            obj = locals[arg]
        except:
            obj = globals[arg]
            return obj
    except:
        print('Invalid variable name entered:', arg)
        raise ValueError

#Pickles objects
def qsave(globals, locals, filename, *args, **kwargs):
    objs = (_get_obj(globals, locals, arg) for arg in args)
    objs_dict = dict(zip(args, objs))

    try:
        nocompress = kwargs['nocompression']

        if not isinstance(nocompress, bool):
            print("'nocompression' keyword argument must be a boolean")
            raise TypeError
    except:
        nocompress = False

    if nocompress:
        with open(filename, 'wb') as file:
            _pickle.dump(objs_dict, file)
    else:
        with _bz2.BZ2File(filename, 'wb') as file:
            _pickle.dump(objs_dict, file)

#Loads objects from file and unpickles them        
def load(filename, *args):
    try:
        with open(filename, 'rb') as file:
            objs = _pickle.load(file)
    except:
        with _bz2.BZ2File(filename, 'rb') as file:
            objs = _pickle.load(file)

    objs_tuple = tuple([objs[arg] for arg in args])

    if len(objs_tuple) > 1:
        return objs_tuple
    else:
        return objs_tuple[0]
