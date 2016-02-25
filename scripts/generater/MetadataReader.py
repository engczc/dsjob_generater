# -*- coding:utf-8 -*-
from odbc.DBConnector import excute_sql


def get_table_metadata_list_from_netezza(schema, table):
    flag = "0"
    sql = "select ATTNAME,ATTNOTNULL,FORMAT_TYPE,ATTCOLLENG,DESCRIPTION " \
          "from _V_RELATION_COLUMN " \
          "where name = '#table#' and schema='#schema#' " \
          "order by colid"
    sql = sql.replace("#table#", table).replace("#schema#", schema)
    rows = excute_sql(sql)
    list = []
    for row in rows:
        map = dict(column=row.ATTNAME, nullable=row.ATTNOTNULL, type=row.FORMAT_TYPE, length=row.ATTCOLLENG,
                   des=row.DESCRIPTION)
        list.append(map)
        flag = "1"
    if "0" in flag:
        print(schema + "." + table + " not found!")
    return list
