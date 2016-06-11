
with open("order_data3.csv") as f:
    for line in f:
        all_ids = line.split(",")
        all_ids.pop(0)
        all_ids.pop(3)
        all_ids.pop(3)
        x_ids = all_ids
        key = 2
        x_ids = all_ids[:key] + all_ids[(key + 1):]
        print ",".join(x_ids)
