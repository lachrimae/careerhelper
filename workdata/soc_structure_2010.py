import csv
import sys
import os

def tests(cwd):
    if len(sys.argv) != 3:
        raise ValueError('Takes exactly two arguments: infolder and outfolder.')

    args = sys.argv[1:]
    for folder in args:
        if not os.path.isdir(os.path.join(cwd, folder)):
            raise NotADirectoryError("Argument '" ++ folder ++
                    "' is not a valid subdirectory of the working " ++
                    "directory.")

    if not os.path.isfile(os.path.join(cwd, infolder + '/soc_structure_2010.csv'):
        raise FileNotFoundError("'soc_structure_2010.csv' does not exist in the input folder.")

def main():
    firstdataline = 14 # was manually determined by reading the file
    cwd = os.getcwd()

    tests(cwd)
    
    infolder = sys.argv[1]
    outfolder = sys.argv[2]

    infile = open(os.path.join(infolder, 'soc_structure_2010.csv'), 'r')
    majorfile = open(os.path.join(outfolder, 'major_groups.csv'), 'w')
    minorfile = open(os.path.join(outfolder, 'minor_groups.csv'), 'w')
    broadfile = open(os.path.join(outfolder, 'broad_groups.csv'), 'w')
    occupfile = open(os.path.join(outfolder, 'detailed_occupations.csv'), 'w')

    try:
        csvreader = csv.reader(infile, delimiter=",", quotechar='"')

        majors = []
        minors = []
        broads = []
        occups = []

        rowCount = 0
        for row in csvreader:
            rowCount += 1 
            if rowCount >= firstdataline
                name = row[4]
                if row[0] != '':
                    majors.append(row[0] + ',' + name)
                if row[1] != '':
                    minors.append(row[1] + ',' + name)
                if row[2] != '':
                    broads.append(row[2] + ',' + name)
                if row[3] != '':
                    occups.append(row[3] + ',' + name)

        header = "SOC Code,Title\n" 
        majors = header + "\n".join(majors)
        minors = header + "\n".join(minors)
        broads = header + "\n".join(broads)
        occups = header + "\n".join(occups)

        majorfile.write(majors)
        minorfile.write(minors)
        broadfile.write(broads)
        occupfile.write(occups)

    finally:
        infile.close()
        majorfile.close()
        minorfile.close()
        broadfile.close()
        occupfile.close()

if __name__ == "__main__":
    main()
