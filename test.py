import speedtest
import platform
import psutil
import time
import requests


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
def http_latency(url="https://www.google.com"):
    try:
        start = time.time()
        requests.get(url, timeout=2)
        end = time.time()
        return round((end - start) * 1000, 2)  # ms
    except Exception as e:
        return str(e)

def speedTest():
    s = speedtest.Speedtest(secure=True)

    download = s.download()
    upload = s.upload()

    download = format(download/1000000, '.2f')
    upload = format(upload/1000000, '.2f')

    print('Download speed is:', download, 'MB per second')
    print('Upload speed is:', upload, 'MB per second')

    ping_result = http_latency("https://www.google.com")
    print(f"Raw HTTP latency result: {ping_result}")
    if isinstance(ping_result, float):
        ping_time = f"{ping_result:.1f}"
        packet_loss = 0
    else:
        ping_time = None
        packet_loss = 100
    print(f"Raw ping result: {ping_result}")  # Add this line
    # Since ping_host returns either a float (ms) or a string, handle accordingly
    if isinstance(ping_result, float):
        ping_time = f"{ping_result:.1f}"
        packet_loss = 0  # No packet loss if we got a response
    else:
        ping_time = None
        packet_loss = 100  # Assume 100% packet loss if no response

    print(f"Packet Loss: {packet_loss}%")
    print(f"Average Ping: {ping_time if ping_time is not None else 'N/A'} ms")

    return [download, upload, packet_loss, ping_time]

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

