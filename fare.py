def fare():
    base_fare= 5
    distance = float(input("Enter distance travelled(km):"))
    distance_fare=0
    time_taken=float(input("Enter time taken(minutes):"))
    time_fare=0
    
    if distance < 0:
        print("Distance cannot be negative")
    elif distance <= 5:
        distance_fare = 2*distance
    elif distance > 5:
        distance_fare = 2*5 + (distance-5)*1.5

   
    if time_taken < 0:
        print("Time cannot be negative")
    elif time_taken <= 10:
        time_fare = 0.50*time_taken
    elif time_taken > 10:
     time_fare = 0.50*10 + (time_taken-10)*0.30

    print("base fare = $",base_fare)
    print("Travelling Distance =", distance,"km")
    print("Distance fare =$",distance_fare)
    print("Time taken =", time_taken,"minutes")
    print("Time fare =$",time_fare)
    print("total fare = $",base_fare+distance_fare+time_fare)

fare()