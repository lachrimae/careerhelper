import csv

def __main__():
    infile = open('soc_structure_2010.csv', 'r')
    majorfile = open('major_groups.csv', 'w')
    minorfile = open('minor_groups.csv', 'w')
    broadfile = open('broad_groups.csv', 'w')
    occupfile = open('detailed_occupations.csv', 'w')

    try:
        infile.seek(0)
        csvreader = csv.reader(infile, delimiter=",", quotechar='"')

        majors = []
        minors = []
        broads = []
        occups = []

        rown = 0
        for row in csvreader:
            name = row[4]
            if row[0] != '':
                majors.append(row[0] + ',' + name)
            if row[1] != '':
                minors.append(row[1] + ',' + name)
            if row[2] != '':
                broads.append(row[2] + ',' + name)
            if row[3] != '':
                occups.append(row[3] + ',' + name)
            rown += 1
            print(majors)
        
    finally:
        header = "SOC Code,Title\n" 
        majors = header + "\n".join(majors)
        minors = header + "\n".join(minors)
        broads = header + "\n".join(broads)
        occups = header + "\n".join(occups)

        majorfile.write(majors)
        minorfile.write(minors)
        broadfile.write(broads)
        occupfile.write(occups)
        print(rown)
        infile.close()
        majorfile.close()
        minorfile.close()
        broadfile.close()
        occupfile.close()

