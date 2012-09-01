# This script will read in a list of raspberian packages and strip
# out just the package names.

import time

# suedo code
# open file
# find a package name
# append package name to a list
# output file

startTime = time.time()

# Read file
# This file has 36,996 records
# First full run on commanche took 1647.78 seconds with while statement below
# after fixing premature termination problem and used for loop execution on
# commanche took 554.86 seconds
#inputFile = "/home/pi/Documents/Packaes-8-25-12" #file on the pi
inputFile = "/home/rich/Desktop/RaspberryPi/Packages-8-25-12"  #file on commanche
rawFile = open(inputFile, "r")
packageData = rawFile.read()
rawFile.close()

size = len(packageData)
entries = packageData.count("Package: ")
entriesCheck = packageData.count("Version: ")

readTime = time.time()

print
print "File read..."
print
print "File length is " + str(size) + " characters with " + str(entries) + " package entries "
print
print "As a check there are " + str(entriesCheck) + " instances of Version:"
print "Elapsed time is " + str(readTime - startTime) + " secs"
print

count = 1
packageList = []
#entries = 10  #Get first 10 for testing purposes when using for loop below
newStart = 0
for i in range(entriesCheck): #Condition did not run to end of file
#while "Package: " in packageData[newStart:]: #Runs MUCH slower
    startIndex = packageData.find("Package: ", newStart)
    endIndex = packageData.find("Version: ", newStart)

    packageName = packageData[startIndex + len("Package: "):endIndex]
    if "Source: " in packageName:
        cut = packageName.find("Source")
        packageName = packageName[:cut]
    packageName = packageName.strip("\n")
    print count, packageName
    packageList.append(packageName)
    newStart = endIndex + 1
    count += 1

endTime = time.time()
print "Total run time was " + str(endTime - startTime) + " secs"
print
print str(count) + " records processed."
    


