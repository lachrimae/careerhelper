import csv
import sys
import os

def properArgsCheck(args, cwd):
    if len(args) != 3:
        raise ValueError('Takes exactly two arguments: infolder and outfolder.')

    args = args[1:] # get rid of scriptname
    for folder in args:
        if not os.path.isdir(os.path.join(cwd, folder)):
            raise NotADirectoryError("Argument '" ++ folder ++
                    "' is not a valid subdirectory of the working " ++
                    "directory.")

    if not os.path.isfile(os.path.join(cwd, sys.argv[1] + '/soc_structure_2010.csv')):
        raise FileNotFoundError("'soc_structure_2010.csv' does not exist in the folder " + os.path.join(cwd, sys.argv[1]) + ".")

