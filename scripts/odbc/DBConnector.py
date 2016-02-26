# -*- coding:utf-8 -*-
from util.ConfigReader import get_config_by_section
import pyodbc


def get_connect_string():
    config = get_config_by_section()
    str = "DRIVER={" + config['DRIVER'] + "};SERVER=" + config['IP'] + ";DATABASE=" + config['DB'] + ";UID=" + config[
        'USER'] + ";PWD=" + config['PWD']
    return str


def get_connection_for_netezza():
    conn = pyodbc.connect(get_connect_string())
    return conn


def excute_sql_for_netezza(sql):
    cursor = get_connection_for_netezza().cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows
