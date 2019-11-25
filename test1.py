import getpass
user = getpass.getuser()
passwd = getpass.getpass()


def svc_login(user, passwd):
    pass


if svc_login(user, passwd):
    # You must write svc_login()
    print('Yay!')
else:
    print('Boo!')

print('useless')
print('keep going')