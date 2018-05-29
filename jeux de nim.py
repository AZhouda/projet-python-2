
# coding: utf-8

# In[ ]:


import pandas as pd 
import numpy as np 
import random
from math import pow
import operator



list1=[]
list2=[]
list_final = []
players=[]
Record_dict={}

def all_player(): 
	df=pd.read_csv('players.csv', sep=',',header=None)
	for d in df.values:
		if(d[1]!='Username'):
				
				Record_dict[d[1]]=d[3]
	
	top_10 =reversed(sorted(Record_dict.items(), key=operator.itemgetter(1)))
	for element in top_10:
		print (element)

def check_existance(username,df): 
	gg=df.loc[(df["Username"] == username)]['Best_Score']
	if gg.empty is True : 
		return True
	else :
		return False
	

def create_file_score():
	df=pd.DataFrame(columns =['Username','Last_score','Best_Score'])
	a='players'+'.csv'
	gg=str(a)
	df.to_csv(gg)


def create_game():
	user1 = input('Enter a Player 1 : ')
	user2 = input('Enter a Player 2 : ') 
	df = pd.read_csv('players.csv',index_col=0)
	if(check_existance(user1,df)):
		df = df.append({'Username': user1, 'Last_score':0, 'Best_Score': 0}, ignore_index=True)
		list1.append(user1)
		list1.append(0)
		list1.append(0)
	else :
		list1.append(user1)
		list1.append(df.loc[(df["Username"] == user1)]['Last_score'].all())
		list1.append(df.loc[(df["Username"] == user1)]['Best_Score'].all())

		
	if(check_existance(user2,df)):
		df = df.append({'Username': user2, 'Last_score':0, 'Best_Score': 0}, ignore_index=True)
		list2.append(user2)
		list2.append(0)
		list2.append(0)
	else :
		list2.append(user2)
		list2.append(df.loc[(df["Username"] == user2)]['Last_score'].all())
		list2.append(df.loc[(df["Username"] == user2)]['Best_Score'].all())		



	filename='players'+'.csv'
	df.to_csv(str(filename))
	
def start_game(): 
	
	nbr_tas=random.randint(3,7)
	for i in range (0,nbr_tas):
		first_item=str(i+1)+"|"
		piere_tas=random.randint(5,23)
		seconditem="	"
		for j in range(0,piere_tas):
			seconditem=seconditem+"*"
		list_final.append(seconditem[1:])
		for k in range(0,23-piere_tas):
			seconditem=seconditem+" "

		print(first_item+seconditem+"|"+str(piere_tas))
	

def retirer(how_much):
	Numero_number=how_much.split("-")
	Numero=int(Numero_number[0])-1
	Number=int(Numero_number[1])
	while(Numero<0 or  Numero>=len(list_final)):
		print("it's empty pick something else ")
		how_much=input("how_much ")
		Numero_number=how_much.split("-")
		Numero=int(Numero_number[0])-1

	x=list_final[Numero]
	x=x[Number:]
	list_final[Numero]=x

def afficher_game():
	for i in range(0,len(list_final)):
		x=list_final[i]
		first_item=str(i+1)+"|	"+list_final[i]
		for j in range(0,23-len(x)):
			first_item=first_item+" "
		first_item=first_item+"|"+str(len(x))
		print(first_item)


def len_total():
	return len(''.join(list_final))

def score(nbcoup):
	somme=0
	for i in range (1,nbcoup+1):
		y=pow(10,i)
		somme=somme+(i*y)
	return somme

def game():
	create_game()
	start_game()
	players.append(list1[0])
	players.append(list2[0])
	playerindex=0
	compt=0
	while(len_total()>1):
		print("Player  "+players[playerindex]+" Plays ")
		chaine=input("how_much ")
		x=len_total()
		retirer(chaine)
		while(len_total()==x):
			print("it's empty pick something else ")
			chaine=input("how_much ")
			retirer(chaine)


		afficher_game()
		playerindex=playerindex+1
		playerindex=playerindex%2
		compt+=1

	print("you lost "+players[playerindex])
	loser=playerindex
	index_gan=(playerindex+1)%2
	print(" he plays "+str(compt))
	print("Player "+players[index_gan]+" wins and his score " +str(score(compt)))
	df1 = pd.read_csv('players.csv',index_col=0)
	if(df1.loc[(df1["Username"] == players[index_gan])]['Best_Score'].all()<score(compt)):
		df1.loc[(df1["Username"] == players[index_gan]),"Best_Score"]=score(compt)
	df1.loc[(df1["Username"] == players[index_gan]),"Last_score"]=score(compt)

	df1.loc[(df1["Username"] == players[loser]),"Last_score"]=0
	filename='players'+'.csv'
	df1.to_csv(str(filename))
	with open('players.txt','w'): pass
	df1.to_csv(r'players.txt', header=None, index=None, sep=' ', mode='a')


while True:
	list1=[]
	list2=[]
	list_final = []
	players=[]
	Record_dict={}
	game()
	print("1-Play Again   ")
	print("2-Top 10 players ")
	x=input("1 OR 2 ")
	if(x=="2"):
		break

all_player()

