server_name="prod_web_o1"
cpu_usage=78
memory_usage=82.5
disk_usage=65

cpu_limit=80
memory_limit=80
disk_limit=75

print("server_name:",server_name)
print("cpu_usage:",cpu_usage,"%")
print("memory_usage:",memory_usage,"%")
print("disk_usage:",disk_usage,"%")

#health check 
if cpu_usage > cpu_limit:
    print("Alert")
else:
    print("warning:","usage is normal")    
if memory_usage > memory_limit:
    print("warning:","Alert")    
else:
    print("usage is normal")    
if disk_usage > disk_limit:
    print("Alert")    
else:
    print("usage is normal")    