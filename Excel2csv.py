import xlrd
import csv
import sys

if len( sys.argv ) < 2:
    print( 'No arguments have been given' )   
    print( 'Usage: Excel2csv.py <excelfile> <outputfilename>' )   
    print( 'e.g. Excel2csv.py test.csv test.txt' )   
    exit( 1 )

try:
    _filename = sys.argv[1]
    _output = sys.argv[2]
except Exception as e:
    print(e)

workbook = xlrd.open_workbook(_filename)
sheet_names = workbook.sheet_names()

for i in range(0, len(sheet_names)):
    
    for k in range(0, workbook.sheet_by_index(i).nrows):
        output = sheet_names[i]  
        for l in range(0, len(workbook.sheet_by_index(i).row_values(k))):
            output += ','+ str(workbook.sheet_by_index(i).row_values(k)[l])            
        print(output)
        output_filename = _output
        writer = open(output_filename,'a+')
        writer.write(output + '\n')
        writer.close()
