import psycopg2
import base64
import hashlib
import os
import time

base_path = '/home/keens/Desktop'

conn = psycopg2.connect(host='localhost', dbname='test', user='postgres' ,password='' ,port=5433)
cur = conn.cursor()
cur.execute("SELECT value from ir_config_parameter where key = '%s'" % ('ir_attachment.location'))
file_storage = cur.fetchall()[0][0]
print (file_storage)

def generate_hash(fname):
    f_encode = hashlib.sha1(fname.encode())
    sha = f_encode.hexdigest()
    store_name = sha[:2] + '/' + sha
    return store_name

def update_fname(fname, attachment_id):
    cur = conn.cursor()
    cur.execute("UPDATE ir_attachment set store_fname = '%s' where id = %s" %(fname, attachment_id))
    conn.commit()
    print ("Updating filestore in database", fname, attachment_id)

def db_to_filestore():
    cur = conn.cursor()
    cur.execute("SELECT id, name, db_datas, store_fname from ir_attachment WHERE db_datas is not null")
    filename = cur.fetchall()

    for files in filename:
        update_fname(generate_hash(files[1]), files[0])
        if not os.path.exists(os.path.dirname(base_path + files[3])):
            try:
                os.makedirs(os.path.dirname(base_path + files[3]))
                with open(base_path + files[3], 'wb') as f:
                    f.write(base64.b64decode(files[2]))
                    f.close()
            except OSError as msg:
                print (msg)
        print ("Migrating files", files[0])

def insert_binary_datas(file_path, attachment_id):
    f = open(file_path, 'rb')
    contents = f.read()
    #print (contents)
    binary = psycopg2.Binary(base64.b64encode(contents))
    print (attachment_id)
    cur = conn.cursor()
    cur.execute("UPDATE ir_attachment set db_datas = %s where id = %s" %(binary, attachment_id))
    conn.commit()
    print ("Setting Binary data for", attachment_id, '--', file_path)

def filestore_to_db():
    cur = conn.cursor()
    cur.execute("SELECT id, name, store_fname from ir_attachment WHERE store_fname is not null")
    filename = cur.fetchall()

    for fname in filename:
        insert_binary_datas(base_path + fname[2], fname[0])
            
def set_db_storage_mode():
    cur = conn.cursor()
    cur.execute("UPDATE ir_config_parameter set value = 'db' where key = 'ir_attachment.location'")
    conn.commit()

def cleanup_filestore():
    cur = conn.cursor()
    cur.execute("UPDATE ir_attachment set store_fname = null")
    conn.commit()

if (file_storage == 'db'):
    db_to_filestore()
if (file_storage == ''):
    filestore_to_db()
