#This program transfer coordinates(x,y) and third value as color into contour graphic

from csv_handler import csv_to_lists, rows_counter, cols_counter
import matplotlib.pyplot as plt

CSVFILE_FULL_NAME='/Users/Extremeways/Desktop/csvfile.csv'
LISTS=csv_to_lists(CSVFILE_FULL_NAME)
ROWS=rows_counter(CSVFILE_FULL_NAME)
COLS=cols_counter(CSVFILE_FULL_NAME)
CP_COUNT=COLS-2

#define your cp spec as following
L1=30
H1=100
C1='r'

L2=30
H2=100
C2='y'

L3=0
H3=1.9
C3='b'

COLOR_SPEC=[[L1,H1,C1],[L2,H2,C2],[L3,H3,C3]]

def cp_color(LISTS):
    'transfer cp to specific color'
    
    #set the default color to green
    color=[]
    for i in range(ROWS): 
        color.append('g')

    #Reset the color according to the COLOR_SPEC
    for i in range(ROWS):
        #redefine the color for every row

        if LISTS[2][i]<L1 or LISTS[2][i]>H1:
            color[i]=C1
        
        elif LISTS[3][i]<L2 or LISTS[3][i]>H2:
            color[i]=C2
        
        elif LISTS[4][i]<L3 or LISTS[4][i]>H3:
            color[i]=C3
        
    return color


c=cp_color(LISTS)
         
plt.scatter(x=LISTS[0],y=LISTS[1],c=c,alpha=1,s=2,edgecolors=c)
g=plt.savefig('/Users/Extremeways/Desktop/cpMapping.png')      
plt.show()

