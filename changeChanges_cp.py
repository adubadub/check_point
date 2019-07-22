from getpass import getpass

username = input("What is the applicable Username: ")
password = getpass()

device = {
    'host': '''+DEVICE IP HERE+''',
    'username': username,
    'password': password,
    'device_type': 'checkpoint_gaia'
}

change = [
    # example below...
    #f"mgmt_cli login -u '''{username}''' -p '''{password}''' > id.txt",
    #'mgmt_cli -s id.txt add network name 192.168.37.0_24 subnet 192.168.37.0 mask-length 24 broadcast allow',
    #'mgmt_cli -s id.txt publish',
    #'mgmt_cli -s id.txt install-policy policy-package "Standard" access true',
    #'mgmt_cli -s id.txt logout'
]
