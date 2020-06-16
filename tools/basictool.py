#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""CLI tool for loopchain"""
import inspect
import os
from collections import OrderedDict
from pathlib import Path
from sys import platform

from tools import get_option_from_prompt

from testcase.unittest.test_util import clean_up_temp_db_files, clean_up_mq


class BasicTool:
    def __init__(self):
        self._menu_actions = {}
        self._tools_root = ''
        self._loopchain_root = ''
        self._methods = OrderedDict({
            'Kill All Process': self.kill_process,
            'Clean up ALL (DB/log/pycache/MQ)': self.clean_up_all,
            'Make essential db backup': self.make_essential_db
        })
        self._set_loopchain_root()

    def _set_loopchain_root(self):
        current_path = Path(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
        loopchain_root = current_path.parents[1]    # get two level upper path
        tools_root = current_path.parent

        print(f'loopchain_root : {loopchain_root} \n'
              f'tools_root : {tools_root}')

        self._loopchain_root = loopchain_root
        self._tools_root = tools_root

    def main(self):
        while True:
            print("\n-----------------------------")
            print(" LoopChain Command Line Tool")
            print(" Choose menu number you want")
            print("-----------------------------")
            choice = get_option_from_prompt(self._methods.keys())
            if choice is None:
                return

            method = list(self._methods)[choice]
            self._methods[method]()

    def kill_process(self):
        clean_up_mq()

        if platform == "darwin":
            os.system("pkill -f python")
            os.system("pkill -f Python")
            os.system("pkill -f gunicorn")
        else:
            os.system("pgrep -f python | tail -$((`pgrep -f python | wc -l` - 1)) | xargs kill -9")

        os.system("make check")

    def clean_up_all(self):
        self.kill_process()

        # clean DB
        clean_up_temp_db_files()

        # clean
        os.system("make clean-test && make clean-pyc && "
                  "make clean-log && make clean-db")

        # make proto
        os.system(f"make generate-proto")

    def make_essential_db(self):
        print("make essential db")
