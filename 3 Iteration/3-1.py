#yongshifangwen celue
#list he zifuchuan shi kediedaiduixiang
l = [1,2,3,4]
s = 'abcde'
for x in l: print x
for x in s: print x
#iter() youkediedai duixiang dedao diedaiqiduixiang
iter(l)
iter(s)

l.__iter__()
s.__getiterm__()

t=iter(l)
t.next()
t.next()
t.next()
