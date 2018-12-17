import timeit
import numpy as np
import math
import multiprocessing
from scipy import sparse 
from openpyxl import load_workbook
from rater import rating_calculator
from evaluator import RMSE,spearman_rank_correlation_calculator,average_precision_at_topK

npr=4

def mag(x): 
    return math.sqrt(sum(i**2 for i in x))

def average_out_ratings_and_row_normalize(maxm,sparse_matrix):
	for i in range(maxm):
		sum_of_elements_in_row=0
		row_start_index_in_data_list=sparse_matrix.indptr[i]
		row_end_index_in_data_list=sparse_matrix.indptr[i+1]
		no_of_elements_in_row=row_end_index_in_data_list-row_start_index_in_data_list
		row_data=sparse_matrix.data[row_start_index_in_data_list:row_end_index_in_data_list]

		for d in range(len(row_data)):
			sum_of_elements_in_row+=row_data[d]

		average=sum_of_elements_in_row/no_of_elements_in_row

		for d in range(len(row_data)):
			row_data[d]=row_data[d]-average

		row_data=sparse_matrix.data[row_start_index_in_data_list:row_end_index_in_data_list]
		row_length=mag(row_data)

		for d in range(len(row_data)):
			row_data[d]/=row_length


def feed_training_and_testing_data_set(pos_train,pos_test,rating_train,rating_test,max_row,max_col):

	row_train,col_train=zip(*pos_train)
	row_test,col_test=zip(*pos_test)

	#declaring variables and arrays in shared memory to store user,actual rating and predicted rating
	usr=multiprocessing.Array('i',len(row_test))
	act=multiprocessing.Array('d',len(row_test))
	prec=multiprocessing.Array('d',len(row_test))

	usrindx=multiprocessing.Value('i')
	actindx=multiprocessing.Value('i')
	precindx=multiprocessing.Value('i')

	usrindx.value=0
	actindx.value=0
	precindx.value=0

	row_train=np.asarray(row_train)
	col_train=np.asarray(col_train)
	rating_train=np.asarray(rating_train)

	#creating sparse matrix from training dataset
	original_sparse_matrix=sparse.csr_matrix((rating_train,(row_train,col_train)),shape=(max_row,max_col))
	sparse_matrix=original_sparse_matrix.copy()

	average_out_ratings_and_row_normalize(max_row,sparse_matrix)
	
	sparse_matrix_transpose=sparse_matrix.transpose()

	lock=multiprocessing.Lock()#lock variable from multiprocessing module
	
	start=timeit.default_timer()

	pr={}
	for k in range(npr):
		#generating multiple processes  
		pr[k]=multiprocessing.Process(target=rating_calculator, args=(k,row_test,col_test,rating_test,sparse_matrix,sparse_matrix_transpose,max_row,original_sparse_matrix,lock,usr,act,prec,usrindx,actindx,precindx)) 
		pr[k].start()

	for k in range(npr):
		pr[k].join()

	stop=timeit.default_timer()
	time_taken=(stop-start)/len(row_test)

	#finding RMSE from RMSE calculated by various processes after reading what these processes have written to excel file
	RMSE()
	
	#average precision at topK
	average_precision_at_topK(usr,prec,act,max_row)

	#spearman rank correlation
	spearman_rank_correlation_calculator(usr,prec,act)
