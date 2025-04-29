# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:22:19 2019

@author: kip
"""

import sys
import datetime
import os
from subprocess import call


def runAPDL(ansyscall,workingdir,scriptFilename):

    """
    runs the APDL script: scriptFilename.inp
    located in the folder: workingdir
    using APDL executable invoked by: ansyscall
    using the number of processors in: numprocessors
    returns the number of Ansys errors encountered in the run
    """
    inputFile = os.path.join(workingdir,
                             scriptFilename+".txt")
    # make the output file be the input file plus timestamp
    outputFile = os.path.join(workingdir,
                              scriptFilename+
                              '{:%Y%m%d%H%M%S}'.format(datetime.datetime.now())+
                              ".out")
    # keep the standard ansys jobname
    jobname = "file"
    callString = ("\"{}\" -p ansys"
              " -dir \"{}\" -j \"{}\" -s read"
              " -b -i \"{}\" -o \"{}\"").format(
                      ansyscall,
                      workingdir,
                      jobname,
                      inputFile,
                      outputFile)             
#    print("invoking ansys with: ",callString)
    call(callString,shell=False)
    print('Start ANSYS') 
    # check output file for errors
#    print("checking for errors")
    numerrors = "undetermined"
    try:
        searchfile = open(outputFile, "r")
    except:
        print("could not open",outputFile)
    else:
        for line in searchfile:
            if "NUMBER OF ERROR" in line: 
                print(line)
                numerrors = int(line.split()[-1])
        searchfile.close()        
    return(numerrors)
    
    

def run(scriptFilename, pathansys, pathwork):
    global error 
    ansyscall = pathansys
    workingdir = pathwork
    nErr = runAPDL(ansyscall,
                   workingdir,
                   scriptFilename)
    return nErr
#    print ("number of Ansys errors: ",nErr)
    
    
        
    
    
 
