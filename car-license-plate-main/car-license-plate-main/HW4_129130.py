# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 09:29:46 2020

@author: Arwa
@section: 20
@id: 129130

Program design:
1. purpose:
    Program that reads input from text file and finds if the alphanumeric 
    sequence in each line of the provided input file is valid for Omani car 
    license plate.
2. Input and output:   
    Input:
         text file contain alphanumeric sequence for Omani car license plate
    Output:
        txt file contain the valid sequences
        txt file contain the invalid sequences
3. Algorithm: 
    Set list for valid letter
    
    Read the input file name from the user
    Opent input file in reading mode
      In case of inexisting file : exit the program
      
    Open output files in writing mode 
      In case of no permission to write in the file : exit the program
      
    Set line number to 1
    
    for each line in input file
    
        Delete new line character
        
        if length of licensePlate == 2
            Split licensePlate into two parts
        
            Set numericSequence to the first part of licensePlate
            Set alphaSequence to the second part of licensePlate
            
            if licensePlate contain  two parts and first part is digit
            and length of the first part less than 5 and greater than 1 and
            the first number is not 0 and the second part is one of the
            letter which is in letter list
            
                Write the line in valid file
            else
                write the line in invalid file
            
        In case of licensePlate contain more than two parts or less than two:
            display a message on the screen 
            add them to invalid file
          
       

        Increase line number by 1
                
    close input file
    close output valid file
    close output invalid file

4. Test case    
=============================================================================== 
input                              exception         result           comment
===============================================================================
file: plates.txt 
3 A                                valid              valid            correct
57893245 AB                        invalid            invalid          correct
3456 ee                            invalid            invalid          correct
22        B                        valid              valid            correct
010 SS                             invalid            invalid          correct
#@5)  123                          invalid            invalid          correct
12654 YR                           valid              valid            correct
===============================================================================
file:rrr                           File Read Error
===============================================================================
file: plates.txt 
output: valid in read only mode    File Write Error (valid)      
===============================================================================
file: plates.txt 
output: valid in read only mode    File Write Error (valid)  
output: invalid in read only mode  File Write Error (invalid)  
===============================================================================
"""

#list contain valid letter combinations
letter = ['A','AA','AB','AD','AR','AM','AW','AY','B','BA','BB','BD','BR','BM',
'BW','BY','D','DA','DD','DR','DW','DY','R','RA','RR','RM','RW','RY','S','SS',
'M','MA','MB','MM','MW','MY','W','WA','WB','WW','Y','YA','YB','YD','YR','YW',
'YY']

#flag to check if we can write in output files
correct = True

try:
    # read input file name from the user
    fileName = input("Enter the input file name: ")
    #open input file
    inFile = open(fileName,"r")
    try:
        #open writing files (valid)
        outFile_valid = open("valid.txt","w")
    # exception for writing file error (valid) - no permission to write
    except IOError as exception:
        # handling exception
        print("File Write Error:",str(exception)) 
        correct = False
    try:
        #open writing files (invalid)
        outFile_invalid = open("invalid.txt","w")
    # exception for writing file error (invalid) - no permission to write
    except IOError as exception:
        # handling exception
        print("File Write Error:",str(exception)) 
        correct = False
    # we can write in all output files      
    if correct:

        #process input file
        
        #count lines to use them in exception
        lineNumber = 0
        #visit each line in the file
        for line in inFile:

            #increase line number by 1   
            lineNumber = lineNumber + 1
            #delete new line character
            line = line.rstrip("\n")
            
            try:

                #split the line into licensePlate 
                licensePlate = line.split()
                if len(licensePlate) == 2:
                    # set numericSequence to the first vailue in licensePlate
                    numericSequence = licensePlate[0]
                    # set numericSequence to the second vailue in licensePlate
                    alphaSequence = licensePlate[1]
                    
                    # check if licensePlate follow the required format
                    if numericSequence.isdigit() and \
                    len(numericSequence) <= 5 and len(numericSequence) >= 1 \
                    and numericSequence[0]!="0" and alphaSequence in letter:
                        # followed required format
                        outFile_valid.write(line + "\n")       
                    else:
                        # not followed required format
                        outFile_invalid.write(line + "\n")
                        
                elif len(licensePlate)>2:
                   raise RuntimeError
                elif len(licensePlate)==1:
                   raise RuntimeError   
               
            # exception for licensePlates which has less or more than 2 parts
            except RuntimeError: 
                # missing data
                if len(licensePlate) == 1:
                    # handling exception
                    print("Parse Error @ line number %d:" % lineNumber\
                          ,"need more than 1 value to unpack:",str(line))
                    outFile_invalid.write(line + "\n")
                # more data    
                elif len(licensePlate) > 2 :
                    # handling exception
                    print("Parse Error @ line number %d:" % (lineNumber) \
                          ,"too many parameters:",str(line))
                    outFile_invalid.write(line + "\n")
           
    
        # close input and output files
        outFile_invalid.close()
        outFile_valid.close() 
        inFile.close()
    
# exception for reading file error
except IOError as exception:
    # handling exception
    print("File Read Error:",str(exception))  