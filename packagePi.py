# This script will read in a list of raspberian packages and strip
# out just the package names.

# suedo code
# open file
# find a package name
# append package name to a list
# output file

# read ile
inputFile = "/home/pi/Documents/Packaes-8-25-12"
rawFile = open(inputFile, "r")
packageData = rawFile.read()
rawFile.close()


startPosition = packageData.find("Package: ")
endPosition = packageData.find("Source: ")

print start
