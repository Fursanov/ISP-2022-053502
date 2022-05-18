from yaml_serializer import loads,dumps,dump,load

a=[]
a.append(dict(int_list=[1, 2, 3],str_list=['a', 'b', 'c'],bool_list=[True,False]))
a.append([[1, 2, 3],['a', 'b', 'c'],dict([('1',1),('2',2)])])
a.append([[[1,2,3],['a','s','d'],[1,2,3]],[[4,5,6],['f','g','h'],[4,5,6]]])
a.append(dict(a1=dict(a11=11, a12=12),a2=dict(a21=21,a22=22)))
a.append([[1,'a',3],[4,'f',5],[6,7]])
a.append([[[1,2,3],2]])
a.append([[1,2,3],[4,5,6]])
A=a[0]

dump(A, './yaml_files/data1.yaml', 1)
print(load('./yaml_files/data1.yaml'))