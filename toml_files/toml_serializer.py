import sys
sys.path.append('/home/kapustka/ISP-2022/json_files')
import json_serializer

def dumps(a, str_name=''):
    string=str_name
    if string!='':
        string+=' = '

    if json_serializer.is_function(a):
        return json_serializer.serialize_function(a,1)

    if json_serializer.is_class(a):
        return json_serializer.serialize_class(a)

    if isinstance(a, str):
        if(len(a)>1):
            if(a[0]=='{' or a[1]=='{' and a[len(a)-1]=='}'):
                return ''+a+''
            if(a[0]=='"' and a[len(a)-1]=='"'):
                return '"'"'"+a[1:len(a)-1]+"'"'"'
        if(len(a)==1):
            if(a[0]=='"' and a[len(a)-1]=='"'):
                return "'"
        return string+('"'+str(a)+'"')

    if isinstance(a, bool):
        if(a==True):
            return string+'true'
        else:
            return string+'false'

    if a is None:
        return string+'null'

    if isinstance(a, dict):
        string=''
        for i in a:
            string+= dumps(a.get(i),str_name+'.'+'"'+str(i)+'"')+'\n'
        return string

    if isinstance(a, list) or isinstance(a, tuple):
        string=''
        for i in range(len(a)):
            string+=dumps(a[i],str_name+'.'+str(i))+'\n'
        return string

    return string+str(a)

def get_name(a, str_name=''):
    for i in range(len(a)-1):
        if a[i]==' ' or a[i]=='.':
            break
        else:
            str_name+=a[i]
    return str_name

def loads(a, b=0, str_name=''):
    if(a[0]!='\n'):
        for i in range(len(a)-1):
            if a[i]==' ' or a[i]=='.':
                break
            else:
                str_name+=a[i]
    
    rec=0
    if(a[0]!='\n'):
        for i in range(len(a)-1):
            if a[i]=='\n' and a[i+1] !='\n':
                rec+=1
    if(rec==0):
        a=a.replace(str_name+' = ','').replace(str_name,'')
    
    if(a=='true'):
        return True
    
    
    if(a=='false'):
        return False
    
    
    if(a=='null'):
        return None
    
    temp_a=a.replace('\n','').replace('\t','').replace('\\','')

    if(temp_a[0]=='{' and temp_a[len(temp_a)-1]=='}'):
        if(temp_a[14:22]=='function' and b==1):
            zxc=json_serializer.deserialize_function(temp_a)
        elif(temp_a[17:22]=='class' and b==1):
            zxc=json_serializer.deserialize_class(temp_a)
        return zxc
    
    if(json_serializer.is_digit(a)):
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


    p=len(str_name)+1
    j=0 
    i=0
    a+=" "
    while(i<len(a)-1):
        if a[i]=='\n' and a[i+1] !='\n':
            a=a.replace(a[j:i],a[j+p:i])
            j=i-p+1
            i-=p
        i+=1

    a=a[0:len(a)-2]

    if(a[0]=='0'):
        max_point=0
        point=0
        for i in range(len(a)):
            if(a[i]=='.'):
                point+=1
            elif(a[i]=='\n'):
                if(point>max_point):
                    max_point=point
                point=0
        a=a.replace('\n'*(max_point+1),'\n'*(max_point)+'^').split('^')
        b=[]
        for i in a:
            if(i!=''):
                b.append(loads(i))
    else:
        max_point=0
        point=0
        for i in range(len(a)):
            if(a[i]=='.'):
                point+=1
            elif(a[i]=='\n'):
                if(point>max_point):
                    max_point=point
                point=0
        a=a.replace('\n'*(max_point+1),'\n'*(max_point)+'^').split('^')
        b={}
        for i in a:
            if(i!=''):
                b[get_name(i)[1:len(get_name(i))-1]]=loads(i)
    return b

def dump(a, file, str_name=''):
    with open(file, 'w') as outfile: outfile.write(dumps(a, str_name))

def load(file,b=0):
    with open(file, 'r') as outfile: return loads(outfile.read(),b)