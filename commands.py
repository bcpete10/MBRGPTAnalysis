import argparse
import hashlib

fmname = " "
itype = " "





def commandParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', dest='type') #set up args
    parser.add_argument('-f', dest='type')
    args = parser.parse_args()
    args.func(args) #allows for parsing




def sumGetter():
    testFile = input("Please enter a file: ") #remove
    with open(testFile, 'rb') as checkFile:
        data = checkFile.read()
        md5 = hashlib.md5(data).hexdigest()

        sha256 = hashlib.sha256(data).hexdigest()
        md5file = open()
        
        
        
        print(md5) #remove, send to file
        print(sha256)




def main():
    sumGetter()


main()