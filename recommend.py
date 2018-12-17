import xlrd
from sklearn.model_selection import train_test_split
from feeder import feed_training_and_testing_data_set

def main():
	loc=("ratings.xlsx") 
		
	row_list=[]
	col_list=[]
	rating_list=[]
	max_row_index=0
	max_col_index=0

	wb=xlrd.open_workbook(loc) 	
	sheet=wb.sheet_by_index(0) 

	#reading data from excel file
	for i in range(sheet.nrows): 
		t1=sheet.cell_value(i,0)
		t2=sheet.cell_value(i,1)
		row_list.append(t1-1)
		col_list.append(t2-1)
		rating_list.append(sheet.cell_value(i,2))
		if t1>max_row_index:
			max_row_index=t1
		if t2>max_col_index:
			max_col_index=t2

	max_row_index=int(max_row_index)
	max_col_index=int(max_col_index)

	pos_list=list(zip(row_list,col_list))

	#splitting dataset into training and testing dataset
	pos_train,pos_test,rating_train,rating_test=train_test_split(pos_list,rating_list,test_size=0.20,random_state=11)
	feed_training_and_testing_data_set(pos_train,pos_test,rating_train,rating_test,max_row_index,max_col_index)
	
if __name__ == '__main__':
	if(main()==-1):
		sys.exit(0)