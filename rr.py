quantum_t=input("Enterthe quantum time: ")
number=input("Enter number Of Processes: ")
remain=number
turnaround=0
wait=0
time=0
flag=0
arr=[]
print arr
for i in range(number):
    arr.append([0,0,0])
    arr[i][0]=(int(input("Pleases enter arrival time for process "+ repr(i+1)+" : ")))
    arr[i][1]=(int(input("Enter Burst Time For Process "+repr(i+1)+" : ")))
    arr[i][2]=arr[i][1]
arr.sort()
for i in range(len(arr)):
    for j in range(2):
        print arr[i][j]
print "\nProcess\t|Turnaround Time|wait Time\n"
i=0
while remain!=0:
    if arr[i][2]<=quantum_t and arr[i][2]>0:
        time=time+arr[i][2]
        arr[i][2]=0
        flag=1
    else if arr[i][2]>0:
        arr[i][2]=arr[i][2]-quantum_t
        time=time+quantum_t
    if arr[i][2]==0 and flag==1:
        remain=remain-1
        print "P"+repr(i+1)+"\t|\t",time-arr[i][0]," \t|\t",time-arr[i][0]-arr[i][1],"\n"
        wait=wait+time-arr[i][0]-arr[i][1]
        turnaround=turnaround+time-arr[i][0]
        flag=0
    if(i==number-1):
        i=0
    else if arr[i+1][0]<time:
        i=i+1
    else:
        i=0
print "Average wait Time ", float(wait/(1.00*number))
print "Average Turnaround Time", float(turnaround/(1.00*number))
