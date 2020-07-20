# 网易云音乐歌词转换工具
用于将网易云下载的lrc歌词转换为标准格式

### 主要特征

- 支持歌词批量处理
- 支持自动转为 UTF-8 
- 支持将3位数时间四舍五入为2位（rounding.py）
- 兼容各大主流系统平台

### 使用效果

Image:

![](https://raw.githubusercontent.com/hui-shao/python-toolkit/master/text-tools/NetEaseCloudMusic-LyricConverter/README1.png)

> 转换前 & 转换后(时间转换并未展示)

### 使用方式

1. 下载并安装python解释器  [官方网站>>>](https://www.python.org/)
2. 下载本项目
3. 在脚本所在目录按要求新建目录，例如“input”，放入lrc歌词文件
4. 在脚本所在目录打开终端，执行相关脚本，例如 `python LrcConverter.py`

#### 另：关于 rounding.py 的说明

- 用于将如下时间格式（三位小数）的歌词四舍五入替换为两位小数

- 要求：输入的歌词文件放置在程序目录下的 input_1 文件夹，换行符为\n

- 支持自动按行寻找匹配），若未发现三位小数则该行不改变，例如：

转换之前：
```text
[ti:]
[00:00.010] 作曲 : papaw泡泡
[00:00.349] 作词 : St
[00:00.23]测试行1
[00:01.049]企划：平安夜的噩梦
```
转换之后：
```text
[ti:]
[00:00.01] 作曲 : papaw泡泡
[00:00.35] 作词 : St
[00:00.23]测试行1
[00:01.05]企划：平安夜的噩梦
```