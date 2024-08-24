num=input("Enter a number:")
m={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
m1={10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"ninteen"}
m2={2:"twenty",3:"thirty",4:"fourty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninty"}
temp=None
count=0
text=[]
for i in reversed(num):
    i=int(i)
    count +=1
    if i==0:
        temp=i
        continue
    if count==1:
        text.append(m[i])
    elif count==2:
        if i==1:
            if text:
                text.pop()
            text.append(m1[i*10+temp])
        else:
            text.append(m2[i])
    elif count==3:
        text.append("hundred")
        text.append(m[i])
    elif count==4:
        text.append("thousand")
        text.append(m[i])
    elif count==5:
        if text:
            text.pop()
        if text:
            text.pop()
        text.append("thousand")
        
        if i==1:
            
            text.append(m1[i*10+temp])
        else:
            text.append(m[temp])
            text.append(m2[i])
    elif count==6:
        text.append("lakh")
        text.append(m[i])
    elif count==7:
        if text:
            text.pop()
        if text:
            text.pop()
        text.append("lakh")
        if i==1:
            
            text.append(m1[i*10+temp])
        else:
            text.append(m[temp])
            text.append(m2[i])
    elif count==8:
        text.append("crore")
        text.append(m[i])
    elif count==9:
        if text:
            text.pop()
        if text:
            text.pop()
        text.append("crore")
        if i==1:
            
            text.append(m1[i*10+temp])
        else:
            text.append(m[temp])
            text.append(m2[i])
    temp=i
for j in reversed(text):
    print(j,end=" ")