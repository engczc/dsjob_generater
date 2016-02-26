# -*- coding:utf-8 -*-
import sys, os
import configparser


def get_config_by_section(section='netezza_remote', path='../../config/config.ini'):
    cp = configparser.ConfigParser()
    cp.read(path)
    cp.sections()
    return cp[section]
