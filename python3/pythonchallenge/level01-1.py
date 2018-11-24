#http://www.pythonchallenge.com/pc/def/map.html
#Caesar Cipher

original_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
original_url = "map"

def caeser(crypt_string):
	result_list = []
	for i in crypt_string:
		if 96 < ord(i) < 123: 
			decrypt_char = chr(((ord(i) - 95) % 26) + 97)
		else:
			decrypt_char = i
		result_list.append(decrypt_char)
	result_string = ''.join(result_list)
	return result_string
	
print("original string :", original_string)
print("decrypt string :", caeser(original_string))
print("original url :", original_url)
print("ANSWER :", caeser(original_url))
