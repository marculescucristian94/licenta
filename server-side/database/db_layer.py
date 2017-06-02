import sqlite3

DATABASE = 'rasprint.db'

# obtains the values that are inserted into the database 
def to_dict(data):
    ret_dict = {}
    pairs = data.split('|')
    for pair in pairs:
        key, value = pair.split(':')
        ret_dict[key] = value
    return ret_dict

# inserts or updates data
def db_insert(fingerprint_id, data):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS user_data
                (id          INTEGER PRIMARY KEY  NOT NULL,
                 fp_id       INTEGER              NOT NULL,
                 field_type  TEXT                 NOT NULL,
                 field_value TEXT                 NOT NULL);''')
    data_dict = to_dict(data)
    for f_type, f_value in data_dict.iteritems():
        c.execute('SELECT id FROM user_data WHERE fp_id = %d AND field_type = \'%s\'' % (fingerprint_id, f_type))
        existing = c.fetchall()
        if not existing:
            command = 'INSERT INTO user_data (fp_id, field_type, field_value) \
                VALUES (%d, \'%s\', \'%s\')' % (fingerprint_id, f_type, f_value)
        else:
            command = 'UPDATE user_data SET field_value = \'%s\' WHERE id = %d' % (f_value, existing[0][0])
        c.execute(command)
    conn.commit()
    conn.close()

# selects the relevant data for fingerprint_id
def db_select(fingerprint_id):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT field_type, field_value FROM user_data WHERE fp_id = %d' % (fingerprint_id))
    result = c.fetchall()
    print result
    conn.close()

# wipes all data for fingerprint_id
def db_delete(fingerprint_id):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('DELETE FROM user_data WHERE fp_id = %d' % (fingerprint_id))
    conn.commit()
    conn.close()
        

#if __name__ == '__main__':
#    db_insert(1, 'name:cristian|surname:marculescu')
#    db_select(1)
#    db_delete(1)
        
db_select(169)
