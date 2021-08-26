#!/usr/bin/python
# Version 1.0
import sys,os, subprocess
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import argparse
import shutil
import glob

#Backup arguments
parser = argparse.ArgumentParser()
parser.add_argument('--host', action='store', dest='pg_host',help='database server host')
parser.add_argument('--port', action='store', dest='pg_port',help='database server port number')
parser.add_argument('--W', action='store',dest='pg_pass',help='database password')
parser.add_argument('--fp', action='store',dest='fp',help='directory where your backup files is located')
parser.add_argument('--dbname', action='store',dest='pg_dbname',help='database name')
parser.add_argument('--jobs', action='store',dest='jobs',help='parallel jobs to restore')
args = parser.parse_args()

tocfilestr = args.fp + '\manifest.txt'
os.environ["PGPASSWORD"] = args.pg_pass

if args.pg_port is None:
    args.pg_port = '5432'
else:
    print("Arguments parsed for port")

if args.jobs is None:
    args.jobs =  '4'     
else:
    print("Arguments parsed for jobs")   

    
# 1. Create DB
conn = psycopg2.connect(user="postgres", password=args.pg_pass, host=args.pg_host, port=args.pg_port)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()
cur.execute ("CREATE DATABASE" + ' ' + args.pg_dbname)

# 2.Create Manifest

path = os.chdir(r'C:\Program Files\PostgreSQL\9.5\bin')
results =os.system('pg_restore.exe -h ' + str(args.pg_host) + ' -p ' + args.pg_port + ' -U postgres --list ' +  args.fp + ' >> ' + tocfilestr )
print(results)
cur.close()
conn.close()

#3.Create Manifest.txttoc and Manifest.txtmv
try:
    #tocfilestr = sys.argv[1]
    tocfile = open(tocfilestr,"r")
except:
    tocfile =  ''  

try:
    matfilestr = tocfilestr+'mv'
    matfile = open(matfilestr,"w")
except:
    matfilestr =  ''  

try:
    ntocfilestr = tocfilestr+'toc'
    ntocfile = open(ntocfilestr,"w")
except:
    tocfile =  ''
print(tocfilestr)

for line in tocfile: 
    if 'MATERIALIZED VIEW' in line:
        matfile.write( line )
    else:
        ntocfile.write( line)
matfile.close()
ntocfile.close()

#4. Restore TOC
path = os.chdir(r'C:\Program Files\PostgreSQL\9.5\bin')
restore = os.system('pg_restore.exe -h ' + str(args.pg_host) + ' -p ' + str(args.pg_port) + ' --no-owner --use-list=' + ntocfilestr + ' --dbname ' + args.pg_dbname + '  --username postgres --format directory --jobs ' + args.jobs + ' --disable-triggers --verbose'  + ' ' + args.fp)
cur.close()
conn.close()

#5. Restore MV
path = os.chdir(r'C:\Program Files\PostgreSQL\9.5\bin')
os.system('pg_restore.exe -h ' + str(args.pg_host) + ' -p ' + str(args.pg_port) + ' -U postgres --no-owner --use-list=' + matfilestr + ' --dbname ' + args.pg_dbname + ' --format directory --jobs ' + args.jobs + ' --disable-triggers --verbose' +  ' '  + args.fp )
cur.close()
conn.close()
