#!/usr/bin/env python3

import argparse
from getpass import getpass
import pymysql
import yaml
from difflib import unified_diff
from datetime import datetime
import os


def fetch_db_structure(conn: pymysql.Connection, db_name: str) -> dict:
    """"""
    """"""
    conn.select_db(db_name)
    cur = conn.cursor()
    cur.execute("SHOW TABLES")
    tables = []
    for table in cur.fetchall():
        tables.append(table[0])
    desc = {}
    for table in tables:
        table_desc = {}
        cur.execute("SHOW FULL COLUMNS FROM " + str(table))
        for row in cur.fetchall():
            row_desc = {
                str(row[0]): {
                    'type': str(row[1]),
                    'collation': str(row[2]),
                    'null': str(row[3]),
                    'default': str(row[4]),
                    'extra': str(row[5]),
                    'privileges': str(row[6]),
                    'comment': str(row[7]),
                }
            }
            table_desc.update(row_desc)
        desc.update({table: table_desc})
    return desc


def write_to_file(file_name: str, lines: list) -> bool:
    """"""
    dt = datetime.now()
    with open(dt.strftime("%Y%m%d%H%M%S") + '_' + file_name, 'w') as file:
        for line in lines:
            file.write(line + os.linesep)
    return True


parser = argparse.ArgumentParser(
    description="Diff tool to compare structure of two databases. Currently only MySQL 5.7+ is supported.")
parser.add_argument("-u", "--user", metavar="", default="root", help="Database user name (default: 'root')")
parser.add_argument("-p", "--password", metavar="", help="Database user password")
parser.add_argument("-H", "--host", metavar="", required=True, help="Host of database server")
parser.add_argument("dbname1", help="Name of first database to compare")
parser.add_argument("dbname2", help="Name of second database to compare")
args = parser.parse_args()
if args.password is None:
    args.password = getpass("MySQL user password: ")

db_host = args.host
db_user = args.user
db_passwd = args.password
source_db_name = args.dbname1
target_db_name = args.dbname2

# @todo Read args from .env file

# Read database structures
db_conn = pymysql.connect(host=db_host, user=db_user, passwd=db_passwd, db=source_db_name)
source_desc = fetch_db_structure(db_conn, source_db_name)
target_desc = fetch_db_structure(db_conn, target_db_name)

source_yaml_lines = yaml.dump(source_desc).splitlines()
# write_to_file(source_db_name + '.yaml', source_yaml_lines)

target_yaml_lines = yaml.dump(target_desc).splitlines()
# write_to_file(target_db_name + '.yaml', target_yaml_lines)

from_file = source_db_name + "@" + db_host
to_file = target_db_name + "@" + db_host
diff_lines = unified_diff(
    source_yaml_lines, target_yaml_lines, fromfile=from_file, tofile=to_file, lineterm='')
# write_to_file(source_db_name + ' ' + target_db_name + '.diff', diff_lines)
for line in diff_lines:
    print(line)
