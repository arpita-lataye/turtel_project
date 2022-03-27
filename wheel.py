import subprocess
data = subprocess.check_output(['netsh','wlan','show', 'profiles']).decode('utf-8').split('\n')

profiles=([i.split(":")[i][1:-1]] for i in data  if "All user profile" in i )
for i in profiles:
    results=subprocess.check_output(['netsh','wlan','show','profile',i,'keysclear']).decode('utf-8').split('\n')
    results=[b.split(":")[i][1:-1] for b in results]
    try:
        print_("{:<10} {:<}".format(i,results[0]))
    except IndexError:
        print_("{:<10} {:<}".format(i,""))