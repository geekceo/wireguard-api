from typing import List
import re

WG_CONFIG_PATH = '/etc/wireguard/wg0.conf'

def get_clients_config() -> List[str]:

    result: List[str] = []

    with open(file=WG_CONFIG_PATH, mode="r") as f:

        result = f.readlines()

    return result

def check_client_status(client_name: str) -> bool:

    config_list: List[str] = get_clients_config()

    result: bool = False

    for index, config_line in enumerate(config_list):

        if client_name in config_line:

            result = True if ''.join(config_list[index + 1])[0] != '#' else False

            break

    return result

def turn_off_client(client_name: str) -> List[str]:

    config_list: List[str] = get_clients_config()

    client_status = check_client_status(client_name)

    if client_status == False:

        return {
            "status": "Error",
            "description": "Client already off"
        }

    for index, config_line in enumerate(config_list):

        if client_name in config_line:

            config_list[index + 1] = f"#{config_list[index + 1]}"
            config_list[index + 2] = f"#{config_list[index + 2]}"
            config_list[index + 3] = f"#{config_list[index + 3]}"
            config_list[index + 4] = f"#{config_list[index + 4]}"

    write_config(config_list)

    return {
        "status": "Ok",
        "description": f"Client {client_name} is off"
    }

def turn_on_client(client_name: str) -> List[str]:

    config_list: List[str] = get_clients_config()

    client_status = check_client_status(client_name)

    if client_status == True:

        return {
            "status": "Error",
            "description": "Client already on"
        }

    for index, config_line in enumerate(config_list):

        if client_name in config_line:

            config_list[index + 1] = config_list[index + 1][1:]
            config_list[index + 2] = config_list[index + 2][1:]
            config_list[index + 3] = config_list[index + 3][1:]
            config_list[index + 4] = config_list[index + 4][1:]

    write_config(config_list)

    return {
        "status": "Ok",
        "description": f"Client {client_name} is on"
    }

def write_config(config_list: List[str]) -> None:

    with open(file=WG_CONFIG_PATH, mode="w") as f:

        f.writelines(config_list)

def get_clients() -> List[str]:

    config_list: List[str] = get_clients_config()

    nicknames = []

    for line in config_list:
        match = re.search(r"#\s*\d+:\s*([A-Za-z0-9_]+)\s*>", line)
        if match:
            nicknames.append(match.group(1))

    return nicknames
