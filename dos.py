import time
import os

os.chdir('C:/')

print('Starting PY-DOS...')
time.sleep(3)
print('Loading...')
time.sleep(5)
print('Checking RAM...')
time.sleep(1)
print('OK')
time.sleep(0.25)
print('Checking ROM...')
time.sleep(1)
print('OK')
time.sleep(0.25)
print('Type "help" to get the list of commands')
print('CapySoft 2024')
ver = 'PY-DOS v0.2'
print(ver)

while True:
    cmd1 = input(os.getcwd())
    if cmd1 == 'help':
        print('help: Get the list of commands')
        print('chelp: Get help for chdir')
        print('dosver: Version')
        print('calc: Open calculator')
        print('shutdown: Shutdown the system')
    if cmd1 == 'dosver':
        print(ver)
    if cmd1 == 'calc':
       os.startfile('calc.bat')
    if cmd1 == 'shutdown':
        time.sleep(3)
        quit()
    if cmd1 == 'chdir':
        os.chdir(input('Dir: '))
