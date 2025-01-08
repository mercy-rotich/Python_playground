import statistics

numbers = [72,54,66,78,90,54,56,98]

mean = sum(numbers)/len(numbers)


mode = statistics.mode(numbers)
median = statistics.median(numbers)


print(f"Mean:",mean)
print(f"mode:",mode)
print(f"median:",median)