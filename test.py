from yaml_files import yaml_serializer
from toml_files import toml_serializer
from json_files import json_serializer

f=16
def HELLO():
    if(f==16):
        print('HELLO')
        return 'success'

class TestClass:
    def __init__(self):
        pass
    test_int = 12345
    test_float = 3.14
    test_tuple = (1, 2, 3)
    test_string = 'Test String'
    test_none = None
    test_bool = False

    def HELLO1(self):
        if(f==16):
            print('HELLO1')
            return 'success'

a=[]
a.append(dict(int_list=[1, 2, 3],str_list=['a', 'b', 'c'],bool_list=[True,False]))
a.append([[1, 2, 3],['a', 'b', 'c'],dict([('1',1),('2',2)])])
a.append([[[1,2,3],['a','s','d'],[1,2,3]],[[4,5,6],['f','g','h'],[4,5,6]]])
a.append(dict(a1=dict(a11=11, a12=12),a2=dict(a21=21,a22=22)))
a.append([[1,'a',3],[4,'f',5],[6,7]])
a.append([[[1,2,3],2]])
a.append([[1,2,3],[4,5,6]])

d=[]
d.append(dict(int_list=[1, 2, 3],str_list=['a', 'b', 'c'],dick=dict([('1',2)]),text='string',number=3.44,boolean=True,none=None))
d.append([[1, 2, 3],['a', 'b', 'c'],dict([('1',1),('2',2)]),'string',3.44,True,None])
d.append([[1, 2, 3],3.44,['a', 'b', 'c'],True,dict([('1',1),('2',2)]),'string',None])
d.append(dict(int_list=[1, 2, 3],number=3.44,str_list=['a', 'b', 'c'],boolean=True,dick=dict([('1',2)]),text='string',none=None))
d.append([[[1,2,3],['a','s','d'],[1,2,3]],[[4,5,6],['f','g','h'],[4,5,6]]])
d.append(dict(a1=dict(a11=11, a12=12),a2=dict(a21=21,a22=22)))
d.append([[[1],['a'],[2]],[[4],['f'],[5]],6])
d.append(dict(a11=[dict(a111=[111]),123], a12=12))
d.append([[[1,2,3],2]])

def test_passing00():
    b=json_serializer.loads(json_serializer.dumps(d))
    assert  b==d
def test_passing0():
    b=yaml_serializer.loads(yaml_serializer.dumps(a[0]))
    assert  b == a[0]
def test_passing1():
    b=yaml_serializer.loads(yaml_serializer.dumps(a[1]))
    assert  b == a[1]
def test_passing2():
    b=yaml_serializer.loads(yaml_serializer.dumps(a[2]))
    assert  b == a[2]
def test_passing3():
    b=yaml_serializer.loads(yaml_serializer.dumps(a[3]))
    assert  b==a[3]
def test_passing4():
    b=yaml_serializer.loads(yaml_serializer.dumps(a[4]))
    assert  b==a[4]
def test_passing5():
    b=yaml_serializer.loads(yaml_serializer.dumps(a[5]))
    assert  b==a[5]
def test_passing6():
    b=yaml_serializer.loads(yaml_serializer.dumps(a[6]))
    assert  b==a[6]
def test_passing7():
    b=json_serializer.loads(json_serializer.dumps(a[0]))
    assert  b == a[0]
def test_passing8():
    b=json_serializer.loads(json_serializer.dumps(a[1]))
    assert  b == a[1]
def test_passing9():
    b=json_serializer.loads(json_serializer.dumps(a[2]))
    assert  b == a[2]
def test_passing10():
    b=json_serializer.loads(json_serializer.dumps(a[3]))
    assert  b==a[3]
def test_passing11():
    b=json_serializer.loads(json_serializer.dumps(a[4]))
    assert  b==a[4]
def test_passing12():
    b=json_serializer.loads(json_serializer.dumps(a[5]))
    assert  b==a[5]
def test_passing13():
    b=json_serializer.loads(json_serializer.dumps(a[6]))
    assert  b==a[6]
def test_passing14():
    b=toml_serializer.loads(toml_serializer.dumps(a[0]))
    assert  b == a[0]
def test_passing15():
    b=toml_serializer.loads(toml_serializer.dumps(a[1]))
    assert  b == a[1]
def test_passing16():
    b=toml_serializer.loads(toml_serializer.dumps(a[2]))
    assert  b == a[2]
def test_passing17():
    b=toml_serializer.loads(toml_serializer.dumps(a[3]))
    assert  b==a[3]
def test_passing18():
    b=toml_serializer.loads(toml_serializer.dumps(a[4]))
    assert  b==a[4]
def test_passing19():
    b=toml_serializer.loads(toml_serializer.dumps(a[5]))
    assert  b==a[5]
def test_passing20():
    b=toml_serializer.loads(toml_serializer.dumps(a[6]))
    assert  b==a[6]
def test_passing21():
    b=json_serializer.loads(json_serializer.dumps(HELLO),1)
    assert  dir(b)==dir(HELLO)
b=json_serializer.loads(json_serializer.dumps(TestClass),1)()
c=TestClass()
def test_passing22():
    assert  b.HELLO1()==c.HELLO1()
def test_passing23():
    assert  b.test_bool==c.test_bool
def test_passing24():
    assert  b.test_float==c.test_float
def test_passing25():
    assert  b.test_int==c.test_int
def test_passing26():
    assert  b.test_none==c.test_none
def test_passing27():
    assert  b.test_string==c.test_string
def test_passing28():
    assert  tuple(b.test_tuple)==c.test_tuple
