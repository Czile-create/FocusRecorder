import getpass, time, datetime
from FocusRecorder import utls
def widget(sqlserver, start_time, description):
    cursor = sqlserver.run(f'''
        with tmp1 as (
            select  time,
                    ifnull(tag, 'Other') tag,
                    time - lag(time, 1, 0) over (partition by tag order by time) as t
            from    focus
            left join tags on focus.title = tags.title and focus.user = tags.user
            where   focus.user = '{sqlserver.config['tags']['user'] if sqlserver.config['tags']['user'] != '' else getpass.getuser()[:20]}'
        ), tmp2 as (
            select * from tmp1 where t <= 100
        ), tmp3 as (
            select  tag,
                    cast(sum(t)/60 as integer)||'min' Time
            from    tmp2
            where   time >= {start_time}
            group by tag
            having sum(t) >= {sqlserver.config['tags']['timeLimit'][description]}
            order by sum(t) desc
            limit   {sqlserver.config['tags']['numberLimit'][description]}
        )
        select * from tmp3
    ''')
    utls.printServer.print(cursor)

def run(user = ''):
    sqlserver = utls.sqlServer()
    if user != '': sqlserver.config['tags']['user'] = user
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