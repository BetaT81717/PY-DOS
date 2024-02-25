import time
import os

print('Starting PY-DOS...')
time.sleep(3)
print('Loading...')
time.sleep(5)
ram1 = '144MB'
rom1 = '1.44GB'
print('RAM' + ram1)
time.sleep(1)
print('OK')
time.sleep(0.25)
print('ROM' + rom1)
time.sleep(1)
print('OK')
time.sleep(0.25)
print('Type "help" to get the list of commands')
print('CapySoft 2024')
ver = 'PY-DOS v0.1'
print(ver)
while True:
    cmd1 = input('C:/>')
    if cmd1 == 'help':
        print('help: get the list of commands')
        print('dosver: version')
        print('calc: open calculator')
        print('shutdown: shutdown the system')
    if cmd1 == 'dosver':
        print(ver)
    if cmd1 == 'calc':
        print('Sorry, but our developer is not that advanced yet, so we ask you to go to the system directory and run the calc.bat file. We promise to make automatic opening in v0.2')
    if cmd1 == 'shutdown':
        quit()