import builtins
import inspect
from types import CodeType, LambdaType
import types


def isdict(a):
    a=a[1:len(a)-1]
    ret_obj={}
    recursiv=0
    lists=[]
    i=0
    while(len(a)>1 and i<len(a)):
        if(a[i]=='"'):
            skip=False
            for j in range(i,len(a)):
                if(a[j]!=',' or skip):
                    if(a[j]=='[' or a[j]=='{'):
                        recursiv+=1
                        skip=True
                    if(a[j]==']' or a[j]=='}'):
                        recursiv-=1
                        if(recursiv==0):
                            lists.append(a[i:j+1])
                            a=a[0:i]+a[j+3:len(a)]
                            i=-1
                            break
                else:
                    lists.append(a[0:j])
                    a=a[j+2:len(a)]
                    skip=False
                    i=-1
                    break

        i+=1
    if(a!=''):
        if(a[0]!='\''):
            temp_lists=a.split(', ')
            for i in temp_lists:
                lists.append(i)
    temp_lists=[]
    for i in range(len(lists)):
        temp_lists.append(list(''))
        j=0
        while(len(lists[i])>1 and j<len(lists[i])):
            if(lists[i][j]==':'):
                temp_lists[i].append(lists[i][0:j])
                lists[i]=lists[i][j+2:len(lists[i])]
                temp_lists[i].append(lists[i])
                j=-1
                break
            j+=1
    lists=temp_lists
    for i in range(len(lists)):
        ret_obj[loads(lists[i][0])]=loads(lists[i][1])
    return ret_obj

def islist(a):
    a=a[1:len(a)-1]
    b=a
    ret_obj=list()
    recursiv=0
    lists=[]
    i=0
    while(len(a)>1 and i<len(a)):
        if(a[i]=='[' or a[i]=='{'):
            for j in range(i,len(a)):
                if(a[j]=='[' or a[j]=='{'):
                    recursiv+=1
                if(a[j]==']' or a[j]=='}'):
                    recursiv-=1
                    if(recursiv==0):
                        lists.append(a[i:j+1])
                        a=a[0:i]+a[j+3:len(a)]
                        i=-1
                        break
        i+=1
    if(a!=''):
        temp_lists=a.split(', ')
        for i in temp_lists:
            lists.append(i)
    while(len(b)>0):
        for i in lists:
            skip=False
            k=0
            for j in range(len(i)):
                k=j
                if(i[j]!=b[j]):
                    skip=True
                    break
            if(skip==False):
                ret_obj.append(loads(i))
                b=b[k+3:len(b)]
    return ret_obj


def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

def dumps(a, rec=-100):
    if(rec>0): 
        Next=1
    elif(rec==0): 
        Next=1
    else: 
        Next=0
        rec=-100
    string=''

    if is_function(a):
        return serialize_function(a,rec)

    if is_class(a):
        return serialize_class(a)

    if isinstance(a, str):
        if(len(a)>1):
            if(a[0]=='{' or a[1]=='{' and a[len(a)-1]=='}'):
                return ''+a+''
            if(a[0]=='"' and a[len(a)-1]=='"'):
                return '\t'*(rec-1)+'"'"'"+a[1:len(a)-1]+"'"'"'
        if(len(a)==1):
            if(a[0]=='"' and a[len(a)-1]=='"'):
                return '\t'*(rec-1)+"'"
        return '\t'*(rec-1)+('"'+str(a)+'"')

    if isinstance(a, bool):
        if(a==True):
            return '\t'*(rec-1)+'true'
        else:
            return '\t'*(rec-1)+'false'
    if a is None:
        return '\t'*(rec-1)+'null'

    if isinstance(a, dict):
        string+=Next*'\n'+'\t'*(rec-1)+'{'+Next*'\n'
        for i in a:
            last=i
        for i in a:
            string+= '\t'*(rec)+'"'+str(i)+'": '
            string+= dumps(a.get(i),rec+1)
            if i != last:
                string+= ', '+Next*'\n'
        string+=Next*'\n'+'\t'*(rec-1)+'}'
        return string

    if isinstance(a, list) or isinstance(a, tuple):
        string+=Next*'\n'+'\t'*(rec-1)+'['+Next*'\n'
        for i in range(len(a)):
            last=i
        for i in range(len(a)):
            string+=dumps(a[i],rec+1)
            if i != last:
                string+= ', '+Next*'\n'
        string+=Next*'\n'+'\t'*(rec-1)+']'
        return string
    return '\t'*(rec-1)+str(a)

