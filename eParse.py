import argparse
import hashlib
import pandas as pds
import struct





#functional as of 3/9
class inFunc:
    def commandParser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-t', dest='type') #set up args
        parser.add_argument('-f', dest='file')
        parser.set_defaults(func=sumGetter)
        input = parser.parse_args()
        input.func(input) #allows for parsing
        #print("Command Parser Check")




def sumGetter(userIn):
    #testFile = input("Please enter a file: ") #remove
    #with open(testFile, 'rb') as checkFile:
    #    data = checkFile.read()
    #    md5 = hashlib.md5(data).hexdigest()

     #   sha256 = hashlib.sha256(data).hexdigest()
     #   md5file = open()
    
    md5sum = hashlib.md5(open(f"{userIn.file}", 'rb').read()).hexdigest()
    with open(f'MD5-{userIn.file}.txt', 'w') as aut:
        aut.write(md5sum)
    sha256sum = hashlib.sha256(open(f"{userIn.file}", 'rb').read()).hexdigest()
    with open(f'SHA-256-{userIn.file}.txt', 'w') as aut:
        aut.write(sha256sum)
    #print("Sum Getter Check")
    calcs(userIn)
    

    #done before ANY operations on the files
    #put all in one class?
def typeChecker(userF):
    temp = pds.read_csv('PartitionTypes.csv')
    userF = str(userF)
    temp2 = userF.split('0x')
    #temp2 = (str(userF).split('0x'))
    returnType = temp.loc[temp['A'] == temp2[1]]['B']
    returnType = str(returnType).split()
    return returnType[1]


def calcs(userIn):
    #print("Calcs Check")
#VARIABLE DELCARATION NEEDED FOR MBR GPT ANALYSIS
#HARDCODED DIDNT KNOW WHAT ELSE TO DO
    gptTE = [0x20F, 0x28F,0x30F, 0x38F]


    mbrBeg = [0x1BE, 0x1CE,0x1DE,0x1EE]
    mbrT = [0x1C2, 0x1D2, 0x1E2, 0x1F2]
    mbrSizeRange1 = [0x1CA,0x1DA,0x1EA,0x1FA]
    mbrSizeRange2 = [0x1CE,0x1DE,0x1EE,0x1FE]
    lbaRange1 = [0x1C6, 0x1D6, 0x1E6, 0x1F6]
    lbaRange2 = [0x1CA, 0x1DA, 0x1EA, 0x1FA]
    

    if userIn.type == 'gpt': #LOGIC FOR FILES IS DONE HERE
        
        #NOT USEABLE
        
        print()

        for i in range(len(gptTE)):
            print("Non functional")
    
    elif userIn.type == 'mbr':
        #print("Accessing MBR")
        mbr = bytearray
        mbrAcc = open(userIn.file, 'rb')
        mbr = mbrAcc.read(512)
        print()
        eval = open(userIn.file, 'rb')
        for i in range(len(mbrBeg)):
            temp = mbr[mbrBeg[i]]
            temp2 = str(hex(mbr[mbrT[i]])[2:])
            checked = typeChecker(str(hex(mbr[mbrT[i]])))
            size = struct.unpack('<I', mbr[mbrSizeRange1[i]:mbrSizeRange2[i]])
            temp3 = struct.unpack('<I', mbr[lbaRange1[i]:lbaRange2[i]])
            if len(temp2) <2:
                temp2 = f"{0x0}{int(temp2,16)}"
            else:
                temp2 = temp2
            print( "(" +  str(temp2) + ")" + " " + str(checked) + " " + str(temp3[0]) + " " + str((size[0] * 512)))
            



        for i in range(len(mbrBeg)):
            temp = int(mbrBeg[i])
            finder = mbr[temp:temp+16]
            finder2 = int.from_bytes(finder[8:12], byteorder="little")
            eval.seek(finder2)
            totalParts = i + 1
            br = eval.read(512)

            print("Partition Number: " + str(totalParts))
            print("Last 16 bytes of boot record: " + str(br.hex(' '))[-47:])



        
        
#def main():
#    commandParser()
    

def main():
    parser = inFunc()
    parser.commandParser()



main()