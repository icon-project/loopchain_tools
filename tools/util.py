"""Common util functions"""
import os
import time
from sys import platform

import loopchain


def close_open_python_process():
    # ubuntu patch
    if platform == "darwin":
        os.system("pkill -f python")
        os.system("pkill -f Python")
    else:
        os.system("pgrep -f python | tail -$((`pgrep -f python | wc -l` - 1)) | xargs kill -9")


def clean_up_temp_db_files(kill_process=True):
    from pathlib import Path
    loopchain_root = Path(os.path.dirname(loopchain.__file__)).parent

    if kill_process:
        close_open_python_process()

    print(f"loopchain root : {loopchain_root}")

    os.system(f'rm -rf $(find {loopchain_root} -name db_*)')
    os.system(f'rm -rf $(find {loopchain_root} -name *test_db*)')
    os.system(f'rm -rf $(find {loopchain_root} -name *_block)')
    os.system(f"rm -rf {loopchain_root}/testcase/db_*")
    os.system(f"rm -rf {loopchain_root}/.storage")
    time.sleep(1)


def clean_up_mq():
    os.system("rabbitmqctl stop_app")
    os.system("rabbitmqctl reset")
    os.system("rabbitmqctl start_app")
