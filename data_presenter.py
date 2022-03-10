# 1
# 2

open_file = open("CupcakeInvoices.csv")

# 3

# for line in open_file:
#     print(line)

# 4

# for line in open_file:
#     value = line.split(',')
#     print(value[2])

# 5
# for line in open_file:
    # values = line.split(',')
    # total = int(values[3]) * float(values[4])
    # print(total)

# 6
total = 0

for line in open_file:
    values = line.split(',')
    total = total + (int(values[3]) * float(values[4]))

print(total)

# 7
open_file.close()
