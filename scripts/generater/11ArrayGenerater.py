# -*- coding:utf-8 -*-

from odbc.MetadataReader import get_table_metadata_list_from_netezza


def get_seq_from_meta(schema, table):
    list = get_table_metadata_list_from_netezza(schema, table)
    res = ""
    for item in list:
        column = item['column']
        if "JOB_ID" == column or "BTCH_ID" == column:
            continue
        nullable = item['nullable']
        if nullable:
            nullable = ""
        else:
            nullable = "nullable "
        res = res + " " + column + ":" + nullable + "string[max=255];\n"
    return res


def generate(src, tgt):
    pass


if __name__ == '__main__':
    list = get_seq_from_meta('SRC', 'NAME_MASTER')
    print(list)
