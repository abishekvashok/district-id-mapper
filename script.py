dist = open("district.csv", "r")
district_info = dist.read()
dist.close()
info = []
for district in district_info.split("\n"):
	i = district.split(",")
	if(len(i) > 1):
		info.append((i[1], i[2]))
d = 'list('
ids = 'list('
for i in info:
	d = d + '"'+i[0]+'",'
	ids = ids + '"'+i[1]+'",'
ids = ids + ')'
d = d + ')'
print(ids)
print(d)