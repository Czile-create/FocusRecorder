import os, json, sqlite3, prettytable

from FocusRecorder.overview import overview
class sqlServer:
    def __init__(self):
        if not os.path.isdir(os.path.join(os.environ['HOMEPATH'], 'FocusRecorder')):
            os.mkdir(os.path.join(os.environ['HOMEPATH'], 'FocusRecorder'))
        self.config = {
            'version': 1,
            'user': '',
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
            },
            'colors': {
                '0': [222, 245, 222],
                '1': [213, 255, 213],
                '2': [162, 255, 162],
                '3': [106, 255, 106],
                '4': [57, 255, 57],
                '5': [97, 222, 97],
                '6': [38, 218, 38],
                '7': [11, 194, 11],
                '8': [10, 169, 10],
                '9': [6, 129, 6],
                'default': [255, 255, 255]
            },
            'overview': True
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