## 键鼠工具
### 项目介绍
- 本项目是一个脚本工具库，主要提供功能包括：键鼠、句柄、图像处理、邮件等
- 本项目开发驱动于飞洛印的可视化清洁性检查脚本
- 清洁性检查脚本不开源，编写的一些工具类开源
### 快速使用
- 软件需要安装的依赖
```shell
pip install pyautogui
pip install pywin32
pip install opencv-python 
```
- 文件打包成EXE
```shell
pip install pyinstaller
pyinstaller --onefile hyperchain.pyw
```
- 默认文件夹
```shell
图像匹配的target图像都从这个文件夹下获取
C:\_check\img 

程序的日志和异常截图会存储在这个文件夹下，通过smtp协议发送到开发者邮箱
C:\_check\log 
```
- 脚本开机自启
`
C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup文件夹下创建bat文件
`
### 文件
- Point：坐标类，主要定义了一些坐标相关的计算
- EmailTool：邮箱工具类，可以指定标题和附件列表
- HandleTool：句柄工具类，可以获取句柄，根据句柄控制窗口
- ImageTool：图形工具类，可以打开，存储，异常处理，图像匹配
- KeyBoardTool：键盘工具类，控制键盘输入
- MouseTool：鼠标工具类：鼠标移动，单双击