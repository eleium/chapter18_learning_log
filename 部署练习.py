# 把python web应用程序部署到平台上的步骤：
"""
一，本地的操作：
1，先 pip freeze > requirements.txt ,搜集本应用所需的包，及依赖项。
2,查看这个requirement.txt文件，删除不必要的项目。
3，更改本地跟项目下的主项目的settings.py文件：ALLOWED_HOSTS = ['eleium.pythonanywhere.com','localhost','127.0.0.1']
ALLOWED_HOSTS 列表的作用,它的作用就是一个“白名单”。
Django 只会响应那些在这个列表里出现的主机名（域名/IP）发来的请求。
如果请求头里的 Host 字段不在列表里，Django 会返回 400 Bad Request 错误，这是一种基本的安全防护。
多个域名，就这么写：[域名1，域名2，域名3，‘localhost','127.0.0.1']
前面的域名让人可以在任何地方访问。如果输入localhost.127.0.0.1,就只能访问本地的这个项目。

重要的一点：DEBUG=False
settings.py 中的DEBUG=False,起到重要的安全作用。
Django 生产环境部署中最重要、最基础的一条安全红线了。

把 DEBUG 设为 False，是项目从“开发阶段”迈向“上线阶段”的标志性一步。
DEBUG = True 时，Django 会做什么？
    当 DEBUG = True 时，Django 进入开发模式，它的核心目的是最大化地暴露错误信息以方便你调试：
    显示详细的错误页面：当代码出错时（比如视图函数报错、模板语法错误、数据库连接失败），
    浏览器会显示一个包含完整调用栈、本地变量值、请求信息、甚至部分代码片段的彩色页面。这对开发者定位问题极有帮助。
    自动提供静态文件服务：在开发环境中，Django 会自动处理你通过 STATIC_URL 引用的 CSS、JS 等静态文件，
    你无需配置 Nginx 或 Apache 等 Web 服务器。
    关闭某些缓存机制：模板文件和数据库查询的缓存会被禁用或简化，确保你对代码的修改能立即在页面上看到效果，便于快速迭代。
    允许显示敏感配置：错误页面可能会显示 SECRET_KEY、数据库密码等敏感信息的环境变量或设置值。

安全实践：如何正确处理？
开发时：在本地电脑上，DEBUG = True 完全没问题，它是你的得力助手。
部署时：在 PythonAnywhere 或其他线上服务器上，强制使用 DEBUG = False。

使用环境变量（专业做法）：不要直接在 settings.py 里硬写 DEBUG = False，而是通过读取环境变量来控制：
在settings.py的开头就要引入环境变量：
import os
# 从环境变量中读取 DEBUG 值，默认为 False
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
在本地电脑设置环境变量 DEBUG=True，在线上服务器不设置（或设置为 False），这样同一份代码在不同环境自动切换。

# settings.py
import os
from pathlib import Path

# 从环境变量中读取 DEBUG 值，默认为 False
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# ... 后续其他配置

此时，因为设置了操作系统的环境变量，原来的setting.py中的代码： DEBUG=True,或False必须删除。
只是最后这个“删除旧行”的细节需要落实。
添加os.debug.get(debug,false)=true,并删除原来的debug=true后，你可以放心地把 settings.py 提交到 Git，
因为敏感配置（DEBUG 值）已经不再写在代码里了。

4，设置.gitignore文件，把不需要的文件忽略推送到github

5，配置静态文件的目录static_root
在项目的根目录下，运行python manage.py collectstatic,会自动在根目录下生成一个staticfiles文件夹.
文件的路径是settings.py 中规定的： static_root = base_dir / 'staticfiles'.
目的是让服务器平台找到项目应用程序文件的静态文件，css样式，image图片，js文件。
：就是那些“不需要 Python 处理”，直接由浏览器下载并使用的文件。
具体来说，就是这三类：
类型	                示例	                              作用
样式表	               .css 文件	                         控制网页的布局、颜色、字体等外观
JavaScript	           .js 文件	                             控制网页的交互行为（点击、动画、表单验证等）
图片/图标	           .png, .jpg, .ico, .svg	             网站的标志、背景图、小图标等

这个static文件夹不是必须的。不是每个 app 都需要静态文件。
如果开发的网站，所含的上面这些静态元素都可以通过cdn，网络下载得到，就没必要自己手动创建learning_logs/static文件夹
除非 有自己的个性静态元素： 自己的图片啊，自己的样式啊等等，就必须创建static，因为服务器不知道去哪里寻找下载。
CDN 全称：
Content Delivery Network（内容分发网络）。
浏览器根据你页面中 {% bootstrap_css %} 生成的 <link> 标签，直接向 Bootstrap CDN 服务器发起请求下载 CSS 文件。
交给谁：CDN 服务器直接把文件交给用户的浏览器，整个过程完全不经过你的 Django 服务器或 PythonAnywhere 平台

本项目为啥有这个文件夹？因为当时为了达到书上 图20-1效果，调试，要绕过cdn模式，手动创建的。


二，上面的步骤完成后，把所有项目文件一并推送到github的response中，等待注册域名后，克隆文件。

1，进入域名
2，克隆文件。进入bash界面，： bash clone https://github.com/eleium/chapter18_learning_log, 将仓库clone到服务器平台上。
3，bash--> cd chapter18_learning_log  -->创建并激活虚拟环境： python -m venv my_venv/my_venv/bin/activate
    注意，激活的路径是bin/,而不是本地的Scripts/
4,在虚拟环境下，安装依赖： pip install -r requirements.txt  根据requirements.txt中的文件，安装。
5，收集静态文件： python manage.py collectstatic ,自动建立一个staticfiles文件夹
    如果没有额外的个性化的static，自己的图片，样式，js指令等，这一步不需要，让浏览器直接从CND上下载默认的static即可。？？？？
    关于你的疑问：这一步是必要的，因为它会将Django admin等内置应用所需的CSS/JS文件集中到staticfiles文件夹，以便生产环境提供。

6，迁徙数据库： python manage.py migrate   这一步的目的是啥?
 这一步的目的是创建数据库表。
 它将你项目中的模型（Models）结构同步到SQLite数据库中，是让网站数据持久化的关键一步。
 必须先运行此命令，网站才能正常读写数据。

7,创建超级用户： python manage.py createsuperuser 

三，退出bash,回到仪表盘，进入web配置
1. 回到 PythonAnywhere 仪表板，点击 **Web** 页面
2. 点击 **Add a new web app**，选择 **Manual Configuration**，手动配置。Python 版本选你本地用的版本（如 3.12）
3. 在 **Code** 部分：
   - **Source code**：`/home/eleium/chapter18_learning_log`
   - **Virtualenv**：`/home/eleium/chapter18_learning_log/myvenv`
4. 编辑 **WSGI configuration file**，配置 Django 入口
    WSGI： Web Server Gateway Interface，即 Web 服务器网关接口，是Python和web之间的翻译官，桥梁

5. 在 **Static files** 部分添加 `/static/` → `/home/eleium/chapter18_learning_log/staticfiles`
    Django 的“放手”策略：当你把 DEBUG = False 后，Django 出于安全和性能的考虑，彻底不再处理任何静态文件请求。
    它把这个任务完全交给了外部的 Web 服务器。
    PythonAnywhere 的 Web 服务器（如 Nginx）不认识 Django 项目结构，不知道要去哪个文件夹找 admin/css/base.css 或 learning_logs/style.css。
    此时在 Web 面板中添加的这个配置，就是给 Web 服务器的一张精确“地图”：
    URL 起点：当用户请求任何以 /static/ 开头的 URL 时（比如 http://eleium.pythonanywhere.com/static/admin/css/base.css），
    物理路径：请直接去服务器的这个文件夹里找文件：/home/eleium/chapter18_learning_log/staticfiles/。
    与上面的python manage.py collectstatic 呼应。

6. 点击 **Reload** 启动网站

今天把一个 Django 应用从本地代码，一路部署到公网可访问的 PythonAnywhere 上，这个过程涉及了：

环节	                 掌握的核心技能
环境准备	             requirements.txt  管理依赖，理解 pip freeze
服务器配置	             虚拟环境、WSGI 入口、静态文件映射
Django 生产模式	         DEBUG=False、ALLOWED_HOSTS、collectstatic
平台操作	             Git 克隆、Bash 命令、Web 面板配置

"""
