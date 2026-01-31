'''text="aws devops python"
words=text.split()
print(words)
'''
'''
log="error nginx 503"
parts=log.split()
level=parts[0]
service=parts[1]
code=parts[2]

print(f"level:{level}\nservice:{service}\ncode:{code}")
'''
'''
ip="112.667.8.9.898"
parts=ip.split(".")
print(parts)
'''
'''
data="user:pavan:admin"
result=data.split(":",1)
print(result)
'''
log="Accepted password for pavan from 123.3454.66.7.889"
words=log.split()
username=words[3]
ip=words[5]
print(f"user:{username}\n ip is:{ip}")