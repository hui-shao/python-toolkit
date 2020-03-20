# 拖放复制/剪切（文件修改时间)
用于接收拖放的文件，并将其移动到当前目录下以 “文件修改时间” 命名的文件夹下

### 使用方式

+ **拖放文件到 main.exe 上即可（支持多文件）**

<br>

+ 也可以使用命令行参数:

  `-o True/False`　或 　`--overwrite=True/False`　　　　用于选择是否覆盖已经存在的文件，默认跳过

  `-f [DIR]`　　　或　　`--filename=[DIR]`　　　　　　用于指定文件，支持多文件。传入文件时，路径外部用{}包裹，{}外部建议加上引号。例如：

  ```cmd
  python main.py -f "{D:\test1.txt}{D:\test2.txt}" -o True
  ```
