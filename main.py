
def count_batteries_by_health(present_capacities):
  #creating a dictionary named counts to intialize different battery health categories
  counts={"healthy":0,"exchange":0,"failed":0}
  for capacity in present_capacities:
    #calculating SoHof each battery
    RA=120
    #RA (rated capacity of new battery)
    SoH=(capacity/RA)*100

    #classification of batteries based on SoH
    if 60<=SoH<=80:
      counts["exchange"]+=1
    elif SoH>80:
      counts["healthy"]+=1
    else:
      counts["failed"]+=1

   return counts
    

 


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [115, 118, 80, 95, 91, 77]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")
  #printing the results
  print("Battery Health Counts:",counts)


if __name__ == '__main__':
  test_bucketing_by_health()
