import acitoolkit

url = 'https://10.10.20.14'
user = 'admin'
pwd = 'C1sco12345'

#create a session
session = Session(url, user, pwd)
session.login()
#get all tenants
tenants = Tenant.get(session)

for tenant in tenants:
    print(tenant.name)
    print(tenant.descr)
    print('*' * 30)
    print(' ')
