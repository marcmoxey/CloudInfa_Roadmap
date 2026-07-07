import argparse, paramiko, getpass, re, time, datetime

            
parser = argparse.ArgumentParser(prog='Labcheck', description='Check if Beelink is healthy')
parser.add_argument('--host',required=True, type=str, help='IP address of remote server')
parser.add_argument('--user', required=True,  type=str, help='remote username')
parser.add_argument('--port', type=int, default=22, help='SSH port')
parser.add_argument('-p','--password', type=str, help='remote password')
parser.add_argument('-k','--key', default=None, type=str, help='EC2 (key file)')
parser.add_argument('-v','--verbosity', help='increase output verbosity', action='store_true')
args =  parser.parse_args()


try: 
    # Create SHH client 
    ssh = paramiko.SSHClient()
    
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    if args.key:
        # use key file
        # Connect to the remote host
        ssh.connect(
            hostname=args.host,
            port=args.port,
            username=args.user,
            key_filename=args.key,
            look_for_keys=False,
            allow_agent=False,
            )
    else:
            password = getpass.getpass() # gets password value
            ssh.connect(
            hostname=args.host,
            port=args.port,
            username=args.user,
            password=password,
            look_for_keys=False,
            allow_agent=False,
            )
    
    try:
        # Perform operations on the remote host 
        
        # Disk usage
        stdin, stdout, stderr = ssh.exec_command('df -h /')
        disk_usage_output = stdout.read().decode('utf-8')
        disk_usage_pattern = r"\d+%"
        disk_usage_match = re.search(disk_usage_pattern, disk_usage_output)
        disk_usage_result = disk_usage_match.group(0)
        # print(disk_usage_result)
    
        # Memory
        stdin_memory, stdout_memory, stderr_memory = ssh.exec_command('free -m')
        memory_output = stdout_memory.read().decode('utf-8')
        memory_pattern= re.compile(r'^Mem:\s+(\d+)\s+(\d+)', re.MULTILINE )
        memory_match = re.search(memory_pattern, memory_output)
        memory_used = memory_match.group(2)
        # print(memory_used)
        memory_total = memory_match.group(1)
        # print(memory_total)
        memory_current_usage = (int(memory_used) / int(memory_total)) * 100
    
        # Uptime
        stdin_uptime, stdout_uptime, stderr_uptime = ssh.exec_command('uptime -p')
        uptime_output = stdout_uptime.read().decode('utf-8').strip('\n')
        
        timestamp = datetime.datetime.now()
        dt = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        
        result = f'''
        =====================================
        Beelink Health Report
        {dt}
        =====================================
        Host:    {args.host}
        Disk:    {disk_usage_result} used
        Memory:  {memory_used}MB / {memory_total}MB ({memory_current_usage:.2f}% used)
        Uptime:  {uptime_output}
        Status:  All systems normal
        =====================================
        '''
        
        
        
        if int(disk_usage_result[:-1]) > 80:
            print('WARNING - Disk above 80%')
        else:
            print(f"{result}")
    except Exception as err:
        print(f'Error {err}')
        
        
    # Close the connection
    ssh.close()

except paramiko.AuthenticationException as err:
    print(f"Authentication failed. Please verify your credentials. {err}")
except paramiko.ssh_exception.NoValidConnectionsError as err:
    print(f'Beelink is offline: {err}')
except paramiko.ssh_exception.BadHostKeyException as err:
    print(f'Wrong IP address: {err}')
    
    

