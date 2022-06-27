# 对初学者的教程

本应用可以帮助记录 Windows 电脑中各项应用的使用情况，为了帮助你快速掌握本应用的各种用法，制定本教程。**本教程大概分为三个部分，一是安装，二是各分区含义与用法，三是常用命令。** 最后还介绍了出现问题的解决方法。

## 开始使用

<u>安装</u>

- 在 [Python 下载界面](https://www.python.org/downloads/) 下载和安装 Python 3，并在安装时勾选 **将 Python 加入 Path**。
- 在 `cmd` 中输入 `pip install FocusRecorder`

这样，我们就安装好了这个应用。接下来我们来尝试调整一些设置

<u>初始化</u>

- 在 `cmd` 中输入 `FocusRecorder --init`
- 输入 `FocusRecorder --setting`

接下来会弹出一个文本编辑器，这里面就是设置内容，你可以在你们调整设置，各项指标的意义如下：

```json
{
    "version": 1,                                   // 第一个版本的设置内容
    "datafile": "\\Users\\Czile\\.focus.db",        // 数据库位置
    "default": {                                    // 不加参数情况下显示的用户数据
        "user": "",                                 // 显示谁的数据，默认是本机
        "numberLimit": {                            // 显示使用最多的前几个应用
            "today": 9999,
            "24h": 9999,
            "thisWeek": 9999
        },
        "timeLimit": {                              // 每个应用使用时间必须达到下面的秒数才会显示
            "today": 600,
            "24h": 600,
            "thisWeek": 1800
        },
        "show": {                                   // 是否显示
            "today": true,
            "24h": true,
            "thisWeek": true
        }
    },
    "tags": {                                       // 加 --tag 的情况下显示的数据
        "user": "",
        "numberLimit": {
            "today": 9999,
            "24h": 9999,
            "thisWeek": 9999
        },
        "timeLimit": {
            "today": 600,
            "24h": 600,
            "thisWeek": 1800
        },
        "show": {
            "today": true,
            "24h": true,
            "thisWeek": true
        }
    },
    "manager": {
        "autoErase": false,                         // 是否需要自动空间管理
        "remainData": 2592000,                      // 如果需要自动空间管理，只保留最近的多少秒产生的数据，默认是三十天
        "notice": false                             // TODO: 出现错误是否弹窗提醒
    }
}
```

## 查看数据

上一步完成后，静候一段时间（以产生数据），我们可以来查看记录的数据了。最简单的查看方法是直接在命令行中输入：
```bash
FocusRecorder
```

当然，它可能显示的数据是空，这是因为数据量不够，无法统计有展示意义的数据。你可能会疑惑，是否电脑真的记录了我的使用情况呢？为了回答这个问题，你可以输入：
```bash
FocusRecorder -s
```
查看记录的数据数量，如果不是0，说明已经有记录了。

