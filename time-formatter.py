import sys

def formatter(file):
	for line in open(file, 'r'):
		minute = "00"
		hour = "00"

		if 'h' in line:
			parts = line.split('h')
			hour = parts[0]

			if 'm' in line:
				minute = parts[1].split('m')[0]

		else:
			minute = line.split('m')[0]

		if len(hour) == 1: 		hour 	= "0" + hour 
		if len(minute) == 1: 	minute 	= "0" + minute 

		print("{}:{}:00".format(hour, minute))


if (len(sys.argv) < 2):
	print("Enter input file")
else:
	formatter(sys.argv[1])
