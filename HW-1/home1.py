name=input("please tell us your name")
print("hello " +name+ " guess a number between 1 and 100")
count=0
low=1
high=100
mid=(low+high)//2
while True:
	reply= input("is your number " +str(mid)+ " ? (yes/no)")
	count=count+1
	if (reply=='yes'):
		print("yeah! I got it in " +str(count)+ " tries \n")
		reply=input("do you want to play more?")
		if(reply=='yes'):
			count=0
			low=1
			high=100
			mid=(low+high)//2
			continue
		else:
			print("BYE-BYE")
			break
	elif(reply=='no'):
		reply=input("is your number greater than " +str(mid))
	if(reply=='no'):
		high=mid
		mid=(low+high)//2
	elif(reply=='yes'):
		low=mid
		mid=(low+high)//2
else:
	print(" wrong choice")

