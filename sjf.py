avg_wt=0
avg_tat=0
num=0
bt=[0,0,0,0,0]
wt=[0,0,0,0,0]
turn_t=[0,0,0,0,0]
num=input("Enter total number of processes(maximum 5 processes):")
i=0
print "Enter burst times for the following processes:\n"
while i<num:
	print'p[' +str(i+1)+ ']:'
	bt[i]=input("")
	i+=1
i=0
while i<num:
	pos=i
	j=i+1
	while j<num:
		if(bt[j]<bt[pos]):
			pos=j
		j+=1
	temp=bt[i]
        bt[i]=bt[pos]
        bt[pos]=temp
	i+=1
wt[0]=0
i=1
while i<num:
	wt[i]=0
	j=0
	while j<i:
		wt[i]+=bt[j]
		j+=1
	i+=1
print "Process\t\tBurst time\t\tWaiting time\t\tTurnaround time"
i=0
while i<num:
	turn_t[i]=bt[i]+wt[i]
	avg_wt+=wt[i]
	avg_tat+=turn_t[i]
	print str(i+1)+'\t\t',str(bt[i])+'\t\t\t\t',str(wt[i])+'\t\t\t',str(turn_t[i])+'\t\t'
	i+=1
avg_wt/=num
avg_tat/=num
print 'Average waiting time:'+str(avg_wt)
print 'Average turn around time:'+str(avg_tat)
		
