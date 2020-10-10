# INSERT 함수 예제
from flask import render_template

import DBUtil


@test.route('/insert', methods=['GET'])
def insert():
    db_class = DBUtil.Database()
 
    sql = "INSERT INTO testDB.testTable(test) \
                VALUES('%s')" % ('testData')
    db_class.execute(sql)
    db_class.commit()

    return render_template('register.html',
                           result='insert is done!',
                           resultData=None,
                           resultUPDATE=None)


# SELECT 함수 예제
@test.route('/select', methods=['GET'])
def select():
    db_class = DBUtil.Database()

    sql = "SELECT idx, test \
                FROM testDB.testTable"
    row = db_class.executeAll(sql)

    print(row)

    return render_template('find.html',
                           result=None,
                           resultData=row[0],
                           resultUPDATE=None)


# UPDATE 함수 예제
@test.route('/update', methods=['GET'])
def update():
    db_class = DBUtil.Database()

    sql = "UPDATE testDB.testTable \
                SET test='%s' \
                WHERE test='testData'" % ('update_Data')
    db_class.execute(sql)
    db_class.commit()

    sql = "SELECT idx, test \
                FROM testDB.testTable"
    row = db_class.executeAll(sql)

    return render_template('update.html',
                           result=None,
                           resultData=None,
                           resultUPDATE=row[0])
