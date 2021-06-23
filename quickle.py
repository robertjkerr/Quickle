import pickle


def get_obj(globals, locals, arg):
    try:
        try:
            obj = locals[arg]
        except:
            obj = globals[arg]
    except:
        print('Invalid variable name entered:', arg)
        raise TypeError
    return obj


def quickle_save(globals, locals, filename, *args):
    get = lambda arg: get_obj(globals, locals, arg)
    objs = tuple(map(get, args))
    objs_dict = dict(zip(args, objs))
    file = open(filename, 'wb')
    pickle.dump(objs_dict,file)
    file.close()


def load(filename, *args):
    file = open(filename, 'rb')
    objs = pickle.load(file)
    file.close()
    get_obj = lambda arg: objs[arg]
    objs_tuple = tuple(map(get_obj, args))
    return objs_tuple



