# WireGuard API (for easy-wg-quick)


[![Python 3.10](https://img.shields.io/badge/python-3.10+-green.svg)](https://www.python.org/downloads/release/python-310/)
[![GitHub](https://img.shields.io/badge/WireGuard-red?style=for-the-badge&logo=wireguard&logoColor=white)](https://github.com/geekceo/Tutter)

### Note


This API will be correct to easy-wg-quick installer (link [![easy-wg-quick installer](https://img.shields.io/badge/github-black.svg)](https://github.com/burghardt/easy-wg-quick))


### Tools
| Method | URL Path                     | Body                      | Description                    |
|--------|------------------------------|---------------------------|--------------------------------|
| <span style="color:#C2B02F;">GET </span>   | /api/v2/clients              | None                      | Get all clients                |
| <span style="color:#2E90A6;">PUT </span>    | /api/v2/clients/off          | { client_name: "string" } | Turn off client                |
| <span style="color:#2E90A6;">PUT </span>    | api/v2/clients/on            | { client_name: "string" } | Turn on client                 |
| <span style="color:#C2B02F;">GET </span>    | api/v2/clients/{client_name} | None                      | Get clients status (ON or OFF) |

### Get started

To activate service:
```bash
uvicorn main:app --port 50050
```

To activate background process:
```bash
nohup uvicorn main:app --port 50050 >/dev/null 2>&1 &
```
