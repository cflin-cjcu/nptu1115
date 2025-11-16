data = []

with open("read.txt","r") as file:
   # TODO
   for line in file:
      print(line)
      n, h, w = line.split()
      data.append([n,int(h),int(w)])

nn = [i[0]for i in data]
nh = [i[1]for i in data]
nw = [i[2]for i in data]

s=f"""Average height: {sum(nh)/len(nh):.2f}
Average weight: {sum(nw)/len(nw):.2f}
The tallest is {nn[nh.index(max(nh))]} with {max(nh):.2f}cm
The heaviest is {nn[nw.index(max(nw))]} with {max(nw):.2f}kg"""
print(s)