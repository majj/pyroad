# -*- coding: utf-8 -*-

import codecs
import cx_Oracle


def main(fn, fn2):
        
    print("start")
    con = cx_Oracle.connect('dbuser/dbpw@ORCL')  # bfcecmes

    print(con.version)

    cur = con.cursor()
    #x = cur.fetchall()

    fw = codecs.open(fn2, "wb", 'utf-8')

    with codecs.open(fn, "rb", 'utf-8') as fh:
        i = 0
        j = 0
        sql = ""
        while True:
            #print(".",end="")
            i = i +1
            x = fh.readline()
            
            if i<3:
                #remove REM and SET line
                continue
            
            ### if i>40:
                ### break
                
            if i % 100 == 0: 
                cur.execute("commit")
            
            if len(x) == 0:
                break
            #print(repr(x))
            sql = sql + x
            if sql[-4:] == ');\r\n':
                #print(sql)
                j = j + 1
                #print("%d." % j)
                try:
                    #print(sql[:-3])
                    v = sql[:-3].replace('\n',"'||chr(10)||'")
                    cur.execute(v)
                    #print(v)
                    #print("done")
                except cx_Oracle.IntegrityError as exi:
                    #print(exi)
                    pass
                
                except Exception as ex:
                    #print(">>", end=":")
                    #print(ex)
                    fw.write(sql[:-3].replace('\n',"'||chr(10)||'")+";\r\n")
                    #print(sql.encode('utf8'))
                    #break
                sql = ""

            #print(">==========================")
            #break
    fw.close()      
    print("done")

if __name__ == "__main__":
    
    fn = "t1.sql"
    fn2 = "t1-1.sql"
    
    main(fn, fn2)
    