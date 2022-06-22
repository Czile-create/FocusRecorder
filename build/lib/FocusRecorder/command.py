from FocusRecorder import utls
import sqlite3
def run():
    print('请注意：您正使用命令模式，所有您所输入的命令，包括对数据库的增、删、查、改，将会无条件地以最高权限执行，并在退出时自动提交。如果您不清楚命令模式的风险，请退出。')
    sqlserver = utls.sqlServer()
    while True:
        temp = input('SQL > ')
        if temp.startswith('exit'): return
        sql = ''
        rownum = 1
        while ';' not in temp:
            sql += (temp + '\n')
            rownum += 1
            temp = input(str(rownum).ljust(6))
        sql += (temp + '\n')
        try:
            utls.printServer.print(sqlserver.run(sql))
        except sqlite3.Error as e:
            print('请检查检查命令错误')
            print(f'Error: {e}')
        except:
            pass