# -*- coding: UTF-8 -*-
from __future__ import print_function

def error_logger():
  	Log=open('error_log')
	error_log=[]
	for i in Log:
			if i.find("[error]") != -1:
				error_log.append(i)
	return error_log

def error_counter():
	Log=open('error_log')
	counter=0
	for i in Log:
		if i.find("[error]") != -1:
			counter+=1
	return counter

def notice_logger():
	Log=open('error_log')
	notice_log=[]
	for i in Log:
		if i.find("[notice]") != -1:
			notice_log.append(i)
	return notice_log

def notice_counter():
	Log=open('error_log')
	counter=0
	for i in Log:
		if i.find("[notice]") != -1:
			counter+=1
	return counter	

def warn_logger():
	Log=open('error_log')
	warn_log=[]
	for i in Log:
		if i.find("[warn]") != -1:
			warn_log.append(i)
	return warn_log

def warn_counter():
	Log=open('error_log')
	counter=0
	for i in Log:
		if i.find("[warn]") != -1:
			counter+=1
	return counter

def else_logger():
	Log=open('error_log')
	else_log=[]
	for i in Log:
		if i.find("[error]") == -1:
			if i.find("[notice]") == -1:
				if i.find("[warn]") == -1:
					else_log.append(i)
	return else_log

def else_counter():
	Log=open('error_log')
	counter=0
	for i in Log:
		if i.find("[error]") == -1:
			if i.find("[notice]") == -1:
				if i.find("[warn]") == -1:
					counter+=1
	return counter

def All_counter():
	print ("error_log :", error_counter())
	print ("notice_log :",notice_counter())
	print ("warn_log :", warn_counter())
	print ("else_log :",else_counter())

def log_printer(log):
	splog=[]
	for i in log:
		splog=i.split ('] ')
		if(len(splog) <= 3):
			print (splog[2])
		else:
			print (splog[2]+"]"+splog[3])

def log_printer2(log):
	for i in log:
		print (i)

def optionSelecter():
	print ("Choose the option : ")
	print ("1. details of error messages")
	print ("2. details of notice messages")
	print ("3. details of warning messages")
	print ("4. details of other messages")

	selNum=raw_input()

	while(selNum==''):
		print ("input the number!")
		selNum=raw_input()			
	selNum=int(selNum)

	if selNum==1:
		print ("Error messages : \n")
		log_printer(error_logger())
	elif selNum==2:
		print ("Notice messages : \n")
		log_printer(notice_logger())
	elif selNum==3:
		print ("Warning messages : \n")
		log_printer(warn_logger())
	elif selNum==4:
		print ("Other messages : \n")
		log_printer2(else_logger())
	else:
		print("\n")
		print (line)
		print ("Choose the Number between 1~4.")
		optionSelecter()


line="============================================================================\n"
print("\n")
print (line)
print ("Number of each type of message : \n")
All_counter()
print("\n")
print (line)

optionSelecter()
