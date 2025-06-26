import speedtest
import platform
import psutil
import subprocess
import re

from ping3 import ping
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def ping_host(host):
    # Use 'ping' instead of 'ping.exe' for Linux
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    result = (subprocess.run(command, capture_output=True, text=True))
    return result.stdout

def speedTest():
    s = speedtest.Speedtest(secure=True)

    # Raw results
    raw_download = s.download()
    raw_upload = s.upload()
    print(f"Raw download (bits/sec): {raw_download}")
    print(f"Raw upload (bits/sec): {raw_upload}")

    # Convert to Mbps and MBps
    download_mbps = raw_download / 1_000_000
    upload_mbps = raw_upload / 1_000_000
    download_MBps = download_mbps / 8
    upload_MBps = upload_mbps / 8

    print(f"Download: {download_mbps:.2f} Mbps, {download_MBps:.2f} MB/s")
    print(f"Upload: {upload_mbps:.2f} Mbps, {upload_MBps:.2f} MB/s")

    # Ping test
    count = 4
    lost = 0
    total_ping = 0
    successful_pings = 0
    for _ in range(count):
        result = ping("www.google.com", timeout=2)
        print(f"Ping result (seconds): {result}")
        if result is None:
            lost += 1
        else:
            total_ping += result
            successful_pings += 1
    packet_loss = (lost / count) * 100
    ping_time = f"{(total_ping / successful_pings) * 1000:.1f}" if successful_pings > 0 else None

    print(f"Packet Loss: {packet_loss}%")
    print(f"Average Ping: {ping_time} ms")

    # Return MBps for consistency with your frontend
    return [f"{download_MBps:.2f}", f"{upload_MBps:.2f}", packet_loss, ping_time]    

def getHardware():
    print("="*40, "System Information", "="*40)
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")

    # let's print CPU information
    print("="*40, "CPU Info", "="*40)
    # number of cores
    print("Physical cores:", psutil.cpu_count(logical=False))
    print("Total cores:", psutil.cpu_count(logical=True))
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
    print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
    # CPU usage
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

if __name__ == '__main__':
    speedTest()

