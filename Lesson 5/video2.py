
def print_ip(ip_addr, username='admin', password='cisco123'):
	print("My IP address is: {}".format(ip_addr))
	print (username)
	print(password)
	return
	
my_dict = {"ip_addr":'10.1.1.1', "password":'admin123'}

print_ip(**my_dict)