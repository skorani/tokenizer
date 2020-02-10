import db

reveresd_array = []
lookup_reverse_dic_CODE = {}
lookup_dic_CODE = {}


def init():
    db.connect()


def release():
    db.close()

def create_dic_code():
    global lookup_reverse_dic_CODE
    global lookup_dic_CODE

    cursor = db.cursor(buffered=True)
    cursor.execute("SET NAMES utf8;")  # or utf8 or any other charset you want to handle
    cursor.execute("SET CHARACTER SET utf8;")  # same as above
    cursor.execute("SET character_set_connection=utf8;")


    sql = "SELECT replace_with, phrase  FROM phrase;"
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    reveresd_array = cursor.fetchall()

    for row in reveresd_array:
        replace_with, phrase = row
        # Now print fetched result
        lookup_dic_CODE.update({replace_with: [phrase]})
        lookup_reverse_dic_CODE.update({phrase: [replace_with]})
    cursor.close()
    return


def reverse_replace(_token_):
    global lookup_dic_CODE
    for item in lookup_dic_CODE.items():
        _token_ = str.replace(_token_, item[0], item[1][0])

    return _token_
