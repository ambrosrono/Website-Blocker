import time
from datetime import datetime as dt 


# temp hosts
hosts_temp = 'hosts'
# hosts path for linux "you can change hosts path according to your OS"
hosts_path = '/etc/hosts'

# redirect to localhost
redirect = '127.0.0.1'

# websites that you want to block
block_websites = ['www.facebook.com', 'facebook.com'
                  'www.youtube.com', 'youtube.com']


while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working Hours, so blocking website....")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in block_websites:
                if website in content:
                    # means the website is already blocked
                    print("Website is on block mode")
                else:
                    #mapping hostnames to your localhost IP adrress
                    file.write(redirect + " " + website + "\n") 
        
    else:
        print("Fun Hour")
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in block_websites):
                    file.write(line)
            # removing hostnames from host file
            file.truncate()
            
                
    time.sleep(10)