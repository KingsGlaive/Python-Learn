#yi zuqiuliansai jinqiuweili

#sample quyang(suiji)
from random imort randint,sample
sample('abcdefg',3)

sample('abcdefg',randint(3,6))

#caiyong zidianjiexi
s1 = {x: randint(1,4) for x in samle('abcdefg',randint(3,6))}
s2 = {x: randint(1,4) for x in samle('abcdefg',randint(3,6))}
s3 = {x: randint(1,4) for x in samle('abcdefg',randint(3,6))}

#1.diedai(xiaolvdi)
res=[]
for k in s1:
	if k in s2 and k in s3:
		res.append(k)

#2 liyongjihe(set)dejiaojicaozuo
#use viewkeys() dedao yigezidian keys dejihe

s1.viewkeys()
s2.viewkeys()

#jiaoji
s1.viewkeys() & s2.viewkeys() & s3.viewkeys()

#duiyu N lunlaishuo
#use map() dedaosuoyouzidian keys dejihe
#use reduce() qusuoyouzidian keys dejihedejiaoji
map(dict.viewkeys,[s1,s2,s3])
reduce(lambda a,b: a & b, map(dict.viewkeys,[s1,s2,s3]))