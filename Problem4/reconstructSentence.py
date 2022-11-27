# Filename: reconstructSentence.py
#
# This program takes two arguments that are filenames
#
# This program reads the contents of the two files, concatenates them, and then orders them into a 
# readable sentence
#   
#   Example Invocation: debian@beaglebone:~$ python3 reconstructSentence.py filename1.txt filename2.txt
#
# Written by Mike Stepanik, Nov. 26th, 2022


import sys

def readFile(filepath):
    with open(filepath, 'r') as f:
        f_contents = f.read().split()
        f.close()
    return len(f_contents), f_contents

def writeFile(filepath, cotents):
    with open(filepath, 'w') as f:
        f.write(cotents)
        f.close()


def main():

    if len(sys.argv) !=3:
        sys.exit(3)

    INPUT1_FILEPATH = sys.argv[1]
    INPUT2_FILEPATH = sys.argv[2]
    OUTPUT_FILEPATH = 'output.txt'\

    print('')
    print ("Reading {} & {}....".format(INPUT1_FILEPATH, INPUT2_FILEPATH))


    #Read the file and get the file length
    file1_length, f1_contents = readFile(INPUT1_FILEPATH)
    file2_length, f2_contents = readFile(INPUT2_FILEPATH)

    print('')
    print ("List 1 (from file 1) is: ")
    print (f1_contents)
    print('')
    print ("The length of list 1 is: {}".format(file1_length))
        

    print('')
    print ("List 2 (from file 2) is: ")
    print (f2_contents)
    print('')
    print ("The length of list 2 is: {}".format(file2_length))
    
    #Find the greatest file length 
    file_length=file1_length
    if file2_length > file1_length:
        file_length = file2_length

    #Reconstruct the full sentence 
    out=[]
    while file_length > 0:
        if f1_contents:
            out.append('{} '.format(f1_contents.pop()))
        if f2_contents:
            out.append('{} '.format(f2_contents.pop()))
        file_length -= 1

    #array to string and write to file
    sentence = ''.join(out)

    print('')
    print("Reconstructed Sentence: ")
    print (sentence)

    writeFile(OUTPUT_FILEPATH, sentence)

    print ('')
    print ("Successfully written to {}!".format(OUTPUT_FILEPATH))
    print('')

if __name__ == '__main__':
        main()


    

