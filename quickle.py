import pickle


def get_obj(globals, locals, arg):
    try:
        try:
            obj = locals[arg]
        except:
            obj = globals[arg]
        return obj
    except:
        print('Invalid variable name entered:', arg)
        raise TypeError
    


def save(globals, locals, filename, *args):
    get = lambda arg: get_obj(globals, locals, arg)
    objs = tuple(map(get, args))
    objs_dict = dict(zip(args, objs))
    file = open(filename, 'wb')
    pickle.dump(objs_dict,file)
    file.close()


def load(locals, filename, *args):
    file = open(filename, 'rb')
    objs = pickle.load(file)
    file.close()
    get_obj = lambda arg: objs[arg]
    objs_tuple = tuple(map(get_obj, args))
    for i in range(len(args)):
        locals[args[i]] = objs_tuple[i]
        



