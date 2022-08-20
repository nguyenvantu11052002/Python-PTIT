
def check (n):
	flag = 1;
	if (n % 2 == 0):
		flag = 0
	return flag

n = int(input())
ok = check(n)
if ok:
	print("LE")
else:
	print("CHAN")
