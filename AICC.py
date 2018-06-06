def printinfo(fruit,quantity):
	return [fruit,quantity]
	
def list_pos(a,n):
	return a[n]
	
def volume_calculate(r,h):
	return int((1/3)*h*3.14*r*r*100)/100
	
def grade_check(grader):
	if grader>=0 and grader<=59:
		return 'fail'
	elif grader>=60 and grader<=69:
		return 'pass'
	elif grader>=70 and grader<=79:
		return 'fair'
	elif grader>=80 and grader<=89:
		return 'good'
	elif grader>=90 and grader<=100:
		return 'excellent'
	else:
		return 'out of range'
		
def BMI_judger(weight,height):
	if height>=10:
		height/=100
	bmi=weight/(height*height)
	if bmi<=18.5:
		return 'underweight'
	elif bim<=25:
		return 'normal weight'
	elif bim<=30:
		return 'overweight'
	else:
		return 'obese'

def minus_sum(n):
	sum=0
	for i in range(1,n+1):
		if i%2!=0:
			i=-i
		sum+=i
	return sum
	
def range_Prime(n):
	ans=[]
	for i in range(2,n):
		flag=True
		for j in range(2,int(i**0.5+1)):
			if i%j==0:
				flag=False
				break
		if flag:
			ans.append(i)
	return ans
	
def factorial_digit_sum(n):
	num=1
	ans=0
	for i in range(2,n+1):
		num*=i
	num=list(str(num))
	for i in num:
		ans+=int(i)
	return ans
	
def sum_each_column(list_1):
	ans=[]
	for i in range(0,len(list_1)):
		ans.append(0)
	for i in range(0,len(list_1)):
		for j in range(0,len(list_1[0])):
			ans[j]+=list_1[i][j]
	return ans

def multiples(n):
	i=1
	ans=0
	while 3*i<n:
		ans+=3*i
		if 5*i<n:
			ans+=5*i
		i+=1
	return ans
	
def fibo(n):
	l=[1,1]
	for i in range(0,n):
		l.append(l[i]+l[i+1])
	return l[n-1]
	
def check_palin(n):
	return list(str(n))==list(reversed(str(n))
	
def max_path_sum(A):
	l=list(reversed(A))
	for i in range(0,len(l)-1):
		for j in range(0,len(l[i])-1):
			l[i+1][j]+=max(l[i][j],l[i][j+1])
	return l[len(l)-1][0]
	
def get_all_factors(num):
	return [i for i in range(1,num+1) if num%i==0]
	
def sub_list_sum(list_1):
	max=0
	sum=0
	for i in range(0,len(list_1)):
		sum=0
		for j in range(i,len(list_1)):
			sum+=list_1[j]
			if sum>max:
				max=sum
	return max