# yuanzu may got problem when index   like
student = ("Jim",16,'male','jim666@gmail.com')
## name
print student[0]
## age
if student[1] >= 18

# 1.meiju like C/C++
NAME = 0
AGE = 1
SEX = 2
EMAIL = 3
## or
NAME,AGE,SEX,EMAIL = xrange(4)
## name
print student[NAME]
## age
if student[AGE] >= 18

# 2.use collections.namedtuple instead of tuple
from collections imort namedtuple
Student = namedtuple('Student',['name','age','sex','email'])
## creat
s = Student('Jim',16,'male','jim666@gmail.com')
## or
s = Student(name='Jim',age=16,sex='male',email='jim666@gmail.com')
## name
s.name
## age
s.age

## shifou wei neizhi tuple dezilei
isinstance(s,tuple)