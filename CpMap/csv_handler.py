import csv
# Module for importing csv data into python list of lists

def rows_counter(f):
    'count the row number of the csv file'
    with open(f) as openf:
        reader=csv.reader(openf)
        rows=0
        for row in reader:#get every line of the reader
            if row[0]!='':
                rows+=1
    return rows
    

def cols_counter(f):
    'count the column number of the csv file'
    with open(f) as openf:
        reader=csv.reader(openf)
        cols=0
        for row in reader:
            for i in range(len(row)):
                if row[i]!='':
                    cols+=1
            break
    return cols
    
          
def csv_to_lists(f):
    'transfer the csv data into list of lists'
    rows=rows_counter(f)
    cols=cols_counter(f)
    
    #build up a lists container to contain data from csv
    lists=[[]]
    for i in range(1,cols):
        lists.append([])

    #input the data into list of lists
    reader=csv.reader(open(f))
    flag=0    
    for row in reader:
        if flag<rows:
           for i in range(cols):
               lists[i].append(float(row[i]))
           flag+=1
        else:
            break
    return lists
            
         
if __name__=="__main__":
   #update the following file name according to your file address
   CSVFILE_FULL_NAME='/Users/Extremeways/Desktop/csvfile.csv'
   print csv_to_lists(CSVFILE_FULL_NAME)    
    
    
    
    
    
    
    