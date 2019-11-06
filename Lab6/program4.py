import xlrd

file=xlrd.open_workbook("File.xlsx");

worksheet=file.sheet_by_index(0);
len_of_row=worksheet.nrows;
len_of_col=worksheet.ncols;
for i in range(0,len_of_row):
    for j in range(0,len_of_col):
        print(worksheet.cell_value(i,j),end=' ');
    print("");

print("\n");
print("\n");

print("Number of rows = ",len_of_row);
print("Number of columns = ",len_of_col);
print("Total number of elements in excel file = ",len_of_row*len_of_col);
