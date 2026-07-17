import subprocess
import datetime
import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def check_host(host):
    """Проверяет доступность хоста, возвращает True/False"""
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "2", host],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result.returncode == 0

def read_hosts(filename):
    """Читает список хостов из файла"""
    try:
        with open(filename, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден")
        sys.exit(1)

def write_log(filename, message):
    """Записывает строку в лог-файл"""
    with open(filename, "a") as log:
        log.write(message + "\n")

def main():
    hosts = read_hosts("hosts.txt")
    log_file = "ping_log.txt"
    
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = f"\n=== Проверка: {now} ==="
    print(header)
    write_log(log_file, header)

    available = 0
    unavailable = 0

    for host in hosts:
        if check_host(host):
            line = f"✓  {host} — доступен"
            available += 1
        else:
            line = f"✗  {host} — недоступен"
            unavailable += 1
        print(line)
        write_log(log_file, line)

    summary = f"Итого: {available} доступны, {unavailable} недоступны"
    print(summary)
    write_log(log_file, summary)

main()

