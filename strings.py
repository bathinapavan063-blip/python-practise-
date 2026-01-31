'''str="pavan"
print(str[0::])
'''
'''first="pavan"
last="Bathina"
full = first+" "+last
print(full)
'''
'''
str1="pavanbathina"
print(len(str1))
'''
'''
name=input(" ")
age=int(input())
print(f"my name is {name} and iam {age} years old","\n")
'''
'''
server="web-01"
cpu=82
memory=76
disk=91
print(f"""
    server health report
      server name:{server}  
      cpu usage  : {cpu}%
      memory usage:{memory}%
      disk usage:{disk}%
      """)
if disk>90:
    print(f"alert:disk usage{server} is critcal")
    '''
name=input(" ")
ip=float(input())
print(f"user {name} logged in ip address {ip}")
