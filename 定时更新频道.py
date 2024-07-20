import requests
from bs4 import BeautifulSoup
import subprocess
import threading
import os
import time

url='https://mirror.ghproxy.com/https://raw.githubusercontent.com/asdjkl6/tv/tv/.m3u/%E6%95%B4%E5%A5%97%E7%9B%B4%E6%92%AD%E6%BA%90/%E6%B5%8B%E8%AF%95/kk.txt'
local_filename=r'E:\IPTV\kk.m3u'

file1=r'E:\IPTV\IPTV.m3u'
file2=local_filename

def check_live_url(url, timeout=10):
    def fetch_url():
        try:
            nonlocal result, error
            command = [
                "ffmpeg",
                "-timeout", str(timeout*1000000),  # 超时设置为微秒
                "-i", url,
                "-c", "copy",
                "-f", "null",
                "-"  # 将输出定向到空设备
            ]
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=timeout)
        except subprocess.TimeoutExpired as e:
            error = "Timeout occurred"

    result = None
    error = None

    thread = threading.Thread(target=fetch_url)
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        thread.join()  # 确保线程结束
        return False, "Timeout occurred"

    if error:
        print(f"Error checking URL {url}: {error}")
        return False, error

    if result and "Input/output error" in result.stderr:
        return False, "Stream not accessible"
    elif result and "Connection timed out" in result.stderr:
        return False, "Connection timed out"
    else:
        return True, "Stream is accessible"

def download_file(url, local_filename):
    # 下载文件
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

def extract_quote_character(line):
    start = line.find('"')
    if start != -1:
        end = line.find('"', start + 1)
        if end != -1:
            return line[start + 1:end]
    return None
   
def extract_comma_qian(line):
    try:
        if ',' in line:
            comma_qian = line.split(',', 1)[0].strip()
            return comma_qian.strip()
        else:
            return None
    except IndexError:
        return None
    
def extract_comma_ho(linetwo):
        try:
            if ',' in linetwo:
                comma_ho = linetwo.split(',', 1)[1].strip()
                return comma_ho.strip() + '\n'
            else:
                return None
        except IndexError:
            return None    
        
def compare_and_update_files(file1, file2):
    """
    比较 file1 中每一行与 file2 中每一行的第一个双引号里的字符，
    如果一致则用 file2 文件里第一个逗号后面的字符改写 file1 文件中的下一行字符。

    :param file1: 第一个文件的路径
    :param file2: 第二个文件的路径
    :return: 包含每对行比较结果的列表
    """
    result = []
    lines1 = []
    lines2 = []
    # 读取文件内容
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    best_urls = {}

    # 遍历列表并提取每个字符串中第一个引号内的内容
    for i, item in enumerate(lines1):
        quote_char1 = extract_quote_character(item)
        if quote_char1 is not None:
            for j, line2 in enumerate(lines2):
                quote_char2 = extract_comma_qian(line2)
                quote_char3 = extract_comma_ho(line2)
                if quote_char2 is not None:
                    # 比较引号里的字符
                    comparison_result1 = (quote_char1 == quote_char2)
                    result.append((i, j, comparison_result1))

                    # 调试输出
                    print(f"Comparing File1 Line {i+1} ('{quote_char1}') with File2 Line {j+1} ('{quote_char2}'): {comparison_result1}")

                    if comparison_result1:
                        # 检查直播链接速度
                        is_online, speed = check_live_url(quote_char3)
                        if is_online:
                            # 如果当前链接速度更快或还没有记录
                            if quote_char1 not in best_urls or best_urls[quote_char1][1] > speed:
                                best_urls[quote_char1] = (quote_char3, speed)
                            print(f"Checked URL speed: {speed}s for {quote_char3}")
                        else:
                            print(f"已失效直播链接: {quote_char3}")

    # 更新 file1 内容
    for i, item in enumerate(lines1):
        quote_char1 = extract_quote_character(item)
        if quote_char1 in best_urls and (i + 1) < len(lines1):
            lines1[i + 1] = best_urls[quote_char1][0]
            print(f"Updated File1 Line {i+2} with: '{best_urls[quote_char1][0]}'")

    # 将更新后的内容写回 file1
    with open(file1, 'w', encoding='utf-8') as f1:
        f1.writelines(lines1)
        f1.close()  

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

def initialize_git_repo():
    result = run_git_command(['git', 'init'])
    if result.returncode == 0:
        print("Initialized empty Git repository")
    else:
        print(f"Error initializing Git repository: {result.stderr}")

def upload_to_github(file_path, commit_message, repo_url=None):
    try:
        # 获取文件所在目录并切换到该目录
        file_dir = os.path.dirname(file_path)
        os.chdir(file_dir)

        # 检查当前目录是否是Git仓库
        if not os.path.exists('.git'):
            initialize_git_repo()

        # 如果提供了远程仓库地址，则设置远程仓库
        if repo_url:
            set_remote_repo(repo_url)

        # 添加文件到暂存区
        result = run_git_command(['git', 'add', os.path.basename(file_path)])
        if result.returncode != 0:
            return

        # 提交文件到本地仓库
        result = run_git_command(['git', 'commit', '-m', commit_message])
        if result.returncode != 0:
            return

        # 确保推送到main分支
        result = run_git_command(['git', 'branch', '-M', 'main'])
        if result.returncode != 0:
            return

        # 推送提交到远程仓库
        result = run_git_command(['git', 'push', '-u', 'origin', 'main'])
        if result.returncode == 0:
            print(f"Successfully pushed {file_path} to GitHub.")
        else:
            print(f"Error pushing {file_path} to GitHub: {result.stderr}")
    except Exception as e:
        print(f"Error: {e}")
        

commit_message = "一次最新的更新提交"
repo_url = 'git@github.com:zcglc/IPTV.git'
download_file(url, local_filename)
compare_and_update_files(file1, file2)
print('完成')
upload_to_github(file1, commit_message, repo_url)