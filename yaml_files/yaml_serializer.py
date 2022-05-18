import sys
sys.path.append('/home/kapustka/ISP-2022/json_files')
from json_serializer import deserialize_class, deserialize_function, is_class, is_digit, is_function, isdict, islist, serialize_class, serialize_function


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
                return '"'"'"+a[1:len(a)-1]+"'"'"'
        if(len(a)==1):
            if(a[0]=='"' and a[len(a)-1]=='"'):
                return "'"
        return ('"'+str(a)+'"')

    if isinstance(a, bool):
        if(a==True):
            return 'true'
        else:
            return 'false'
    if a is None:
        return 'null'

    if isinstance(a, dict):
        string+=Next*'\n'+'{'+Next*'\n'
        for i in a:
            last=i
        for i in a:
            string+= '"'+str(i)+'": '
            string+= dumps(a.get(i),rec+1)
            if i != last:
                string+= ', '+Next*'\n'
        string+=Next*'\n'+'}'
        return string

    if isinstance(a, list) or isinstance(a, tuple):
        string+=Next*'\n'+'['+Next*'\n'
        for i in range(len(a)):
            last=i
        for i in range(len(a)):
            string+=dumps(a[i],rec+1)
            if i != last:
                string+= ', '+Next*'\n'
        string+=Next*'\n'+']'
        return string
    return str(a)

def loads(a, b=0):
    if isinstance(a, str):  
        a=a.replace('\n','').replace('\\','')
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


def dump(a, file, rec=-100):
    with open(file, 'w') as outfile: outfile.write(dumps(a,rec))

def load(file,b=0):
    with open(file, 'r') as outfile: return loads(outfile.read(),b)