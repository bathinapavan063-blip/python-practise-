'''disk_sage=95
if disk_sage>80:
    print("send alert")
else:
    print("fine")
'''
environment="production"
approval_given=True
if environment == "production" and not approval_given:
    print("deployment blocked:roval required")
else:
    print("deployment allowed")
