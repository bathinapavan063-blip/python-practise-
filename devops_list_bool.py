services={
    "nginx" : True,
    "docker": True,
    "jenkins": False,
    "ssh": True
}

print("services status report\n")
for service,status in services.items():
    if status:
        print(service,":running")
    else:
        print(service,":stopped")    