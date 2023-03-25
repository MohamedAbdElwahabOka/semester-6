# Mohamed Abdelwahab
# 20108761
print("Customer \t Inter-arrival time \t Service time \t Arrival time \t Service starts at \t Service ends at \t Waiting time \t Queue length")
import random
Customer =[]
Inter_arrival_time =[]
Service_time =[]
Arrival_time =[]
Service_starts_at =[]
Service_ends_at =[]
Waiting_time =[]
Queue_length =[]
for i in range(9):
    Customer = i+1
    Inter_arrival_time.append(random.randint(1, 7))
    Service_time.append(random.randint(4, 8))
    if i == 0:
        Arrival_time.append(Inter_arrival_time[i])
        Service_starts_at.append(Arrival_time[i])
        Service_ends_at.append(Service_starts_at[i] + Service_time[i])
        Waiting_time.append(0)
        Queue_length.append(0)
    else:
        Arrival_time.append(Inter_arrival_time[i] + Arrival_time[i-1])
        Service_starts_at.append(max(Arrival_time[i], Service_ends_at[i-1]))
        Service_ends_at.append(Service_starts_at[i] + Service_time[i])
        Waiting_time.append(Service_starts_at[i] - Arrival_time[i])
        Queue_length.append(Service_starts_at[i] - Arrival_time[i])
        print(f"{i+1} \t\t {Inter_arrival_time[i]} \t\t\t {Service_starts_at[i]} \t\t\t\t\t {Arrival_time[i]} \t\t\t {Service_time[i]} \t\t\t {Service_ends_at[i]} \t\t    \t{Waiting_time[i]} \t\t\t {Queue_length}\t\t")




    


        







   

    






