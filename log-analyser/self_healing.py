import subprocess

SERVICE="nginx"

def is_active(service):
    result = subprocess.run(['systemctl', 'is_active', service], stdout=subprocess.PIPE)
    return result.stdout.decode().strip() == "active"

if not is_active(SERVICE):
    subprocess.run(['systemctl', 'restart', SERVICE])
    print(f"{SERVICE} restarted")
else:
    print(f"{SERVICE} was running")
  	