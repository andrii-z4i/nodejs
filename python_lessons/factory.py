# factory method

def get_instance(type_id, *args):
    def create_type_0(*args):
        return object()

    def create_type_1(*args):
        return object()

    def create_type_2(*args):
        return object()

    objects = {
        0: create_type_0,
        1: create_type_1,
        2: create_type_2 
    }

    if type_id in objects:
        print objects[type_id], args
        return objects[type_id](*args)

    return object()

    
objs = []
for i in range(3):
    p = get_instance(i, 100, 120, 130)
    objs.append(p)
    print p