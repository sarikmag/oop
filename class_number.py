class Number:
    def __init__(self,number):
        self.number=number
    def get_number(self):
        return number
    def is_even(self):
        return self.number%2==0
    def is_odd(self):
        return self.number%2==1
    def is_prime(self):
        if self.number < 2:
            return False
        if self.number == 2:
            return True
        if self.number%(self.number**0.5)==0:
            return False
        for i in range(2, self.number // 2 + 1):
            if self.number % i == 0:
                return False
            return True
    def is_divisiors(self):
        return 
    def get_lenght(self):
        return len(str(self.number))
    def get_sum(self):
        s=0
        n=self.number
        while n:
            s+=n%10
            n//=10
        return s
    def get_product(self):
        s=1
        s1=[]
        while self.number:
            s1+=[self.number%10]
            self.number//=10
        for i in s1:
            s*=i
        return s
    def get_reverse(self):
        s1=[]
        s=''
        while self.number:
            s1+=[self.number%10]
            self.number//=10
        for i in s1:
            s+=str(i)
        return int(s)
    def get_digits(self):
        s=str(self.number)
        s1=[]
        for i in s:
            s1+=[int(i)]
        return s1
    def get_max(self):
        s=str(self.number)
        s1=[]
        for i in s:
            s1+=[int(i)]
        return max(s1)
    def get_min(self):
        s=str(self.number)
        s1=[]
        for i in s:
            s1+=[int(i)]
        return min(s1)
    def get_average(self):
        return
    def get_frequensy(self):
        s=str(self.number)
        s1={}
        n=1
        for i in s:
            s1[n]=int(i)
            n+=1
        return s1
x=Number(number=544)
print(x.get_frequensy())
