
# coding: utf-8

import pandas as pd
import sys
import getopt

def main():

    inputFile = ''
    outputFile = ''

    try:
        opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["ifile=","ofile=", "help"])
    except getopt.GetoptError:
        print('Error. Aborting operation.')
        sys.exit(2)

    for opt, arg in opts:
        if (opt == '-h' or opt == '--help'):
            print('Type the command below:')
            print('python excel2array.py -i <completeInputFileName.xlsx> -o <completeOutputFileName.txt>')
            sys.exit()
        elif (opt == "-i"):
            inputFile = arg
        elif (opt == "-o"):
            outputFile = arg

    try:
        df = pd.read_excel(inputFile)
    except:
        print('Excel file not found')
        sys.exit()

    columns = df.axes[1].values

    print('Starting execution')

    with open(outputFile, "w") as text_file:
        print('array(', file=text_file)
        for i in range(len(df)):
            print('    array(', file=text_file)
            for c in columns:
                print('       "{}" => "{}", '.format(c, df[c][i]), file=text_file)
            print('    ),', file=text_file)
        print(")", file=text_file)

    print('Operation finished successfully  ;)')

if __name__ == "__main__":
    main()

