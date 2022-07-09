from rich.console import Console
def overview(sqlserver): 
    data = sqlserver.run(
        '''
        with tmp1 as
        (
            select  strftime('%Y-%m-%d', datetime(time, 'unixepoch', 'localtime')) date,
                    title,
                    time - lag(time, 1, 0) over (order by time) time
            from    focus
        ), tmp2 as
        (
            select  round(sum(time)/60/60, 0) time
            from    tmp1
            where   time < 100
            group by    date
            order by    date desc
        )
        select * from tmp2 limit 90
        '''
    )
    data = [row[0] for row in data]
    print('总览')
    console = Console()
    colors = sqlserver.config['colors']
    for i in range(90):
        if i % 30 == 0:
            print('\n\t', end = '')
        if i >= len(data):
            color = colors['default']
            console.print('  ', style = f'white on rgb({color[0]},{color[1]},{color[2]})', end='')
        else:
            color = colors[str(int(data[i]))]
            console.print('  ', style = f'white on rgb({color[0]},{color[1]},{color[2]})', end='')
    print()
    print()