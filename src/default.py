import utls, getpass, time, datetime
def widget(sqlserver, start_time, description):
    cursor = sqlserver.run(f'''
        with tmp1 as (
            select  time,
                    title Title,
                    name Name,
                    time - lag(time, 1, 0) over (partition by title order by time) as t
            from    focus
            where   user = '{sqlserver.config['default']['user'] if sqlserver.config['default']['user'] != '' else getpass.getuser()[:20]}'
        ), tmp2 as (
            select * from tmp1 where t <= 100
        ), tmp3 as (
            select  title,
                    min(name) name,
                    cast(sum(t)/60 as integer)||'min' Time
            from    tmp2
            where   time >= {start_time}
            group by title
            having sum(t) >= {sqlserver.config['default']['timeLimit'][description]}
            order by sum(t) desc
            limit   {sqlserver.config['default']['numberLimit'][description]}
        )
        select tmp3.title, name, ifnull(tag, 'Other') tag, Time from tmp3
        left join tags on tmp3.title = tags.title
    ''')
    utls.printServer.print(cursor)

def run(user = ''):
    sqlserver = utls.sqlServer()
    if user != '': sqlserver.config['default']['user'] = user
    start_time = int(time.mktime(datetime.date.today().timetuple()))
    if sqlserver.config['default']['show']['today']:
        print('今日内')
        widget(sqlserver, start_time, 'today')
    if sqlserver.config['default']['show']['24h']:
        print('过去24小时')
        widget(sqlserver, time.time() - 24*3600, '24h')
    if sqlserver.config['default']['show']['thisWeek']:
        print('过去一周')
        widget(sqlserver, time.time() - 24*3600*7, 'thisWeek')