#!/usr/bin/python3.6

def open_file(file_name):
	f = open(file_name, "a")
	f.write(string_for_file)
	f.close()

def reading_file(file_name):
	f = open(file_name, "r")
	for line in f:
		print(line, end='')
	f.close()

print("put your filename here:")
file_name = input()

print("put your string for file here:")
string_for_file = input() + "\n"

open_file(file_name)
reading_file(file_name)








