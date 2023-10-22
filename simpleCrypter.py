from easygui import *
import sys

#Tampilan GUI
msg = "Masukkan Plainteks dan key dibawah ini"
title = "Kriptografi Klasik Caesar Cipher"
fieldNames = ["Masukkan Plainteks", "Masukkan key"]
fieldValues = multenterbox(msg, title, fieldNames)
if fieldValues is None:
	sys.exit(0)
#Pastikan bahwa tidak ada satu pun dari kolom dibiarkan kosong
while 1:
	errmsg = ""
	for i, name in enumerate(fieldNames):
		if fieldValues[i].strip() == "":
			errmsg += "{} is a required field.\n\n".format(name)
	if errmsg == "":
		break
	fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
	if fieldValues is None:
		break
dataIn = fieldValues

#Logic Part
alph = ("abcdefghijklmnopqrstuvwxyz")
msg = dataIn[0]
strKey = dataIn[1]
key = int(strKey)
newMsg = ""
for char in msg:
	if char in alph:
		pos = alph.find(char)
		newPos = (pos + key) % 26
		newChar = alph[newPos]
		newMsg += newChar
	else:
		newMsg += char
#Menampilkan Pesan yang di enkripsi/dekripsi
msgbox(msg = newMsg)
