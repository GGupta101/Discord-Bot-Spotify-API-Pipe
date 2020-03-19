import subprocess
import json

client_id="eb49f162c72d48e6a53a52b2f183a20e"
client_secret="b450e134564f4316a004f60abafad1c0"
c="ZWI0OWYxNjJjNzJkNDhlNmE1M2E1MmIyZjE4M2EyMGU6YjQ1MGUxMzQ1NjRmNDMxNmEwMDRmNjBhYmFmYWQxYzA="
cmd = "curl -X \"POST\" -H \"Authorization: Basic "+c+"\" -d grant_type=client_credentials https://accounts.spotify.com/api/token"
print(subprocess.check_output(cmd).decode("utf-8"))

auth=(json.loads(subprocess.check_output(cmd).decode("utf-8")))["access_token"]

print(str(auth))