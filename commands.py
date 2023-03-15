import argparse
import hashlib



#VARIABLE DELCARATION NEEDED FOR MBR GPT ANALYSIS
#HARDCODED DIDNT KNOW WHAT ELSE TO DO

gptTS = [0x200, 0x280, 0x300, 0x380]
gptTE = [0x20F, 0x28F,0x30F, 0x38F]
gptLS = [0x220, 0x2A0, 0x320,0x3A0]
gptLE = [0x228, 0x2A8, 0x328, 0x3A8]
gptEndRange = [0x227, 0x2A7, 0x327, 0x3A7, 0x22F,0x2AF,0x32F, 0x3AF]

mbrBeg = [0x1BE, 0x1CE,0x1DE,0x1EE]
mbrSizeRange = [0x1CA,0x1DA,0x1EA,0x1FA,0x1CE,0x1DE,0x1EE,0x1FE]
mbrLR = [0x1C6, 0x1D6, 0x1E6, 0x1F6, 0x1CA, 0x1DA, 0x1EA, 0x1FA ]
mbr16 = [0x1BE, 0x1CE, 0x1DE, 0x1EE ]
mbr16E = [0x1CE, 0x1DE, 0x1EE, 0x1FE ]
mrbeastVar = [0x1C2, 0x1D2, 0x1E2, 0x1F2]



def commandParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', dest='type') #set up args
    parser.add_argument('-f', dest='type')
    args = parser.parse_args()
    args.func(args) #allows for parsing

#CHECK TYPE OF FILE JSON OR CSV
#need pandas

def sumGetter(userIn):
    #testFile = input("Please enter a file: ") #remove
    #with open(testFile, 'rb') as checkFile:
    #    data = checkFile.read()
    #    md5 = hashlib.md5(data).hexdigest()

     #   sha256 = hashlib.sha256(data).hexdigest()
     #   md5file = open()
    
    md5sum = hashlib.md5(open(f"{userIn.file}", 'rb').read()).hexdigest()
    with open(f'md5-{userIn.file}.txt', 'w') as aut:
        aut.write(md5sum)
    sha256sum = md5sum = hashlib.sha256(open(f"{userIn.file}", 'rb').read()).hexdigest()
    with open(f'sha-256-{userIn.file}.txt', 'w') as aut:
        aut.write(sha256sum)

    #done before ANY operations on the files
    #put all in one class

    if userIn.type == mbr: #LOGIC FOR FILES IS DONE HERE
        mbr = bytearray()
        mbrAcc = open(userIn.file, 'rb')
        mbr = mbrAcc.read(512)
        print() #needed to maintain readability
        for i in range (len(mbrBeg)):
            currLoc = mbr[mbrBeg[i]]
            temp = str(hex(mbr[mrbeastVar[i]])[2:])





#cont with conda
def fileParse(feastible):
    #beastType = pd.read_csv('PartitionTypes.csv')
    feastible = str(feastible)
    




def main():
    commandParser()
    sumGetter()


main()
