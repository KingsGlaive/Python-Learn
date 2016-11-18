#shiyong neizhihanshu sorted
#1.liyong zip jiangzidianshuju zhuanhuawei yuanzu
from random import randint
d = {x: randint(60,100) for x in 'xyzabc'}
#buneng zhijie sorted(d)
#yuanzu de bijiao xianbijiao dilingge yuansu

zip(d.values(),d.keys())
#or cunchukongjian gengyou
zip(d.itervalue(),d.iterkeys())
sorted(zip(d.itervalue(),d.iterkeys()))

#2.chuandi sorted hanshu de key canshu
d.item()
#yong key xuanze yonglaibijiaode zhi
sorted(d.item(),key=lambda x : x[1])