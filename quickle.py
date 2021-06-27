import pickle

#Finds the variable associated with a variable name
def get_obj(globals, locals, arg):
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
def save(globals, locals, filename, *args):
    get = lambda arg: get_obj(globals, locals, arg)
    objs = tuple(map(get, args))
    objs_dict = dict(zip(args, objs))
    file = open(filename, 'wb')
    pickle.dump(objs_dict,file)
    file.close()

#Loads objects from file and unpickles them        
def _load(filename, *args):
    file = open(filename, 'rb')
    objs = pickle.load(file)
    file.close()
    get_obj = lambda arg: objs[arg]
    objs_tuple = tuple(map(get_obj, args))
    return objs_tuple

#Loads objects directly into locals
def implicit_load(locals, filename, *args):
    objs_tuple = _load(filename, *args)
    for i in range(len(args)):
        locals[args[i]] = objs_tuple[i]

#Returns an object or tuple of unpickled object
def explicit_load(filename, *args):
    objs_tuple = _load(filename, *args)
    if len(objs_tuple) > 1:
        return objs_tuple
    else:
        return objs_tuple[0]