def loads(a, b=0):
    if isinstance(a, str):  
        a=a.replace('\n','').replace('\t','').replace('\\','')
    else:
        return a
    
    if(a=='true'):
        return True
    
    
    if(a=='false'):
        return False
    
    
    if(a=='null'):
        return None
    
    
    if(is_digit(a)):
        try:
            if(float(a).is_integer()):
                return int(a)
            else:
                return float(a)
        except ValueError:
            return float(a)

    if(len(a)>1):
        if(a[0]=="'" and a[len(a)-1]=="'"):
            return a[1:len(a)-1]
        if(a[0]=='"' and a[len(a)-1]=='"'):
            if(len(a)>3):
                if(a[1]=="'" and a[len(a)-2]=="'"):
                    return '"'+a[2:len(a)-2]+'"'
            return a[1:len(a)-1]
    if(a=='""'):
        return a
    if(a=='"'):
        return '"'
    
    if(len(a)>1):
        if(a[0]=='[' and a[len(a)-1]==']'):
            zxc=islist(a)
            return zxc
            

        if(a[0]=='{' and a[len(a)-1]=='}'):
            if(a[14:22]=='function' and b==1):
                zxc=deserialize_function(a)
            elif(a[17:22]=='class' and b==1):
                zxc=deserialize_class(a)
            else:
                zxc=isdict(a)
            return zxc

    return a

def serialize_iterable(obj):
    if isinstance(obj, list) or isinstance(obj, tuple):
        packed_iterable = []
        for value in obj:
            if value is None:
                packed_iterable.append('null')
            packed_iterable.append(dumps(value))
        return packed_iterable
    elif isinstance(obj, dict):
        packed_dict = {}
        for key, value in obj.items():
            packed_dict[key] = dumps(value)
        return packed_dict

def get_global_vars(func):
    globs = {}
    for global_var in func.__code__.co_names:
        if global_var in func.__globals__:
            globs[global_var] = func.__globals__[global_var]
    return globs

def is_iterable(obj):
    return getattr(obj, "__iter__", None) is not None

def serialize_function(obj, rec=-100):
    result = {"__type__": "function"}
    if inspect.ismethod(obj):
        obj = obj.__func__
    result["__name__"] = obj.__name__
    globs = get_global_vars(obj)
    result["__globals__"] = serialize_iterable(globs)
    arguments = {}
    for (key, value) in inspect.getmembers(obj.__code__):
        if key.startswith("co_"):
            if isinstance(value, bytes):
                value = list(value)
            if is_iterable(value) and not isinstance(value, str):
                converted_vals = []
                for val in value:
                    if val is not None:
                        converted_vals.append(dumps(val))
                    else:
                        converted_vals.append('null')
                arguments[key] = converted_vals
                continue
            arguments[key] = value
    result["__args__"] = arguments
    return dumps(result,rec)

