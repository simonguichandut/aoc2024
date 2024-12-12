from utils import *

s = read()

lengths,free = s[::2], s[1::2]
data = []
for i in range(len(lengths)):
    for _ in range(int(lengths[i])):
        data.append(i)
    if i < len(free):
        for _ in range(int(free[i])):
            data.append(-1)

def checksum(data):
    chk = 0
    for i,n in enumerate(data):
        if n!=-1: chk += i*n
    return chk

# Part 1
data1 = data[:]
jlast = 0
for i in range(len(data1)-1,-1,-1):
    id = data1[i]
    if id==-1: continue

    for j in range(jlast,i): # bit faster to not look from 0
        if data1[j]!=-1: continue

        data1[j] = id
        data1[i] = -1
        jlast = j
        break

print("Part 1: ", checksum(data1))

# Part 2
data2 = data[:]
for id in range(len(lengths)-1,0,-1):
    i = data2.index(id)
    nmove = int(lengths[id])
    for j in range(0,i):
        if all(x==-1 for x in data2[j:j+nmove]):
            data2[j:j+nmove] = [id for _ in range(nmove)]
            data2[i:i+nmove] = [-1 for _ in range(nmove)]
            break

print("Part 2: ", checksum(data2))


# Way over-engineered first solve...

# class File:
#     def __init__(self, id, size, free):
#         self.id,self.free = id,free
#         self.nums = [id] * size
#         self.free_left = 0 # some weird edge case if part 2..

#     def add(self, id):
#         if self.free==0: sys.exit("tried to add to full")
#         self.nums.append(id)
#         self.free -= 1

#     def pop(self):
#         self.free += 1
#         return self.nums.pop()
    
# Files = []
# for i in range(len(s)//2):
#     size,free = map(int, s[2*i:2*i+2])
#     Files.append(File(i,size,free))
# Files.append(File(i+1,int(s[-1]),0))

# # Part 1

# def has_room(files):
#     found_free = False
#     for file in files:
#         if len(file.nums)>0 and found_free:
#             return True
#         if not file.free==0:
#             found_free = True
#     return False

# while has_room(Files):
#     forg = [file for file in Files if len(file.nums)>0][-1]
#     id = forg.pop()
#     fdest = [file for file in Files if file.free>0][0]
#     fdest.add(id)

# def checksum(files):
#     # return sum(i*n for i,n in enumerate(n for file in files for n in file.nums)) # works for part1, not part2 because free space
#     i,chk = 0,0
#     for file in files:
#         for _ in range(file.free_left):
#             i += 1
#         for n in file.nums:
#             chk += i*n
#             i += 1
#         for _ in range(file.free):
#             i += 1
#     return chk

# print("Part 1: ", checksum(Files))


# # Part 2: recreate the classes
# Files = []
# for i in range(len(s)//2):
#     size,free = map(int, s[2*i:2*i+2])
#     Files.append(File(i,size,free))
# Files.append(File(i+1,int(s[-1]),0))

# for id in range(len(Files)-1,0,-1): # move ids once in decreasing order
#     moved = False
#     for i in range(1,len(Files)):
#         forg = Files[-i]
#         nmove = forg.nums.count(id) # blocks of that id in this file
#         if nmove==0:
#             continue

#         for j in range(0,len(Files)-i): # look for somewhere to place them starting left
#             fdest = Files[j]
#             if fdest.free >= nmove:
#                 for _ in range(nmove):
#                     fdest.add(id)
#                 moved = True
            
#                 if id == max(forg.nums):
#                     forg.free += nmove
#                 else:
#                     forg.free_left += nmove

#                 forg.nums = [n for n in forg.nums if n!=id]

#                 # check on test example
#                 # ss = ''
#                 # for file in Files:
#                 #     ss += '.'*file.free_left
#                 #     ss += ''.join(str(n) for n in file.nums)
#                 #     ss += '.'*file.free
#                 # print(ss)

#                 break
#         if moved:
#             break

# print("Part 2: ", checksum(Files))