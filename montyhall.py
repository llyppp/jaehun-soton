import random as rd

def select_car(doors):
	n = rd.randint(0,2)
	doors[n] = 1
	return doors
def show_host_act(doors,contestant):
	
	for i,x in enumerate(doors):

		if i != contestant and x == 0:
			return i
def final_selection(doors,contestant,strategy=0):
	if strategy == 0:

		for i,x in enumerate(doors):
			if i == contestant and x == 1:
				return True
			else:
				return False

	if strategy == 1:
		for i,x in enumerate(doors):
			if i == contestant and x == 1:
				return False
			else:
				return True
		
#goat = 0, car = 1
#initiate the doors

doors = [0, 0, 0]
contestant = 0
show_host = 0

won_count = list()
won_count2 = list()

for i in range(0,10000):
	n = rd.randint(0,2)
	doors = select_car(doors)
	contestant = 0
	show_host = show_host_act(doors,contestant)

	#print 'doors: ', doors
	#print 'contestant: ', contestant
	#print 'show_host: ', show_host
	print "[%d] processing"%i
	won_count.append(final_selection(doors,contestant,strategy=0))
	won_count2.append(final_selection(doors,contestant,strategy=1))
	#initialize
	doors = [0,0,0]

print '--------------------------------'
print 'not changed: '
print 'probability of winning the price: ', won_count.count(True)/float(len(won_count))
print 'changed: '
print 'probability of winning the price: ', won_count2.count(True)/float(len(won_count2))
