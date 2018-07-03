def loot(arr,W):
	curWeight = 0
	finValue = 0
	for i in range(0,len(arr)):
		if curWeight +arr[i][1] <= W:
			curWeight +=arr[i][1]
			finValue += arr[i][0]
		else:
			remain = W - curWeight
			finValue += arr[i][0]*(remain/arr[i][1])
			break
	return finValue			 







n,W = map(int,input().split())
arr = []
for i in range(n):
	arr.append(list(map(int,input().split())))
arr = sorted(arr,key=lambda x:(x[1]/x[0]))
print("{0:.4f}".format(loot(arr,W))	)