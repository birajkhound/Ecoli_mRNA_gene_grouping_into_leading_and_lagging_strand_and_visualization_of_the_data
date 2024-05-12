#library to read excel file
import openpyxl

# for the file 1300_gene_coordinates
# Define variable to load the dataframe
dataframe1300 = openpyxl.load_workbook("1300_gene.xlsx")
# Define variable to read sheet
dataframe1300 = dataframe1300.active
# number of rows in file 1300_gene
count_rows_1300 = len([row for row in dataframe1300 if not all([cell.value == None for cell in row])])


# for the file 4000_gene_coordinates
dataframe4000 = openpyxl.load_workbook("4000_gene_coordinates.xlsx")
# Define variable to read sheet
dataframe4000 = dataframe4000.active
# number of rows in file 4000_gene
count_rows_4000 = len([row for row in dataframe4000 if not all([cell.value == None for cell in row])])
#count Columns in each row
count_col_4000 = len(dataframe4000[1])



# Iterate the loop to read the cell values
# for row in range(1, count_rows_4000 + 1):
#         print(dataframe4000[row][count_col_4000-1].value)
#         print(dataframe4000[row][0].value)
#         print(dataframe4000[row][1].value)

#starting coordinate of leading stand
les_start1 = 0
les_start2 = 3927000
#ending coordinate of lagging stand
les_end1 = 157800
les_end2 = 4635000

#this loop to iterate all the rows of the file containing 1300 genes 
for gene1 in range(1,count_rows_1300 +1):
#this loop to check all the rows of the file containing 4000 genes     
    for row in range(1, count_rows_4000 + 1):
#this if condition is to check whether the gene in 1300_gene file contain in the 4000_gene file        
        if 'gene='+dataframe1300[gene1][0].value in dataframe4000[row][count_col_4000-1].value :
            # print(dataframe1300[gene][0].value)
            # print(dataframe4000[row][0].value)
            # print(dataframe4000[row][1].value)
#storing the starting coordinate available in 4000_gene file against the gene available in 1300_gene file            
            starting_coordinate = dataframe4000[row][0].value
#storing the ending coordinate available in 4000_gene file against the gene available in 1300_gene file               
            ending_coordinate = dataframe4000[row][1].value
#checking  whether it is in LeS or LaS           
            if (starting_coordinate > les_start1 and ending_coordinate < les_end1) or (starting_coordinate > les_start2 and ending_coordinate < les_end2) :
                print(dataframe1300[gene1][0].value, 'LeS', starting_coordinate , ending_coordinate)
            else :
                print(dataframe1300[gene1][0].value, 'LaS', starting_coordinate , ending_coordinate)    
