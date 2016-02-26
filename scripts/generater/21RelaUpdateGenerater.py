# -*- coding:utf-8 -*-
from odbc.MetadataReader import get_table_metadata_list_from_netezza

tgt_list = []
src_list = []
sif_column = ""


def tgt_except_column():
    return ['TENANT_SK', 'LOAD_INFO_SK']


def src_except_column():
    return ['RELATIONSHIP_TYPE_CODE', 'SOURCE_CODE', 'TYPE_CODE']


def add_column():
    return ['TENANT_CD', 'SOURCE_CODE', 'JOB_ID', 'BTCH_ID', 'TENANT_SK']


def get_column_from_meta(schema, table):
    global tgt_list
    tgt_list = get_table_metadata_list_from_netezza(schema, table)
    res = ''
    for item in tgt_list:
        column = item['column']
        res = res + column + ','
    return res[:-1]


def get_tenant_lookup(jointable1, jointable2):  # target table
    res = ""
    for item in tgt_list:
        column = item['column'].strip()
        if column in ['LOAD_INFO_SK', 'SRC_CD_SK', 'TENANT_SK']:
            column = ""
        elif column[-5:] == 'CD_SK':
            column = column[:-3]
        elif column[-3:] == '_SK' and column not in tgt_except_column():
            column = column.replace('SK', 'BK')
        if column != "":
            res += column + ","
    for i in add_column():
        res += i + ","
    res += jointable1 + "_SK," + jointable2 + "_SK" + ";"
    return res


def get_sif_column(schema, table):
    global src_list
    global sif_column
    res = ""
    src_list = get_table_metadata_list_from_netezza(schema, table)
    for item in src_list:
        column = item['column']
        if column[-5:] == '_CODE' and column not in src_except_column():
            res += ", A." + column + "\n"
            sif_column = column
    return res


def get_sif_source():
    pass

def generate(src, tgt):
    pass


if __name__ == '__main__':
    get_column_from_meta('AW', 'PTNT_2_NM')
    get_tenant_lookup('PTNT', 'NM')
    get_sif_column('SRC', 'NAME_MASTER')
    # print(src_list)
