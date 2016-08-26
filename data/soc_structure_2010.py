import csv
import sys
import os

import tests

def main():
    firstdataline = 14 # was manually determined by reading the file

    tests.properArgsCheck(sys.argv, os.getcwd())
    
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
            if rowCount >= firstdataline:
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
