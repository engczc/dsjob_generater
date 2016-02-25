# -*- coding:utf-8 -*-
from util.ConfigReader import get_config_by_section
import pyodbc


def get_connect_string_for_netezza():
    config = get_config_by_section()
    str = "DRIVER={NetezzaSQL};SERVER=" + config['IP'] + ";DATABASE=" + config['DB'] + ";UID=" + config[
        'USER'] + ";PWD=" + config['PWD']
    return str


def get_connection():
    conn = pyodbc.connect(get_connect_string_for_netezza())
    return conn


def excute_sql(sql):
    cursor = get_connection().cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows
