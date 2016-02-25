# -*- coding:utf-8 -*-

from generater.MetadataReader import get_table_metadata_list_from_netezza


def except_column():
    return list["TENANT_SK"]


def get_column_from_meta(schema, table):
    list = get_table_metadata_list_from_netezza(schema, table)
    res = ""
    for item in list:
        column = item["column"]
        res = res + column + ","
    return res[:-1]


def get_tenant_lookup(schema, table):  # target table
    list = get_table_metadata_list_from_netezza(schema, table)
    res = ""
    for item in list:
        column = item["column"]
        if column[-5:] == "CD_SK":
            column = column[:-3]
        elif column[-3:] == "_SK" and column not in except_column():
            column = column.replace("SK", "BK")
        res = res + column + ","
    return res[:-1]


def generate(src, tgt):
    pass


if __name__ == '__main__':
    list = get_tenant_lookup('AW', 'PTNT_2_NM')
    print(list)
