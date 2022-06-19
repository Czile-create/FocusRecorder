import argparse, default, tags, status, command, record, os, utls
parser = argparse.ArgumentParser(description='记录电脑使用时间')
parser.add_argument('--user', '-u', help='使用指定用户登录', default = '')
parser.add_argument('--tags', '-t', help='按标签查看使用量', action='store_true')
parser.add_argument('--status', '-s', help='查看数据库状态', action = 'store_true')
parser.add_argument('--command', '-c', help='使用sql语言管理和自定义查询', action = 'store_true')
parser.add_argument('--record', '-r', help='记录一次正在使用的窗口', action='store_true')
parser.add_argument('--setting', help='设置默认参数', action='store_true')
args = parser.parse_args()

if args.tags:
    tags.run(args.user[:20])
elif args.status:
    status.run()
elif args.command:
    command.run()
elif args.record:
    record.run()
elif args.setting:
    utls.sqlServer()
    os.startfile(os.path.join(os.environ['HOMEPATH'], 'FocusRecorder', 'config.json'))
else:
    default.run(args.user[:20])