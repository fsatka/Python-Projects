# File loader to ftp server

## FTPLoader
Base class for load data to server.
Was tested on "Ubuntu 16.04.LTS"

### Consider:
1. class **Log** for logging errors to **file.log**.
2. user settings for authorization on the server(host, name, password).
3. function **start_load**, which makes connection to the server 
   and set **Queue** of paths.

## Log
class that implements thread-safe write to the **file.log**,
which locates in directory of program

## ParseJson
class that parses the **json** file of the following type:
```json
{
    "path": [
        [
            "/home/roman/Music",
            "/home/roman/ftp",
            "test_in_python.pdf"
        ],
        [
            "/home/roman/Music",
            "/home/roman/ftp2",
            "variants-rk2.pdf"
        ]
    ],
    "user": {
        "host": "192.168.1.21",
        "name": "ivanov",
        "password": "111111"
    }
}
```
