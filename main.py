import subprocess
import re

server_ip = '10.0.2.10'


def client(ip):
    try:
        command = subprocess.Popen(["iperf", "-c", ip, "-u"], 
stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = command.communicate()

        return stdout.decode(), stderr.decode()

    except Exception as e:
        return None, str(e)


def parser(stdout):
    interval_pattern = re.compile(
        
r'\[\s*\d+]\s+(\d+\.\d+-\d+\.\d+|\d+\.\d+-\d+\.\d+\s+sec)\s+(\d+\.\d+\s+[KM]Bytes)\s+(\d+\.\d+\s+[KM]bits/sec)')
    matches = interval_pattern.findall(stdout)

    results = []
    for match in matches:
        interval, transfer, bitrate = match
        result = {
            'Interval': interval.strip(),
            'Transfer': transfer.strip(),
            'Bitrate': bitrate.strip()
        }
        results.append(result)

        return results


output, error = client(server_ip)

if name == 'main' and error:
    print(error)
else:
    print("We are connected to iperf server!")
    result_list = parser(output)
    for value in result_list:
        print(value)
    print("Success!!!")
