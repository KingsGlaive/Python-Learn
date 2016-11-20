#xingming : (paiming : suoyongshijian)
#ex.
{'L':{2,43},'H':{5,52},'Jim':{1,39}...}

#or
d={}
d['Jim'] = (1,35)
d['Leo'] = (2,37)
d['Bob'] = (3,40)

for k in d: print k
#faxian bushi xiangjinruzidianshi youxu

#use collections.OrderedDict daiti neizhi zidian
from collections import OrderedDict
d = OrderedDict()
d['Jim'] = (1,35)
d['Leo'] = (2,37)
d['Bob'] = (3,40)

for k in d: print k
#biande youxu

#moni shili
from time import time
from random import randint
from collections import OrderedDict

#youxu zidian jilu
d = OrderedDict()

players = list('ABCHEFG')
start = time()

for i in xrange(8):
	raw_input() #qidao zuse de zuoyong
	p = players.pop(randint(0,7 - i))#meici chuqu yigeren
	end = time()
	print i + 1,p,end - start
	d[p] = (i+1,end - start)

print 
print '-'*20

for k in d:
	print k, d[k]

