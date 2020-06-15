import os
import subprocess
test = os.popen('ipconfig').read()
#print(test)


test1 = subprocess.run('ipconfig',capture_output=True)
print(test1.args)
print(test1.returncode)
print(test1.stdout.decode())