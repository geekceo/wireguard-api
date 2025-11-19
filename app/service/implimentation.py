import os

def restart_wg_daemon():

    os.popen('sudo systemctl restart wg-quick@wg0')