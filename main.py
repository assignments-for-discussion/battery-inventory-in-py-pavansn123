def count_batteries_by_health(present_capacities):
    # Initialize a dictionary named counts to initialize different battery health categories
    counts = {"healthy": 0, "exchange": 0, "failed": 0}
    
    for capacity in present_capacities:
        # Calculating SoH of each battery
        rated_capacity = 120  # Rated capacity of a new battery
        SoH = (capacity / rated_capacity) * 100

        # Classification of batteries based on SoH
        if 65 <= SoH <= 80:
            counts["exchange"] += 1
        elif SoH > 80:
            counts["healthy"] += 1
        else:
            counts["failed"] += 1

    return counts

def test_bucketing_by_health():
    print("Counting batteries by SoH...\n")
    present_capacities = [115, 118, 80, 95, 91, 77]
    counts = count_batteries_by_health(present_capacities)
    
    assert counts["healthy"] == 2
    assert counts["exchange"] == 3
    assert counts["failed"] == 1
    
    print("Done counting :)")
    # Printing the results
    print("Battery Health Counts:", counts)

if __name__ == '__main__':
    test_bucketing_by_health()

