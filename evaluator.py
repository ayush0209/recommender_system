import xlrd
import random
import math

def adder(x,y):
	s1=(x*(x+1))/2
	s2=(y*(y+1))/2
	return s2-s1


def spearman_rank_correlation_calculator(usr,prec,act):
	t1=list(zip(usr,prec,act))
	t1.sort(key=lambda x:(x[0],-x[1]))
	t2,t3,t4=zip(*t1)
	t5=list(zip(t3,t4))
	t5.sort(key=lambda x:(x[0]))
	t3,t4=zip(*t5)
	
	ranked_t3=[]
	nn=1
	for i in range(len(t3)):
		ranked_t3.append(nn)
		nn+=1

	ranked_t4=[]
	numb=[0,0,0,0,0]
	for i in range(len(t4)):
		numb[int(t4[i])-1]+=1
	
	r1=adder(0,numb[0])/numb[0]
	r2=adder(numb[0],numb[1]+numb[0])/numb[1]	
	r3=adder(numb[0]+numb[1],numb[2]+numb[1]+numb[0])/numb[2]
	r4=adder(numb[0]+numb[1]+numb[2],numb[3]+numb[2]+numb[1]+numb[0])/numb[3]
	r5=adder(numb[0]+numb[1]+numb[2]+numb[3],numb[4]+numb[3]+numb[2]+numb[1]+numb[0])/numb[4]
	for i in range(len(t4)):
		if(t4[i]==1):
			ranked_t4.append(r1)
		elif(t4[i]==2):
			ranked_t4.append(r2)
		elif(t4[i]==3):
			ranked_t4.append(r3)
		elif(t4[i]==4):
			ranked_t4.append(r4)
		elif(t4[i]==5):
			ranked_t4.append(r5)

	x=ranked_t3
	y=ranked_t4
	s1=sum(i for i in x)
	s2=sum(i for i in y)
	s11=sum(i**2 for i in x)
	s22=sum(i**2 for i in y)
	s12=0
	for i in range(len(x)):
		s12+=x[i]*y[i]
		
	num=(len(x)*s12-s1*s2)
	den=((len(x)*s11 - s1*s1)*(len(x)*s22 - s2*s2))**0.5
	cor=num/den
	print(cor)

def RMSE():
	loc=("answer.xlsx")
	wb=xlrd.open_workbook(loc) 	
	sheet=wb.sheet_by_index(0)
	tn=0
	p=0
	for i in range(sheet.nrows): 
		r=sheet.cell_value(i,0)
		n=sheet.cell_value(i,1)
		tn+=n
		p+=(r**2)*n
	RMSE_TOTAL=math.sqrt(p/tn)
	print(RMSE_TOTAL)

def average_precision_at_topK(usr,prec,act,max_row):
	t1=list(zip(usr,prec,act))
	t1.sort(key=lambda x:(x[0],-x[1]))
	t2,t3,t4=zip(*t1)
	random_users_list=random.sample(range(max_row),1000)
	precattopk=0
	den=0
	for i in range(len(random_users_list)):
		try:
			firstocc=t2.index(random_users_list[i])
			lastocc=len(t2)-t2[::-1].index(random_users_list[i])-1
			if((lastocc-firstocc)>=10):
				recommend=0
				relevant=0
				for j in range(firstocc,firstocc+10):
					if(t3[j]>3.5):
						recommend+=1
						if(t4[j]>3.5):
							relevant+=1
				if(recommend!=0):
					precattopk+=(relevant/recommend)
					den+=1
		except ValueError:
			continue
	average_precision_at_top_K=(precattopk/den)
	print(average_precision_at_top_K)