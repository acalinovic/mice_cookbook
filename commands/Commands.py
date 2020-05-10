import os
import subprocess


def Open():
    result = os.system('ls -lai')
    print(result)
    return 'command open invoked, ' + str(result)


def New():
    process = subprocess.Popen(['ping', '-c 4', 'python.org'],
                               stdout=subprocess.PIPE,
                               universal_newlines=True)
    message = ''
    while True:
        output = process.stdout.readline()
        print(output.strip())
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            # Process has finished, read rest of the output
            for output in process.stdout.readlines():
                print(output.strip())
                message = message + '\n' + output.strip()
            break

    return 'command new invoked' + '::' + message


def Save():
    return 'command save invoked'


def execute(command: str):
    if command == 'open':
        return Open()
    elif command == 'new':
        return New()
    elif command == 'save':
        return Save()

