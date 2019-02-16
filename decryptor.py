text = "dygfopejposqptdygfopepdyitdygfopefjtlofyexhjx"
key = 5
alph = "qwertyuiopasdfghjklzxcv bnm:/"
decrypted = ""

for i in text:
	index = alph.find(i)
	new_pos = (index-key)%26
	decrypted += alph[new_pos]

print("decrypted : " + decrypted)
