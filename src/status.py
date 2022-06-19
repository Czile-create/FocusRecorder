import prettytable, os, utls
def run():
    sqlserver = utls.sqlServer()
    print(f"数据文件位置：{sqlserver.config['datafile']}")
    print(f"数据文件大小：{round(os.path.getsize(sqlserver.config['datafile'])/1024/1024, 2)} MB")
    print('各用户产生数据量')
    table = prettytable.from_db_cursor(
        sqlserver.run(
            '''
            select  user 用户,
                    count(*) 数据量
            from    focus
            group by user
            '''
        )
    )
    print(table)