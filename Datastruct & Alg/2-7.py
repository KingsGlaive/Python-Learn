#zhizuo yigejiandan de caishuzide youxi
from random import randint

N = randint(0,100)

def guess(k):
	if k==N:
		print 'right'
		return True
	if k<N:
		print '%s is less than N' % k
	else:
		print '%s is greater than N' % k
	return False

while True:
	line = raw_input('please input a number: ')
	if line.isdigit():
		k = int(line)
		if guess(k):
			break

#yaoqiu xianshi zuijinde 5 tiao caicejilu
#1.shiyong rongliangwei n de duilie cunchulishijilu
#shiyong collections.deque de shuangduankouxunhuanduilie
from collections import deque
q = deque([],5)#chushizhi ; rongliang
q.append(1)
#chengxutuichuqian shiyong pickle jiangduilieduixiang cunruwenjian(file) zaici yunxingchengxushi jiangqidaoru
import pickle
pickle.dump(q,open('history','w'))#python duixiang ;  wenjian duixiang
q2 = pickle.load(open('history')) 

from random import randint
from collections import deque

N = randint(0,100)
history = deque([],5)

def guess(k):
	if k==N:
		print 'right'
		return True
	if k<N:
		print '%s is less than N' % k
	else:
		print '%s is greater than N' % k
	return False

while True:
	line = raw_input('please input a number: ')
	if line.isdigit():
		k = int(line)

		history.append(k)

		if guess(k):
			break

	elif line == 'history' or line == 'h?'
		print list(history)
