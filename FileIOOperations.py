import datetime

writefile = open('TextFile', 'a')
writefile.write("Hello succer")
writefile.write(str(datetime.datetime.day))
writefile.close()

readFromMyFile = open('TextFile', 'r')

for data in readFromMyFile:
    print(data)