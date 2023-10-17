import datetime 
import random
arrival_time_list=[] 
s=int(input("enter the no. of slots")) 


charging_rate=40 
final_SoC=0.8

for i in range (0,999): 
    x=int(input("enter the vehiles in charging queue")) 
    if x>=0 and x<=s: 
        print() 
        break 
    else: 
        print("invalid input")

#arrival_time_list={} 

y=int(input("enter the vehiles in virtual queue"))



SoC_charging_queue={}
SoC_virtual_queue={}
batterycap_charging_queue={}
batterycap_virtual_queue={}
charging_time_charging_queue={}
charging_time_virtualqueue={}
chargingendtime_charging_queue={}
chargingendtime_virtual_queue={}
arrival_time1=[]
arrival_time_list1=[]
arrival_time11=[]


for i in range(0,x):
    

  for j in range(0,999):
    ii = input(" time in format HH:MM for charging queue")
    hour, minute = ii.split(":")
    hour1=int(hour)
    minute1=int(minute)
    if hour1<23 and hour1>0 and minute1>=0 and minute1<59:
        print()
        arrival_time_list1.append(ii)
        break
    else:
        print("invalid")
        

   
print(arrival_time_list1)
for i in range(0,x):
    timeslot_selected1=arrival_time_list1[i]
    time_str1=len(timeslot_selected1)
    time_str_last22=timeslot_selected1[time_str1 -2:]
    time_first22=timeslot_selected1[:2]
    int_hr1=int(time_first22)
    int_min1=int(time_str_last22)
    time1=int_hr1+int_min1/60
    arrival_time11.append(time1)
    
print(arrival_time11)


for i in range(0,y):
    

  for j in range(0,999):
    i = input(" time in format HH:MM for virtual queue")
    hour, minute = i.split(":")
    hour=int(hour)
    minute=int(minute)
    if hour<23 and hour>0 and minute>=0 and minute<59:
        print()
        arrival_time_list.append(i)
        break
    else:
        print("invalid")
        

   
print(arrival_time_list)
for i in range(0,y):
    timeslot_selected=arrival_time_list[i]
    time_str=len(timeslot_selected)
    time_str_last2=timeslot_selected[time_str -2:]
    time_first2=timeslot_selected[:2]
    int_hr=int(time_first2)
    int_min=int(time_str_last2)
    time=int_hr+int_min/60
    arrival_time1.append(time)
    
print(arrival_time1)

total_ev_queue= x+y 
print(total_ev_queue)

if total_ev_queue<s: 
    print("waiting time(tw)=0") 
    print(end="") 
else: 
    print("Generate time set T of the EV’s charging end time in charging queue") 
    print(end="")



#w=float(input("enter the initial SoC")) 
#c=int(input("enter the Battery capacity"))




for i in range(0,x):
    SoC_charging_queue[i]=random.randint(20,50)
    batterycap_charging_queue[i]=random.randint(50,70)
    charging_time_charging_queue[i]=((80-SoC_charging_queue[i])*batterycap_charging_queue[i])/(charging_rate*100) 
    chargingendtime_charging_queue[i]=arrival_time11[i]+charging_time_charging_queue[i]
    
    chargingendtime_charging_queue1=list(chargingendtime_charging_queue.values())
    chargingendtime_charging_queue1.sort()
    print(chargingendtime_charging_queue1)
    
for j in range(0,y):
    SoC_virtual_queue[j]=random.randint(20,50)
    batterycap_virtual_queue[j]=random.randint(50,70)
    charging_time_virtualqueue[j]=((80-SoC_virtual_queue[j])*batterycap_virtual_queue[j])/(charging_rate*100) 
    chargingendtime_virtual_queue[j]=arrival_time1[j]+charging_time_virtualqueue[j]

print("charging queue", chargingendtime_charging_queue1)
print("virtual queue", chargingendtime_virtual_queue)
#print(arrival_time1[i])

for i in range (0,y):
    twait=chargingendtime_charging_queue1[i]-arrival_time1[i]
    if twait < 0 :
        print('twait=0')
    else:
        print(twait)
    #print(twait)