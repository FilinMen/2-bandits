input_data = open("input.txt","r")
data = input_data.read()

a = int(data[0])
b = int(data[1])
d = 10

c = d - a # первый стрелок не прострелил
r = d - b #второй стрелок не прострелил

t = str(c) + str(r)
output_data = open("output.txt","w")
output_data.write(t)
output_data.close()
input_data.close()