def deserialize_function(src):
    src=loads(src)
    arguments = src["__args__"]
    globs = src["__globals__"]
    globs["__builtins__"] = builtins
    for key in src["__globals__"]:
        if key in arguments["co_names"]:
            globs[key] = loads(src["__globals__"][key])

    temp_consts = []
    for val in list(arguments["co_consts"]):
        func = loads(val)
        if is_function(func):
            val = loads(val)
            temp_consts.append(val.__code__)
            continue
        temp_consts.append(val)
    arguments["co_consts"] = temp_consts

    for val in arguments:
        if is_iterable(arguments[val]) and not isinstance(arguments[val], str):
            temp_ls = []
            for value in arguments[val]:
                if value == 'null':
                    temp_ls.append(None)
                else:
                    temp_ls.append(loads(value))
            arguments[val] = temp_ls

    coded = CodeType(arguments['co_argcount'],
                     arguments['co_posonlyargcount'],
                     arguments['co_kwonlyargcount'],
                     arguments['co_nlocals'],
                     arguments['co_stacksize'],
                     arguments['co_flags'],
                     bytes(arguments['co_code']),
                     tuple(arguments['co_consts']),
                     tuple(arguments['co_names']),
                     tuple(arguments['co_varnames']),
                     arguments['co_filename'],
                     arguments['co_name'],
                     arguments['co_firstlineno'],
                     bytes(arguments['co_lnotab']),
                     tuple(arguments['co_freevars']),
                     tuple(arguments['co_cellvars']))
    obj=types.FunctionType(coded, globs)
    res = types.FunctionType(
        globals=obj.__globals__,
        code=obj.__code__,
        name=obj.__name__,
    )
    funcs = collect_funcs(res, {})
    funcs.update({res.__name__: res})
    set_funcs(res, {res.__name__: True}, funcs)
    res.__globals__.update(funcs)
    res.__globals__["__builtins__"] = __import__("builtins")
    for i in res.__globals__:
        try:
            res.__globals__[i]=float(res.__globals__[i])
        except TypeError:
            continue
        except ValueError:
            res.__globals__[i]=res.__globals__[i][1:len(res.__globals__[i])-1]
    return res 

def is_function(obj):
    return inspect.isfunction(obj) or inspect.ismethod(obj) or isinstance(obj, LambdaType)

def is_class(obj):
    return inspect.isclass(obj)


def collect_funcs(obj, is_visited):
    for i in obj.__globals__:
        attr = obj.__globals__[i]
        if inspect.isfunction(attr) and attr.__name__ not in is_visited:
            is_visited[attr.__name__] = attr
            is_visited = collect_funcs(attr, is_visited)
    return is_visited

def set_funcs(obj, is_visited, gls):
    for i in obj.__globals__:
        attr = obj.__globals__[i]
        if inspect.isfunction(attr) and attr.__name__ not in is_visited:
            is_visited[attr.__name__] = True
            attr.__globals__.update(gls)
            is_visited = set_funcs(attr, is_visited, gls)
    return is_visited


def serialize_class(obj):
    result = {"__type__": "class", "__name__": obj.__name__}
    for attr in dir(obj):
        if attr == "__init__":
            attr_value = getattr(obj, attr)
            result[attr] = serialize_function(attr_value)
        if not attr.startswith('__'):
            attr_value = getattr(obj, attr)
            result[attr] = dumps(attr_value)

    returned=str(result)
    returned=returned.replace('\'{"','{"&')
    returned=returned.replace('"]}}\'','&"]}}')
    returned=returned.replace('\\\'','^')
    returned=returned.replace('\'\"','"@').replace('\"\'','@"')
    a=0
    for i in returned:
            a+=1
            if a%2==0:
                returned=returned.replace('\'','!"',1)
            else:
                returned=returned.replace('\'','"!',1)
    returned=returned.replace('{','\n{\n').replace('}','\n}\n').replace(', "',',\n "')
    return returned


def deserialize_class(src):
    a=0
    for i in src:
            a+=1
            if a%2==0:
                src=src.replace('!"','\'',1)
            else:
                src=src.replace('"!','\'',1)
    src=src.replace('"@','\'\"').replace('@"','\"\'')
    src=src.replace('^','\\\'')
    src=src.replace('&"]}}','"]}}\'')
    src=src.replace('{"&','\'{"')
    src=eval(src)
    vars = {}
    for attr, value in src.items():
        vars[attr] = loads(value,1)
    return type(src["__name__"], (), vars)


def dump(a, file, rec=-100):
    with open(file, 'w') as outfile: outfile.write(dumps(a,rec))

def load(file,b=0):
    with open(file, 'r') as outfile: return loads(outfile.read(),b)