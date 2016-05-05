avg_wt=0
avg_tat=0
num=0
burst_t=[0,0,0,0,0]
waiting_t=[0,0,0,0,0]
turn_t=[0,0,0,0,0]
num=input("Enter total number of processes:")
i=0
print "Enter burst times for the following processes(maximum 5 processes):\n"
while i<num:
	
	print'p[' +str(i+1)+ ']:'
	burst_t[i]=input("")
	i+=1
waiting_t[0]=0  #waiting time for first process is zero
i=1
while i<num:
	waiting_t[i]=0
	j=0
	while j<i:
		waiting_t[i]+=burst_t[j]
		j+=1
	i+=1
print "Process\t\tBurst time\t\tWaiting time\t\tTurnaround time"
i=0
while i<num:
	turn_t[i]=burst_t[i]+waiting_t[i]
	avg_wt+=waiting_t[i]
	avg_tat+=turn_t[i]
	print str(i+1)+'\t\t',str(burst_t[i])+'\t\t\t\t',str(waiting_t[i])+'\t\t\t',str(turn_t[i])+'\t\t'
	i+=1
avg_wt/=num
avg_tat/=num
print 'Average waiting time:'+str(avg_wt)
print 'Average turn around time:'+str(avg_tat)

	

