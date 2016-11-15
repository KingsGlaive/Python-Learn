#shaixuan
#1.tongyongzuofa ---diedai
data = [1,5,-3,-2,6,0,9]

res = []
for x in data:
	if x>=0:
		res.append(x)

print res

#gaojie 
#List 
#1.filter
from random import randint
data = [randint(-10,10) for _ in xrange(10)]

filter(lambda x: x >= 0,data)

#22.liebiaojiexi
[x for x in data if x >= 0] #gengkuai better

#Dictionary
d = {x: randint(60,100) for x in range(1,21)}
#zidianjiexi
{k : v for k,v in d.iteritems() if v > 90}

#jihe
s = set(data)
#jihejiexi(yu zidianjiexi xiangbi shaole maohao)
{x for x in s if x % 3 == 0}