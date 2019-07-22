#! /usr/bin/env python3
import io
import os
from netmiko import ConnectHandler
import changeChanges_cp

un = changeChanges_cp.username
pwd = changeChanges_cp.password
dev = changeChanges_cp.device
session_log = io.BytesIO()

dev.update({'session_log': session_log})

try:
    with ConnectHandler(**dev) as channel:

        for line in changeChanges_cp.change:
            output = channel.send_command_timing(line, delay_factor=2)
            if 'sername' in output:
                output = channel.send_command_timing(un)
            if 'assword' in output:
                output = channel.send_command_timing(pwd)

        session = session_log.getvalue().decode()

except Exception as e:
    print(str(e))

with open('temp.txt', 'w') as f:
    sensitive_words = ["''' -p '''", "password", "Password"]
    f.write(session)
    f.close()

    with open('stdout.txt', 'w') as nf:
        logs = open('temp.txt', 'r+')
        log_lines = logs.readlines()

        for line in log_lines:
            if any(words in line for words in sensitive_words):
                nf.write('-' * 85 + '\n')
                nf.write('REDACTED FOR SECURITY\n')
                nf.write('-' * 85 + '\n')
            else:
                nf.write(line)

        logs.close()

os.remove('temp.txt')
print("Job complete!")