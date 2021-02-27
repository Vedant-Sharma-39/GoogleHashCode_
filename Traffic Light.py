
for i in ['a','b','c','d','e','f']:
    file_name = f"{i}.txt"
    output = f"{i}_sub.txt"
fileh = open(file_name,'r')
# Streets : line 2 -  1+line 1[2]
# Paths : 1 + line 1[2] + 1 : 1 + line 1[2] + 2

for index,lines in enumerate(fileh):
    if index == 0:
        header = lines.split()

print(header)

list = []
end_list = []
dict = {}

fileh = open(file_name,'r')
for index,lines in  enumerate(fileh):

    if (index >= 1 ) and (index <= int(header[2]) ):
        start = lines.strip().split()[-1]
        end = lines.strip().split()[0]
        if end not in list:
            list.append(end)
            end_list.append(end)

        if start not in list:
            list.append(start)

fileh = open(file_name,'r')
for index,lines in  enumerate(fileh):

    if (index >= 1 ) and (index <= int(header[2]) ):
        end = lines.strip().split()[1]
        road = lines.strip().split()[-2]

        if end in dict.keys():
            dict[end].append(road)
        else:
            dict[end] = [road]





for nodes,roads in dict.items():
     for i,road in enumerate(roads):
        #k = road
        #count = 0
        #fileh = open(file_name, 'r')
        #for index, lines in enumerate(fileh):
            #if index >= int(header[2]) + 1 and index <= int(header[2]) + int(header[3]):
                #lines = lines.strip().split()
                #if road in lines:
                   # count = count + 1

        dict[nodes][i] = {road:1}


file = open(output,'w')
file.write(f"{len(dict)} \n")

for nodes,roads in dict.items():
    list = []
    for road in roads:
        for road,value in road.items():
            print(value)

  #  list = [list[[i]]*3//max(list) for i in list]
   # for i,road in enumerate(roads):
    #    for key in road.keys():
        #    road[key] = list[i]



for nodes,roads in dict.items():

    file.write(f"{nodes}\n")
    file.write(f"{len(roads)} \n")
    for road in roads:
        for keys,values in road.items():
            file.write(f"{keys} {1} \n")

