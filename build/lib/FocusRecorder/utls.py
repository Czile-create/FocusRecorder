import os, json, sqlite3, prettytable
class sqlServer:
    def __init__(self):
        if not os.path.isdir(os.path.join(os.environ['HOMEPATH'], 'FocusRecorder')):
            os.mkdir(os.path.join(os.environ['HOMEPATH'], 'FocusRecorder'))
        self.config = {
            'version': 1,
            'datafile': os.path.join(os.environ['HOMEPATH'], 'FocusRecorder', 'focus.db'),
            'default': {
                'user': '',
                'numberLimit': {
                    'today': 9999,
                    '24h': 9999,
                    'thisWeek': 9999
                },
                'timeLimit': {
                    'today': 600,
                    '24h': 600,
                    'thisWeek': 1800
                },
                'show': {
                    'today': True,
                    '24h': True,
                    'thisWeek': True
                }
            },
            'tags': {
                'user': '',
                'numberLimit': {
                    'today': 9999,
                    '24h': 9999,
                    'thisWeek': 9999
                },
                'timeLimit': {
                    'today': 600,
                    '24h': 600,
                    'thisWeek': 1800
                },
                'show': {
                    'today': True,
                    '24h': True,
                    'thisWeek': True
                }
            },
            'manager': {
                'autoErase': False,
                'remainData': 30*24*3600,
                'notice': False
            }
        }
        if not os.path.isfile(os.path.join(os.environ['HOMEPATH'], 'FocusRecorder', 'config.json')):
            with open(os.path.join(os.environ['HOMEPATH'], 'FocusRecorder', 'config.json'), 'w') as f:
                f.write(json.dumps(self.config, ensure_ascii=False, indent=4))
        else:
            config = json.loads(open(os.path.join(os.environ['HOMEPATH'], 'FocusRecorder', 'config.json')).read())
            self.config.update(config)

        self.conn = sqlite3.connect(self.config['datafile'])
        self.run('''
            create table if not exists focus
            (
                time int primary key,
                user char(20) not null,
                name char(100) not null,
                title char(100) not null
            );
        ''')
        self.run('''
            create table if not exists tags
            (
                title   char(100) primary key,
                user    char(20)  not null,
                tag     char(100) not null
            )
        ''')
        
    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def run(self, sql):
        result = self.conn.cursor()
        result.execute(sql)
        return result

class printServer:
    def print(cursor):
        table = prettytable.from_db_cursor(cursor)
        table.align = 'l'
        if 'Time' in table.align.keys(): table.align['Time'] = 'r'
        table.set_style(prettytable.DOUBLE_BORDER)
        print(table)

class noticeServer:
    pass