import birthday_match,random,time
random.seed(time.time())
def xba(x):
	A={}
	for(C,D)in x.items():
		B=str(D)
		if B not in A:A[B]=[]
		A[B].append(C)
	E=[A for(B,A)in A.items()if len(A)>1];return E
def test_birthday_match():
	C=birthday_match.get_random_people_birthdays();D=birthday_match.find_birthday_matches(C);A=xba(C);E=set(tuple(sorted(A))for A in D);F=set(tuple(sorted(A))for A in A);B='Birthday matches do not match the expected result.'
	if A:B+=f" I expected {len(A)} matches.";B+=f" One of the matches should be: {A[0]}"
	assert E==F,B