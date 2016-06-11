
with open("order_data3.csv") as f:
    for line in f:
        all_ids = line.split(",")
        key = 3
        if all_ids[3] == "100.0":
            print "1.0"
        else:
            print "0.0"
