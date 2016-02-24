# -*- coding:utf-8 -*-
import sys, os
import configparser


class config_reader:
    def get_config_by_section(section, path='../../config/db_config.ini'):
        cp = configparser.ConfigParser()
        cp.read(path)
        cp.sections()
        return cp[section]


if __name__ == '__main__':
    f = config_reader.get_config_by_section('netezza_home')
    print(f['IP'])
