import sqlite3

DATABASE = 'fingerpi.db'

def to_dict(data):
    ret_dict = {}
    pairs = data.split(',')
    for pair in pairs:
        key, value = pair.split(':')
        ret_dict[key] = value
    return ret_dict

def db_insert(fingerprint_id, data):
    conn = sqlite3.connect(DATABASE)
    print 'Database opened successfully'
    conn.execute('''CREATE TABLE IF NOT EXISTS USER_DATA
                (ID             INTEGER PRIMARY KEY  NOT NULL,
                 FINGERPRINT_ID INTEGER              NOT NULL,
                 FIELD_TYPE     TEXT                 NOT NULL,
                 FIELD_VALUE    TEXT                 NOT NULL);''')
    data_dict = to_dict(data)
    for f_type, f_value in data_dict.iteritems():
        command = 'INSERT INTO USER_DATA (FINGERPRINT_ID, FIELD_TYPE, FIELD_VALUE) \
                VALUES (%d, \'%s\', \'%s\')' % (fingerprint_id, f_type, f_value)
        conn.execute(command)
    conn.commit()
    conn.close()
        
        
        

if __name__ == '__main__':
    db_insert(1, 'type1:value1,type2:value2')
        
