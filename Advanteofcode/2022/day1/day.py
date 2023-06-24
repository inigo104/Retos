import heapq

elfs_cal = []

with open("input.txt") as archivo: 
    elfs_cal = archivo.read().split("\n\n")

for index, elf in enumerate(elfs_cal):
    numbers = elf.split("\n")
    total = 0
    for number in numbers:
        total += int(number)
    elfs_cal[index] = total

print(max(elfs_cal))


top3_elfs_cal = sum(top for top in heapq.nlargest(3, elfs_cal))

print(top3_elfs_cal)