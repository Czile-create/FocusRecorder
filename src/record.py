import win32process, win32gui, psutil, time, getpass
import pygetwindow as gw
from FocusRecorder import utls
def get_focus():
    try:
        pid = win32process.GetWindowThreadProcessId(
            win32gui.GetForegroundWindow()
        )
        return (
            psutil.Process(pid[-1]).name(), 
            gw.getActiveWindow().title
        )
    except Exception as e:
        print(e)

def run():
    sqlserver = utls.sqlServer()
    if sqlserver.config['manager']['autoErase']:
        sqlserver.run(
            f'''
                delete from focus 
                where       user = '{getpass.getuser()[:20]}'
                and         time < {int(time.time() - sqlserver.config['manager']['remainData'])}
            '''
        )
    focus = get_focus()
    sqlserver.run(
        f'''
            insert into focus values (
                {int(time.time())},
                '{getpass.getuser()[:20]}',
                '{focus[0][:100]}',
                '{focus[1][:100]}'
            )
        '''
    )