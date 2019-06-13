import sys
import csv

gcode_file = sys.argv[1]
f = open(gcode_file, 'r')

stripped = []

for line in f:
    if line[0] != ";" and line != '\n':
        stripped.append(line.partition(';')[0].rstrip())

current_tool = 0
feeder = 0
speed = 0
X = 0
Y = 0
Z = 0
theta = 0
phi = 0

filename = gcode_file
while '\\' in filename:
    filename = filename.rpartition('\\')[2]

filename = filename.partition('.')[0]

with open(filename + '.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for command in stripped:
        if "T0" in command:
            current_tool = 0
        elif "T1" in command:
            current_tool = 1
        if "F" in command:
            speed = command.partition('F')[2].partition(' ')[0]
        if "X" in command:
            X = command.partition('X')[2].partition(' ')[0]
        if "Y" in command:
            Y = command.partition('Y')[2].partition(' ')[0]
        if "Z" in command:
            Z = command.partition('Z')[2].partition(' ')[0]
        if "E" in command and "E-" not in command:
            feeder = 1
        else:
            feeder = 0
        #print("{} {} {} {} {} {}".format(X,Y,Z,feeder,current_tool,speed))
        if "G1" in command or "G0" in command:
            writer.writerow([X,Y,Z,theta, phi, feeder,current_tool,speed])
#print(stripped)
#gcode = f.read()
