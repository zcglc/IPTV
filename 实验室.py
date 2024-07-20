import requests
from bs4 import BeautifulSoup
import subprocess
import threading
import time

repo_url = 'git@github.com:zcglc/IPTV.git'

def run_git_command(command):
    result = subprocess.run(command, check=False, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Command {command} failed with return code {result.returncode}")
        print(result.stdout)
        print(result.stderr)
    return result

def set_remote_repo(repo_url):
    # 检查是否已经存在名为 'origin' 的远程仓库
    result = run_git_command(['git', 'remote', 'get-url', 'origin'])
    if result.returncode == 0:
        print("Remote 'origin' already exists, updating URL.")
        result = run_git_command(['git', 'remote', 'set-url', 'origin', repo_url])
    else:
        print("Adding new remote 'origin'.")
        result = run_git_command(['git', 'remote', 'add', 'origin', repo_url])
    
    if result.returncode == 0:
        print(f"Remote repository set to {repo_url}")
    else:
        print(f"Error setting remote repo: {result.stderr}")

set_remote_repo(repo_url)