rooms=[]

def allot():
	for i in range(len(rooms)):
		if rooms[i] == 0:
			rooms[i] == 1
			return i
	rooms.append(1)
	return len(rooms)

def clear(i):
	rooms[i]=0


def runmStart(arr):
	min=arr[0][0]
	max=arr[0][1]
	mStart = {}
	mEnd = {}
	for x in arr:
		if x[0] < min:
			min = x[0]
		elif x[1] > max:
			max = x[1]
		if x[1] in mEnd:
			mEnd[x[1]].append(x[1])
		else:
			mEnd[x[1]] = [x[1]]
		if x[0] in mStart:
			mStart[x[0]].append(x[0])
		else:
			mStart[x[0]] = [x[0]]
	print(mStart, mEnd)
	for i in range(min, max+1):
		if i in mStart:
			print (mStart[i])
			for x in mStart[i]:
				ans = allot()
				print('Alloted', ans, rooms)
				pass #print (i, x)

def test(exp, arr):
	print(arr)
	ans = runmStart(arr)
	print(ans, ans == exp)

test(1, [[10, 15], [20, 25], [30, 35]])