from random import randint

data = [randint(0,20) for _ in xrange(30)]
#data zhong biranyouxiangtongyuansu]

#1.chuangjianzidian
c = dict.fromkeys(data,0)
for x in data:
	c[x] += 1

#tongjijieguo baocunzai c zhong

#2.shiyong collection.Counter duixiang
from collections import Counter
c2 = Counter(data)
#zhaodao chuxian pinduzuigaode 3geyuansu
c2.most_common(3)



#duiwenzhang de cipintongji
import re
txt = open('wenjian.txt').read()
#zhengze fenge
c3 = Counter(re.split('\W+',txt))
c3.most_common(10)