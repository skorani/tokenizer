#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import db
import lookup_dic as lk
import token as tok



def main():
 lk.create_dic_code()
 tok.init()

    # 1 to 218

 for step  in range(1,218) :
    offset = 10
    read_cursor = db.cursor()

    write_cursor = db.cursor()
    print("SELECT 'clean_news','idclean_text'  FROM clean_text limit " + str((step - 1) * 100000 - offset)+ ", 10000;")
    read_cursor.execute("SELECT * FROM clean_text limit 10000 offset " + str(step * 10000)+";")
    counter = {}
    for news in read_cursor:
        clean_news = news[1]
            # print(clean_news)
        tokens = tok.tokenize(clean_news)
        for token in tokens:
            if type(token) == list:
                token = token[0]
            if token in counter:
                counter[token] += 1
            else:
                counter[token] = 1
            # print(counter)

            docID = news[0]
            newCounter = {}
            for token, count in counter.items():
                # print(token)
                test = lk.reverse_replace(format(token))
                # print(test)
                newCounter[test] = count
            for newToken,newCount in newCounter.items():
                write_cursor.execute("INSERT INTO Tokened (Token , `count` ,DociD) VALUES (" +"\""+ newToken+"\""+","+str(newCount)+","+str(docID)+")")
                db.commit()
                # print('done!')
            counter = {}
            step += 1
    write_cursor.close()
    read_cursor.close()
    db.close()
if __name__ == "__main__":
    main()