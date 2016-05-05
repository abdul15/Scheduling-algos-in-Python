avg_wt=0
avg_tat=0
num=0
bt=[0,0,0,0,0]
wt=[0,0,0,0,0]
turn_t=[0,0,0,0,0]
at=[0,0,0,0,0]
rt=[0,0,0,0,0]
sum_wait=0
sum_turnaround=0
num=input("Enter total number of processes(maximum 5 processes):")
i=0
print "Enter burst times for the following processes:\n"
while i<num:
	print'p[' +str(i+1)+ ']:'
	bt[i]=input("")
	i+=1
i=0
print "Enter arrival times for the following processes:\n"
while i<num:
	print'p[' +str(i+1)+ ']:'
	rt[i]=input("")
	i+=1
print"\n\nProcess || Turnaround time || Waiting time\n\n"
time=0
remain=0
rt[4]=9999
while remain!=num:
	smallest=4
	i=0
	while i<num:
		if(at[i]<=time and rt[i]<rt[smallest] and rt[i]>0):
                	smallest=i	
		i+=1
	rt[smallest]-=1
	if(rt[smallest]==0):
            remain+=1
            endTime=time+1
            print'\nP['+str(smallest+1)+']\t\t'+str(endTime-at[smallest])+'\t  |  '+str(endTime-bt[smallest]-at[smallest])
           # sum_wait+=endTime-bt[smallest] - at[smallest]
           # sum_turnaround+=endTime-at[smallest]
	time+=1





time+=1
