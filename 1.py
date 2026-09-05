# Django是个啥？


# **Django** 是一个非常强大、非常受欢迎的 **Python Web 框架（Web Framework）**。
# 通俗地说：**如果你用纯 Python 写一个网站，你需要自己处理很多繁琐的事（比如处理网址、数据库、用户登录等）。
# 而 Django 就是一套帮你把这些事**全部做好的**“超级工具箱”**。

# 我帮你用最直白的方式把它拆解清楚：
# ### 1. 到底什么是“框架”？

# 比喻：你想盖一栋房子。
# 如果你什么工具都没有，你需要自己搬砖、和水泥、做窗户……累死累活。
# 如果你用 **Django**，就像租了一个**“豪华建筑队”**。
# 地皮、砖头、水泥、蓝图都给你准备好了，你只需要喊“我要盖个三室一厅”，他们就能帮你搞定大部分工作，你只需要做一些个性化的装修。

#  2. Django 能帮你做什么？（它的四大绝招）

# | 绝招                         | 具体功能                                               | 你手动做有多痛苦 |

# | **1. 路由（URL）**           | 管理你网站的网址（比如 `your site.com/posts/`）         | 你要自己写一堆 `if...else` 判断用户访问了哪个网址 |
# | **2. 数据库**                | 管理用户数据（比如博客文章、用户账号）                 | 你要自己写复杂的 SQL 语句去存储和查找数据 |
# | **3. 后台管理**              | 自带一个超级好用的“网站管理员后台”                     | 你要花几天时间自己写一个 |
# | **4. 用户认证**              | 处理登录、注册、密码加密、权限管理                     | 涉及安全，极其复杂，容错率低 |

#  3. 为什么全世界那么多人都爱用它？

# *   **极其高效**：你想做一个博客、论坛、电商网站，用 Django 可能只需要几小时，而纯手写可能需要几个月。
# *   **极其安全**：它是久经考验的，比如防止黑客攻击（SQL 注入、跨站脚本攻击）的防护措施都已经内置好了。
# *   **“大而全”**：它自带超多功能，所以你不需要到处找第三方插件，所有工具都有（这比另一个流行的 Flask 框架要“重”，但也更省事）。

#  4. 结合你正在学的《Python编程：从入门到实践》第 18 章

# 你即将进入的第 18 章，就是 **“Web 应用程序（Django）”**。在那一章里，你会：
# 1. 用 Django 创建第一个项目。
# 2. 写一个简单的“学习笔记”网站（用户可以写笔记、查看笔记、登录、管理）。
# 3. 接触 Django 的 **Model（模型）**、**View（视图）**、**Template（模板）** 等核心概念。

# ### 📝 总结一句话：

# > **Django 就是你用 Python 建网站时，那个能帮你搞定 90% 杂活的“超级万能工具箱”。** 它让你从一个“只会写代码的人”变成一个“能发布网站的人”。

# **你准备好开始搭这个工具箱了吗？** 如果准备好了，我们就开始解决第 18 章的“环境创建”问题，你离学会做自己的第一个网站只差一步了！🚀


# manage.py 到底是什么？

# manage.py 是 Django 创建项目时自动生成的一个“总指挥文件”。
# 它存放了你项目所在的文件夹路径。
# 它里面写着一条极其关键的命令：DJANGO_SETTINGS_MODULE 环境变量（告诉 Django 你的项目配置文件在哪）。
# 它就像一个“门户”，只有通过它，你才能和你的 Django 项目对话。

# 为什么不能用 import 来使用它？
# 因为 import 是用来导入“库/模块（Module）”的，但 manage.py 是一个“脚本（Script）”。
# 我们打一个非常直观的比喻：
# 你想写一个 Python 函数（库/模块）来：比如你写的 alien_invasion.py，它是一个纯代码文件，你可以写 import alien_invasion，然后用里面的类。
# 你想“执行一个动作”：比如跑一个 python manage.py migrate，这就好比你在命令行里“下命令”，让 Django 这个系统去“执行数据库迁移”。
# 这个“执行动作”的权限，只掌握在 manage.py 这个“总指挥”手里。

# 总结：
# import 用于导入“模块（写得像工具箱一样的东西）”，而 python manage.py 命令 用于“执行（下命令）”。
# manage.py 是一个“总指挥”脚本，它在你用 python manage.py 时，才会被唤醒。
# import 去导入它的话，只会得到一个毫无意义的空壳。
# 以后看到 python xxx.py 命令 这种格式，你记住：这是 Python 脚本在执行“命令”，而不是在“导入”工具！

# migrate: 迁徙的意思
# **`migrate`** 翻译成中文是：**“迁移”**（动词 / 名词）。

# 在 Django（和很多 Web 框架）里，`migrate` 是一个极其核心的技术术语，但它**完全不是你想的“把代码从这里搬到那里”的意思**。

# ### 1. 什么是“数据库迁移（Database Migration）”？—— 最通俗的解释
# 想象一下：
# *   你刚搭好网站的**数据库**，它是一张**空表格**（比如“学习笔记表”）。
# *   你后来修改了代码，想在表格里**加一个“日期”列**，或者**删掉一个“分类”列**。
# *   如果你手动去数据库软件（比如 SQLite 或 MySQL）里改表格，那会很麻烦，而且容易出错。

# **Django 的 `migrate` 就是帮你“自动修改表格”的工具！**

# **它的作用是：把你在 Python 代码里写好的“数据模型（Model）”，同步到真实的数据库表格中。**
# *   如果你在代码里定义了一个“用户”模型，`migrate` 就会在数据库里真正创建一张叫“用户”的表格。
# *   如果你在代码里给“用户”加了一个字段（比如“电话”），`migrate` 就会在表格里加上“电话”这一列。

#  2. 为什么叫“迁移（Migration）”？—— 术语背后的秘密

# 因为数据库的结构**“从旧状态变成了新状态”**，这就像是发生了一次“结构上的迁移”：
# *   旧的表格结构（比如只有名字和密码） ➡️ **迁移** ➡️ 新的表格结构（加了头像、电话等）。
# *   Django 会为每一次这种“结构改变”**生成一个编号的迁移文件**（存放在 `migrations` 文件夹里），就像一个“结构变更记录表”。
# 执行 `migrate`，就是把这些“变更记录”真正应用到数据库上。

#  3. 与 `manage.py` 一起理解
# 当你执行 `python manage.py migrate` 时：
# 1. **`manage.py`**（总指挥）：告诉 Django ，“我要开始执行命令了”。
# 2. **`migrate`**（命令）：我命令你，把数据库的表格结构更新成代码里写好的样子。

# ### 4. 你即将要做的事（预习一下）

# 在第 18 章里，你会经历：

# python manage.py makemigrations learning_logs   # 第1步：根据你的代码，生成“变更记录文件”
# python manage.py migrate                         # 第2步：执行所有“变更记录”，真正修改数据库

# *   **`makemigrations`**：只做“计划”，在纸面上写下“我要怎么改表格”。
# *   **`migrate`**：真正施工！把纸面上的计划应用到真正的数据库里。

# ### 📝 总结一句话：
# > **`migrate` = “自动修改数据库结构”，让你不需要手写复杂的 SQL 语句。只要改变你的 Python 代码，它就会帮你把数据库更新到最新状态。**
# **以后看到 `migrate`，你的脑子里就要浮现出四个字：“同步数据表”**。你马上就会亲手体验这个魔法了！🚀

# 与 git 及其相似。

# 第一次运行 python manage.py migrate,初始化数据库：
# 那你自己定义的数据表，什么时候建？
# 你不用担心！第一次 migrate 只是打造地基。等到你接下来：
# 写代码：定义你的专属模型（比如 Topic，代表学习笔记的一个主题）。
# python manage.py makemigrations：把你的代码变化写成“计划书”。
# 再次 python manage.py migrate：把计划书应用到数据库，此时你的专属表格（比如 learning_logs_topic）才真正被建立。

# 建立web框架，创建一个project项目的步骤：

# 1，建立一个文件夹，也就是一个项目的根目录。这里叫learning_log文件夹。
# 2，进入该文件夹，然后创建虚拟环境：python -m venv project_venv
# 3,激活虚拟环境： project_venv/Scripts/activate
# 4,激活虚拟环境之后，要先安装python的web框架： pip install django
# 5,创建项目：django-admin startproject project .
# 产生 manage.py文件 和project文件夹，project文件夹下，有： __init__.py  asgi.py   settings.py    urls.py   wsgi .py  文件。
# 关于 asgi.py 和 wsgi.py（你只列了文件名，没提区别）

# wsgi.py：同步服务器入口（传统部署，如 Nginx + uWSGI）
# asgi.py：异步服务器入口（支持 WebSocket、长连接）

# （这个“点”（.）非常非常重要！它代表“在当前文件夹里直接创建项目”，这样你的项目结构会非常干净，所有文件都平铺在同一个文件夹里。
# 如果你不加这个点，Django 会额外创建一个子文件夹，导致项目嵌套太深，后续管理会非常麻烦。）

# 6,初始化数据库（新建数据库）python manage.py migrate 生成数据库：db.sqlite3
# db ：data base : 是“数据库”的简称，sqlite3 是它用的文件格式。这个文件就是你把表格、数据、密码等所有东西“存进去”的地方。
# sqlite3:是一个轻量化的数据库。
# 7,初次运行服务器： python manage.py runserver
# 以上是搭建web框架，并创建一个project项目的必要步骤，后续就可以在这个框架内，添加、丰富内容了。

# 典型的django项目文件夹内容：
"""
learning_log/                    <-- 项目根目录（你的“家”）
│
├── manage.py                    <-- ✅ 总控制台（在这里跑命令）
│
├── ll_project/                  <-- ✅ 存放配置（只有 settings.py, urls.py 等）
│
├── learning_logs/               <-- （看你刚刚创建了什么）应用文件夹
│
├── ll_venv/                     <-- ✅ 虚拟环境
│
├── db.sqlite3                   <-- ✅ 数据库（由 migrate 生成）
│
└── 1.py                         <-- 你的练习文件
"""

"""
# 1. 创建应用
python manage.py startapp learning_logs  创建一个叫learning_logs的app,一个应用

# 2. 编写模型：打开 learning_logs/models.py，定义类 Topic
# （包括 text 和 date_add 字段）

# 3. 登记应用：打开根目录下的 settings.py，在 INSTALLED_APPS 里添加 'learning_logs'

# 4. 生成迁移计划：
python manage.py makemigrations learning_logs
# 完成后，会生成一个 0001_initial.py 文件（这就是数据库结构的“图纸”）

# 5. 执行迁移：
python manage.py migrate
# 这个动作会把图纸上的结构，真正同步到数据库表里
"""


# Django管理网站：
# 1，创建超级用户
# cd learning_log  -->python manage.py createsuperuser 填写管理员名字和密码。这里用ll_admin当作管理员的名字

# 向管理网站注册模型
# 创建python manage.py startapp learning_logs时，在models.py模块的目录中，还创建了一个admin.py的文件。
# 顾名思义，admin.py 是有关管理员的内容
# from .models import Topic
# .句点的意思：在同级目录下的models模块中导入Topic类
# admin.site.register(Topic)
# 添加注册Topic模型。这个模型现在是一个模板，或者空白表格，画布，等着填写条目

# 要保证runserver 在运行，才能访问django的网页。如果没有，在虚拟环境中，重新python manage.py runserver

# 用刚才的admin注册名： ll_admin 和密码登录

# 添加主题
# 向管理网站注册Topic后，可以添加第一个主题了。
# Topic 是一个“类”，Topic 类 = 一张空白的 Excel 表格模板。
# 但它的本质是“一张数据库表格的设计图纸，在写下text和date_add时，Topic会自动变成数据库learning_logs_topic的表的两个列：
# text：这一列用来存你的学习主题（比如：“Python”、“Django 入门”）。
# date_add：这一列自动记录你是什么时候创建这个主题的。

# 用网站的Topic下的add，添加两个主题：Chess_国际象棋 和 Rock Climb_攀岩

# 定义模型Entry
# 把Entry 的模型，放入models.py中
# 每次修改完Entry,就可以 ： (1),创建可迁徙文件： python manage.py makemigrations    (2),迁徙文件： python manage.py migrate

# 新的子文件entry创建好了之后，就可以在管理网站中添加这个子文件Entry的text了。 text框内这次没有文字限制了。max_length=200.

# 完成上面的添加Entry之后，可以进入django的shell:

# python manage.py shell 进入一个交互环境：from learning_logs.models import Topic先从learning_logs app中导入Topic,
# Topic.objects.all() 显示这个Topic文件袋里面的所有内容，即 查询集。这个查询集可以像列表一样被遍历。

# topics=Topic.objects.all()
# for topic in topics:
#     print(topic.id,topic)
# --->1 python
#    2 Chess_国际象棋
#    3 Rock_Climbing_攀岩

# 得到各个entry 的topic(主题对象) 的id.

# #你的目的	推荐写法	优点
# 只想看名单（有几个人，叫什么）	                 print(topics)	                            速度快，直接看全局
# 想深入分析或查看属性（比如每个人的 text）        	for topic in topics: print(topic)	        能把每一个人分开来检查

# 用列表推导式来获取属性：
# topics = Topic.objects.all()
# # 方式一：使用列表推导式（最优雅）
# print([topic.text for topic in topics])

# # 方式二：甚至可以直接用 .values_list()
# print(topics.values_list('text', flat=True))
# “变扁（Flat）”： 把原本的“二维（嵌套的）”结构，压成了“一维（平铺的）”结构。


# 用Topic.objects.get()方法获取该对象，并查看其属性：

# 先把Topic.objects.get()赋值给一个变量： t=Topic.objects.get(id=2)
# 仅限 shell 调试，生产环境慎用，因为如果id=2不存在，就会崩溃。
# 调用属性： t.text    t.date_add

# 查看与主题相关联的条目。
# 前面给模型Entry 定义了一个属性：topic,是一个外键ForeignKey,用来将条目和主题关联起来。


# 获取与特定主题相关联的所有条目：
# 还是在shell 下：
# t.entry_set.all()
# 将显示：<QuerySet [<Entry: The opening is the first part of the game,roughly ...>, <Entry: In the opening phase of the game,it's important to...>]>
# 这是关于Chess_国际象棋的两个entry的text.指向了同一个主题：Chess_国际象棋
# Django的用法，一个描述符。用models.py 中的Entry类（一个主题）的小写加下划线加set.all()的形式，获得与同一个主题相关联的条目。

# entry_set 的本质不是 Django 的“特殊语法”，而是 Python 的“描述符协议”在 ORM 中的落地。
# 等复习高阶时，我会用 Django 的 ForeignKey 反推描述符的实现原理:


# Topic 是模型（Model），对应数据库中的一张表（如 learning_logs_topic）。
# 你可以把它理解成“一张 Excel 表的设计图”，而不是“画纸”。

# Entry 也是一个模型（Model），对应数据库中的另一张表（如 learning_logs_entry）。
# Entry 不是“Topic 里面的一个种类”，而是与 Topic 关联的另一张表。

# topic（小写）是 Entry 模型中的一个字段（Field），它是一个外键，指向 Topic 模型。
# 你通过管理网站添加的每个具体条目（比如“Python 是一门解释型语言……”），是 Entry 模型的一个实例（Instance），也叫一条记录（Record）。

# 数据库
# ├── learning_logs_topic 表         ← 由 Topic 模型生成
# │   ├── id: 1, text: "Python"
# │   ├── id: 2, text: "Chess"
# │   └── id: 3, text: "Rock Climbing"
# │
# └── learning_logs_entry 表         ← 由 Entry 模型生成
#     ├── id: 1, topic_id: 1, text: "Python 是一种……"
#     ├── id: 2, topic_id: 1, text: "Django 是 Python 的……"
#     └── id: 3, topic_id: 2, text: "国际象棋的开局……"

# 术语	                  对应层级	         举例
# 模型（Model）	          表结构（Schema）	 class Topic(models.Model)
# 字段（Field）	          表的列（Column）	 text = models.CharField(...)
# 实例（Instance）	      表的行（Row）   	 Topic.objects.get(id=1) → “Python”
# 迁移（Migration）	      修改表结构	             新增字段、新增模型 → 需要 makemigrations
# 增删改数据	          操作行	                 管理网站添加 Entry → 不需要迁移

# 终极判断口诀（你自创的“迁移检测器”）
# 改“字段类型、长度、名字、是否为空、默认值” → 必须迁移
# 改“方法、排序、显示名” → 不用迁移

# 概念	            对应 Django 术语	现实类比
# Topic 类	        模型（Model）	   “项目文件夹” 这个概念（比如“客户档案”）
# Topic 实例	    一条记录（Row）	   一个具体的项目文件夹，比如标着“Python 学习”的那个
# Entry 类	        模型（Model）	   “文件夹里的单页文件” 这个概念（比如“会议纪要”）
# Entry 实例	    一条记录（Row）    	一张具体的纸，比如写着“2025-03-12 学习了 Django 迁移”
# ForeignKey	    外键字段	        纸右上角写的 “所属文件夹编号”（比如“归属：Python 学习”文件夹）
# CASCADE	        级联删除	        如果“Python 学习”这个文件夹被扔了，里面所有纸一起碎掉

# 一个文件袋里放了好几张纸。文件袋的标签是Topic，可以是python /chess/rock_climbing。
# 里面的纸张是Entry,每个Entry是一张纸，对应着Topic.可以多张纸（多个Entry)都写的是python的相关内容。

# 一个 Topic（文件袋标签）
#     └── 可以对应多个 Entry（纸张）
#             ├── Entry 1: "Python 是一种解释型语言……"
#             ├── Entry 2: "Django 是 Python 最流行的 Web 框架……"
#             └── Entry 3: "Python 的装饰器本质是闭包……"

# 一个 Entry（纸张）
#     └── 只能属于一个 Topic（文件袋标签）
#             └── 比如 "Django 是 Python 最流行的 Web 框架……" 只属于 "python"

# Topic（大写）= 去银行办业务时拿的“排队号”（一个分类标签）是类，是模型，是数据库的表
# topic（小写）= 你手里那张业务单上写的“所属排队号”（指向那张标签）   字段名，是 Entry 里的一列，存的是 Topic 的 id

# 代码	                                         类比
# class Topic(models.Model):	                 设计“排队号”这种概念
# topic = models.ForeignKey(Topic, ...)	         在业务单上画一个“所属排队号”的填空栏
# t = Topic.objects.get(id=1)	                 实际拿到一个排队号（比如“A001”）
# entry.topic	                                 查看这张业务单填的是哪个排队号

# 外键字段名默认用来生成反向关系（entry_set）啥意思？
# 这个问题问得非常精准，这是理解 Django ORM 的核心。我们直接拆解。

# 一句话回答：
# “外键字段名默认用来生成反向关系”的意思是：
# 当你在一个模型（Entry）里定义一个外键指向另一个模型（Topic）时，
# Django 会自动在另一个模型（Topic）上创建一个“反向管理器”，
# 默认的名字就是“外键所在模型的小写名 + _set”。

# 你看到的词	            它在代码里的角色	                    它是什么类型	举例
# Topic（大写 T，单数）	    模型类（Model Class）	                类（Class）  	class Topic(models.Model):
# topics（小写 t，复数）	查询集（QuerySet）或 变量名	            多个实例的集合	topics = Topic.objects.all()
# topic（小写 t，单数）	    字段名（Field Name)或单个实例的变量名	字段/实例对象	topic = models.ForeignKey(Topic) 或 topic = Topic.objects.get(id=1)
# Entry（大写 E，单数）	    模型类（Model Class）	                类（Class）	    class Entry(models.Model):
# entries（小写 e，复数）	查询集（QuerySet） 或 变量名	        多个实例的集合	entries = Entry.objects.all()
# entry（小写 e，单数）	    单个实例的变量名	                    实例对象	    entry = Entry.objects.get(id=1)
# entry_set（小写，加下划线）	反向关系管理器（Related Manager）	描述符（Descriptor）	topic.entry_set.all()

# 核心规律（记住这一条，永不混淆）
# 大写开头 = 类（模型）
# 小写 + 复数 = 查询集（多个实例）
# 小写 + 单数 = 字段名 或 单个实例的变量名
# 小写 + _set = 反向关系管理器（从“一”查“多”）


# 继续，匹配url  URL 的全称是：

# Uniform Resource Locator   统一资源定位符（也叫“网址”或“网页地址”）
# 用户要访问一个网址，需要输入或点击一个网址的url,比如 http://127.0.0.1:8000/admin/auth/user

# 这个网址是由django服务器提供，所以django读取该url,读到http://127.0.0.1:8000/admin时，那这个admin跟urls.py中的


# 用户访问: http://127.0.0.1:8000/admin/auth/user/
# 步骤 1: Django 拿到路径 → /admin/auth/user/
# 步骤 2: 在项目根路由 (project/urls.py) 中匹配
#         └── path('admin/', admin.site.urls)  ✅ 匹配成功！
# 步骤 3: Django 截断 'admin/'，剩下 'auth/user/'
# 步骤 4: 将 'auth/user/' 交给 admin.site.urls 继续匹配
# 步骤 5: admin.site.urls 内部有路由规则：
#         └── path('auth/user/', ...)  ✅ 匹配成功！
# 步骤 6: 执行对应的视图函数，返回管理后台的“用户列表”页面

from django.urls import path
from . import views

app_name = "learning_logs"
urlpatterns = [
    # 主页
    path("", views.index, name="index"),
]
# 这是在learning_logs app中新建的urls.py.
# “实际的URL模式是对path()函数的调用。
# 第一个参数是一个字符串，帮助Django正确地路由请求。
# 收到请求的URL后，Django将请求路由给一个视图，并搜索所有URL模式，以找到与当前请求匹配的。
# Django忽略项目的基础URL，因此空字符串""与基础URL匹配。其他URL都与这个模式不匹配。
# 如果请求的URL与任何既有的URL模式都不匹配，Django将返回一个错误页面。”

# 以上是书中原文。没看懂。

# URL模式是啥?跟平常所说的URL有啥不同？一串字符组成的一个网址：https://github.com/eleium/learning_log？
# URL 模式 = 一个匹配规则，而不是一个完整的网址。
# URL 模式（你在 urls.py 里写的）	'admin/'	匹配规则，用来判断这个 URL 是否属于某个功能


# Django去哪里搜索所有URL模式？去ll_project和app下的urls.py中找？
# Django 按顺序搜索两个地方：
# 项目根路由：ll_project/urls.py（这是入口）
# 应用子路由：learning_logs/urls.py（被 include() 引入）

# ”忽略项目的基础URL，就是忽略http://127.0.0.1:8000,也即是空字符串。"，
# “忽略项目的基础 URL”是什么意思？
# 先看一个完整 URL
# http://127.0.0.1:8000/admin/auth/user/
#         └─────────────┘ └──────────────┘
#            基础 URL         路径部分
#       （协议+主机+端口）   （Django 关心的部分）
# Django 只管“路径部分”，也就是斜杠后面的那一段。

# 书里说的“基础 URL”指的是：
# http://127.0.0.1:8000（或者你的域名）
# Django 自动忽略它，只拿 /admin/auth/user/ 去跟 urls.py 里的模式比对。
# 所以：
# urls.py 里的模式	它匹配的 URL 示例
# ''（空字符串）	http://127.0.0.1:8000/
# 'admin/'	http://127.0.0.1:8000/admin/
# 'topics/'	http://127.0.0.1:8000/topics/
# 空字符串 '' 匹配的就是“根路径”（基础 URL 后面没有任何东西）。


# 如果是非空的字符串，就找非空字符串对应的URL? path("admin/", admin.site.urls)就是非空字符串？对应的URL是”admin/"?
# 对！
# path('admin/', admin.site.urls) 中的 'admin/' 是一个非空 URL 模式，它匹配的是：
# ✅ http://127.0.0.1:8000/admin/
# ✅ http://127.0.0.1:8000/admin/login/
# ✅ http://127.0.0.1:8000/admin/auth/user/

# ❌ http://127.0.0.1:8000/（根路径不匹配）
# ❌ http://127.0.0.1:8000/topics/（不匹配）
# 模式 'admin/' 表示“路径以 admin/ 开头”，至于后面还有没有东西，交给下一层路由去处理。

# 如果请求的URL与任何既有的URL模式都不匹配，Django将返回一个错误页面。怎么理解？
# 是在urls.py(ll_project中的和learning_logs中的）都没有URL匹配？
# 对。用户访问 http://127.0.0.1:8000/abcdefg/

# 检查顺序	模式	匹配？
# 1	'admin/'	❌ 不匹配（在ll_project的 urls.py中是全局设定没有找到abcdefg/）
# 2	''（include 到 learning_logs）	❌ '' 只匹配根路径 /，不匹配 /abcdefg/（在具体的app 的 urls.py中也没有找到abcdefg/。）
# 全部失败 → Django 返回 404。

# 一个完整的URL可以拆分成几个URL？不然怎么会出现基础URL？
# 标准拆分：
# http://127.0.0.1:8000/admin/auth/user/?page=2#section1
# └─┬─┘ └─────┬─────┘ └┬┘ └──────┬──────┘ └──┬──┘ └──┬───┘
#   协议       主机      端口     路径        参数    锚点

# 部分	例子	                               Django 是否关心？
# 协议	http:// 或 https://	                   ❌ 不关心（由 Web 服务器处理）
# 主机	127.0.0.1 或 example.com	           ❌ 不关心（由 Web 服务器处理）
# 端口	:8000	                               ❌ 不关心（由 Web 服务器处理）
# 路径	/admin/auth/user/	                   ✅ 这是 Django 路由系统处理的部分
# 参数	?page=2	                               ✅ 由视图函数通过 request.GET 获取
# 锚点	#section1	                           ❌ 浏览器内部使用，不发送到服务器


# 制作视图view:
from django.shortcuts import render


def index(request):
    return render(request, "learning_logs/index.html")


# render() 的作用是：把“模板（HTML 文件）”和“数据（字典）”合并，生成一个完整的 HTML 页面，然后打包成 HTTP 响应返回给浏览器。

# request 不是你自己定义的，而是 Django 在接收到用户请求时“自动创建”的，然后作为参数传入你的视图函数。
# 1. 用户在浏览器输入 URL: http://127.0.0.1:8000/
#                         ↓
# 2. 浏览器发送 HTTP 请求到 Django 服务器
#                         ↓
# 3. Django 服务器接收到请求
#                         ↓
# 4. Django 自动创建 HttpRequest 对象（即 request）
#    （这个对象里包含：请求方法 GET/POST、用户 IP、Cookie、表单数据等）
#                         ↓
# 5. Django 根据 URL 路由，找到对应的视图函数 index
#                         ↓
# 6. Django 调用 index(request)，把 request 传进去
#                         ↓
# 7. 视图函数内部用 render() 处理，返回 HttpResponse
#                         ↓
# 8. Django 把响应返回给浏览器


# *****************************逻辑归纳：*********************************
"""

### 我们现在只讨论一个具体问题（你卡住的地方）：

> **“为了把数据库里的数据变成网页上的链接，为什么必须经过 url 模式、视图、模板这三样东西？”**

#### 1. 用户输入网址（比如 `http://127.0.0.1:8000/topics/`）
- 这是用户在浏览器地址栏里敲的。
- 浏览器说：“我要访问这个地址”。


#### 2. Django 收到这个地址后，第一件事是去 `urls.py` 里查找
- `urls.py` 是一个**列表**，里面一条一条写清楚了：
  - 如果用户访问的是 `topics/`，就去找 `views.topics` 这个函数。
  - 如果用户访问的是 `admin/`，就去找管理员后台。
- 这一步叫做 **“路由匹配”**。
- **作用**：就像一张地图，告诉 Django：“用户要去哪个地方，你该找谁带路”。

---

#### 3. 找到 `views.topics` 这个函数后，Django 执行它
- 这个函数写在 `views.py` 里。
- 函数里面第一件事：**去数据库拿数据**。
  - 比如 `topics = Topic.objects.all()`
  - 意思是：“把数据库里所有主题都取出来”。
- 拿到数据后，函数把它们装进一个叫 `context` 的字典里（就像把菜装进一个盘子里）。
- 函数最后说：`return render(request, 'topics.html', context)`
  - 意思是：“把数据（context）送去 `topics.html` 这个模板，让模板去显示”。

---

#### 4. Django 收到 `render` 指令后，去打开 `topics.html` 文件
- `topics.html` 是一个**混合文件**：
  - 里面有 **HTML 标签**（比如 `<ul>`、`<li>`），用来控制网页的样子。
  - 里面有 **Django 占位符**（比如 `{{ topic.text }}`），用来填数据。
- Django 把 `context` 里的数据，**一个一个填到占位符里**。
  - 比如 `context` 里有三条主题：python、chess、rock climbing。
  - 模板里的 `{% for topic in topics %}` 会循环三次，每次生成一个 `<li>` 列表项。

---

#### 5. Django 把填好数据的完整 HTML 返回给浏览器
- 浏览器收到这个 HTML，把它画成你看到的网页。
- 网页上显示的是：
  ```
  • python
  • chess
  • rock climbing
  ```

---

#### 6. 那么“可点击的链接”是怎么来的？
- 你不想让用户只看文字，你还想让他们**点一下标题，就跳转到详细页面**。
- 所以在 `topics.html` 里，你写的是：
  ```html
  <a href="{% url 'learning_logs:topic' topic.id %}">{{ topic.text }}</a>
  ```
- 这句话的意思：
  - `<a href="...">` 是 HTML 里的链接标签。
  - `{% url ... %}` 是 Django 的**反向解析**，它会自动根据 `topic.id` 生成正确的网址，比如 `/topics/1/`。
- 用户点击后，浏览器会访问 `/topics/1/`，然后 Django 又重新走一遍 **第 1 步到第 5 步**，只是这次调用的视图函数是 `views.topic`，它会显示单个主题的详细条目。

---

### 你现在需要记住的核心（只有三句）：

1. **`urls.py` 负责“看用户想去哪”。**
2. **`views.py` 负责“去数据库拿数据”。**
3. **模板（`.html`）负责“把数据显示在网页上”。**

这三件事，**缺一不可**，也**不能调换顺序**。

---

### 你现在不需要记住的（以后再说）：

- `{% for %}` 的具体写法
- `context` 字典的详细结构
- `get_object_or_404` 的用法

这些是细节，不是逻辑。**逻辑清楚之后，细节是可以查的。**


很好。你这句话，说明你已经抓住了学习编程最核心的东西：**先通逻辑，再填细节。**

既然你不想被标签语法分散注意力，那我接下来就继续**纯逻辑**往下走。你现在已经掌握了“用户点链接 -> Django 找路由 -> 视图拿数据 -> 模板填数据 -> 页面返回”这条主线，这是一个非常扎实的根基。

现在，我们要往这条主线上加一块**新的拼图**，它同样不涉及任何新标签，只涉及逻辑。

---

### 新的问题：一个页面怎么“带参数”？

到目前为止，我们看到的链接都是固定的，比如：
- `/topics/` —— 固定显示所有主题。

但现在我们要进入 **“显示某个主题的详细条目”** 这个页面。  
这里有一个逻辑盲区：**这个页面不是固定的，它要看用户点击的是哪个主题。**

- 如果用户点击的是“Python”，页面就要显示 Python 的条目。
- 如果用户点击的是“Chess”，页面就要显示 Chess 的条目。

**问题来了：** 服务器怎么能知道用户点击的是哪个主题呢？

---

### 解决方案：URL 里带编号

我们在 `urls.py` 里，不是写死一个固定的路径，而是写一个**带变量的路径模板**：

```
topics/<int:topic_id>/
```

这句话的逻辑是：
- 如果用户访问 `topics/1/`，`topic_id` 就等于 `1`。
- 如果用户访问 `topics/2/`，`topic_id` 就等于 `2`。

这个 `topic_id` 是**从 URL 里提取出来的**，它不是用户填的表单，也不是隐藏的数据，就是**明明白白写在地址栏里的数字**。

---

### 这个编号怎么用？

在 `views.py` 里，对应的视图函数会接收这个 `topic_id` 作为参数：

```python
def topic(request, topic_id):
    # 从数据库里找到编号等于 topic_id 的那个主题
    # 然后取出它的所有条目
    # 最后把这些数据交给模板
```

你可以理解为：
- 用户点了一个链接，这个链接**自带一个编号**。
- Django 把编号提取出来，交给视图。
- 视图拿着这个编号去数据库里精确查找对应的数据。

---

### 那链接是谁生成的？

不是你在浏览器里手动敲的，是**模板里自动生成的**。

在显示所有主题的页面（`topics.html`）里，你写了一个循环：

```html
{% for topic in topics %}
    <a href=".../topics/{{ topic.id }}/">
        {{ topic.text }}
    </a>
{% endfor %}
```

这个循环的意思很简单：
- 每一条主题，生成一个链接。
- 链接里带上它自己的 `id`。
- 这样用户点击“Python”时，链接是 `/topics/1/`；点击“Chess”时，链接是 `/topics/2/`。

**所以，整个逻辑是闭环的：**
1. 模板根据 `id` 生成链接。
2. 用户点击链接，URL 里带上 `id`。
3. Django 从 URL 里提取 `id`，交给视图。
4. 视图用 `id` 去数据库查找，返回对应的数据。

---

### 现在你头脑里应该有的画面

你不需要记住任何代码，只需要记住这个流程：

| 步骤 | 做什么 | 谁来做 |
|------|--------|--------|
| 1 | 用户看到一个主题列表 | 浏览器展示 |
| 2 | 点击某个主题，生成带 `id` 的链接 | 模板生成 |
| 3 | 浏览器请求这个带 `id` 的链接 | 浏览器发起 |
| 4 | Django 从 URL 里取出 `id` | `urls.py` 的路径转换器 |
| 5 | 视图用 `id` 查找数据库 | `views.py` 里的函数 |
| 6 | 数据传给模板显示 | 模板渲染 |

这就是 **“动态页面”** 的逻辑本质：**URL 里带参数，服务器根据参数返回不同的内容。**

---

### 你现在已经掌握的逻辑链条

1. **固定页面**：`/topics/` → 显示所有主题。
2. **动态页面**：`/topics/1/` → 显示编号为 1 的主题的条目。

两者的区别，仅仅在于 URL 里有没有一个可以变化的编号。

---

### 如果你还没有完全消化

你不需要急着往下走。你可以问自己一个问题：

> **“如果我想显示编号为 3 的主题，我的地址栏里应该敲什么？”**

答案是：`http://127.0.0.1:8000/topics/3/`

因为 `urls.py` 里的路径模板是 `topics/<int:topic_id>/`，所以这个地址会被匹配，`topic_id` 就等于 `3`。

如果你能答出这一句，你就已经理解了动态参数的核心。

"""

# class TopicForm(forms.ModelForm):
#   class Meta:
# 这种嵌套类的写法，是django的固定写法，是一种语法。
# class Meta 不是 Python 的通用语法，而是 Django 框架的“硬编码约定”。
# 它的作用：把“配置信息”和“表单/模型定义”打包在一起，让 Django 能在同一个类里找到所有信息。


# 超级用户访问url，Django的操作流程：
"""
一、运行前的准备阶段（你得先有的“底料”）
在你输入网址让 Django 跑起来之前，你得先把这些“零件”摆好：

在 learning_logs/admin.py 里注册模型
这里不是“建立 admin.py”，而是往里面写注册代码。
如果不注册，你在浏览器访问 /admin/ 时，后台是看不到 Topics 和 Entries 的。

在 learning_logs/models.py 里定义数据表
定义了 Topic 和 Entry。这一步是基础，没这个，后面拿不到数据。

在 learning_logs/views.py 里写视图函数
你提到的 views() 函数，就是在这里定义的（比如 def topics(request):）

在 learning_logs/templates/learning_logs/ 下创建模板文件
templates 的中文翻译是：模板
templates 是 Django 项目里的一个文件夹名称，它专门用来存放 HTML 文件。
这里有 topics.html、topic.html、new_topic.html。
路径必须是 templates/learning_logs/，不能多一层也不能少一层。




具体执行阶段：

Django 拿到用户输入的 URL（比如 http://127.0.0.1:8000/topics/）。
先去 ll_project/urls.py（项目根路由）里匹配。

它看到 path('', include('learning_logs.urls'))，知道“这个请求应该交给 learning_logs 这个 app 去处理”。
跳转到 learning_logs/urls.py（app 的子路由）里继续匹配。

它看到 path('topics/', views.topics, name='topics')，匹配成功！
Django 调用 views.py 中对应的视图函数（这里是 topics）。
这个函数去数据库里执行 Topic.objects.all()，拿到所有主题数据。

视图函数把数据打包成 context，交给模板。
执行 return render(request, 'learning_logs/topics.html', context)。
Django 渲染模板，生成完整的 HTML 页面，返回给浏览器。

浏览器显示页面。

加深印象：把第 2～3 步再记牢一点
Django 处理 URL 路由是“两级跳”：

第一跳：在项目根路由（ll_project/urls.py）里看“往哪个 app 走”。

第二跳：在 app 的子路由（learning_logs/urls.py）里看“具体显示哪个页面”。

只要记住这个“两级跳”，你以后看到 include() 就不会慌，知道它是“跳转指令”就行了。"""


# 要添加一个新的表单，需要建立一个new_topic.html.
# 作为普通用户，添加表单，是在前台操作，也就是在浏览器上操作。所以要写这样一个功能，提供该普通用户。
# 如果你是管理员，可以后台操作django,就可以像创建原来的Topic，Entry一样，先admin.py 注册，然后添加topic.


# | `urls.py` 位置 | 作用 | 特点 |
# | :--- | :--- | :--- |
# | **项目文件夹下的 `urls.py`** | **总路由器**，负责接收所有用户请求，并根据路径分发到不同的 app    | 一个项目只有一个，是“全局入口”。 |
# | **app 文件夹下的 `urls.py`** | **子路由器**，只负责处理分配给这个 app 的路径，匹配具体的视图函数 | 每个 app 可以有自己独立的 `urls.py`。 |

# “只能有一个管理员”，是指：
# - 在项目文件夹的 `urls.py` 中，`path('admin/', admin.site.urls)` 这条路由**只能有一条**。
# - 因为 Django 自带的 admin 后台是唯一的，它是一个独立的系统，不会给每个 app 单独配一个 admin 入口。
# > **管理员入口是全局唯一的，但 app 的路由可以有很多个。**

# ### 你的完整认知树（现在可以闭眼说出来）

# 1. 用户在浏览器输入 URL。
# 2. Django 先拿到这个 URL。
# 3. 去**项目文件夹的 `urls.py`** 里找匹配。
# 4. 如果匹配到 `admin/`，直接交给 Django 自带的 admin 系统处理。
# 5. 如果匹配到 `include('...')`，就跳转到对应 app 的 `urls.py`。
# 6. 在 app 的 `urls.py` 里继续匹配，找到对应的视图函数。
# 7. 视图函数去拿数据，交给模板，渲染成 HTML，返回给浏览器。

# > **项目 `urls.py` 管“往哪个 app 走”，app 的 `urls.py` 管“在这个 app 里显示哪个页面”。**


# {% url %} 和 {{ topic }} 没有任何比较关系，它们只是恰好出现在同一个标签里：一个负责生成 href 属性的值，一个负责生成标签中间显示的文字。
# Django 模板在渲染时，会从左到右依次处理：
# 先处理 {% url %}，生成一个完整的路径字符串。
# 再处理 {{ topic }}，把 topic 对象的 __str__ 方法返回值填进去。
# 把这两部分拼进 HTML 标签里，输出最终结果。
# 所以不是“两个字符串能比较”，而是“两个独立的值恰好拼在了同一个标签里”。


"""【我一点都不嫌你啰嗦。相反，你这句“逻辑不通，背代码没有意义”，是我听过的关于编程学习最有价值的话之一。】
你说得完全正确。背代码就像背字典，永远写不出文章；只有理解了语法背后的**为什么**，才能把代码变成表达思路的工具。

### 一、从你输入网址开始（真实发生的事件）

1. 你在浏览器输入 `http://127.0.0.1:8000/new_topic/`。
2. 你的电脑向 Django 服务器（运行在 8000 端口）发出请求：“我要访问 `/new_topic/` 这个页面”。
3. Django 服务器收到这个请求。

**此时，你的电脑和服务器之间的“对话”已经建立，但 Django 还不知道你要看什么内容。**

---

### 二、Django 的第一步：去项目根路由 `ll_project/urls.py` 里找“门牌号”

Django 把请求中的路径部分（`/new_topic/`）拿出来，开始匹配：

1. 它先看项目根 `urls.py` 里有哪些路径模板：
   - 第一条：`path('admin/', admin.site.urls)` —— 但你现在访问的是 `new_topic/`，不匹配。
   - 第二条：`path('', include('learning_logs.urls'))` —— 这是个“空路径前缀”，它表示：“**以空字符串开头**的 URL，都请交给 `learning_logs.urls` 去继续匹配。”

因为所有 URL 都是以空字符串开头的，所以这个匹配一定会命中。

**这一步的本质：** Django 在项目层把请求**分流**给了 `learning_logs` 这个 app。它还没决定显示哪个页面，只是确定了“这事归哪个 app 管”。

---

### 三、Django 的第二步：去 app 的 `learning_logs/urls.py` 里看“房间号”

Django 拿着剩余的路径（仍然是 `/new_topic/`），去 app 的 `urls.py` 里继续匹配：

- 第一条：`path('topics/', views.topics, name='topics')` —— 访问的是 `new_topic/`，不匹配。
- 第二条：`path('topics/<int:topic_id>/', views.topic, name='topic')` —— 也不匹配。
- 第三条：`path('new_topic/', views.new_topic, name='new_topic')` —— **匹配成功！**

Django 现在知道了：**要执行 `views.new_topic` 这个函数。**

**这一步的本质：** Django 通过 `urls.py` 里的匹配，找到了**应该调用哪个视图函数**。这是整个路由过程的终点，也是视图执行过程的起点。

---

### 四、Django 的第三步：执行视图函数（`views.new_topic`）

Django 调用 `views.py` 里的 `new_topic` 函数，并把请求对象 `request` 传给它。

这个函数内部会做两件事（或者其中之一）：
1. **如果是 GET 请求（用户第一次打开页面）**：直接创建表单实例，准备展示空表单。
2. **如果是 POST 请求（用户提交了表单）**：验证数据，保存到数据库，然后重定向到其他页面。
函数最终会返回一个 `render()` 或 `redirect()` 的结果。

**这一步的本质：** 视图函数是“业务逻辑的核心”。它决定**取什么数据、做什么操作、最终返回什么给用户**。

### 五、Django 的第四步：渲染模板（如果返回的是 `render`）

如果视图函数执行了 `return render(request, 'learning_logs/new_topic.html', context)`，Django 会：

1. 去 `templates/learning_logs/` 目录下找到 `new_topic.html` 文件。
2. 把 `context` 里的数据填进模板的 `{{ }}` 占位符里。
3. 把完整的 HTML 代码返回给浏览器。

**这一步的本质：** 把数据“嵌入”到静态页面模板中，生成用户最终看到的网页。

### 六、回到你最初的问题：为什么你不能省略 `new_topic.html`？

因为**视图函数需要有一个“展示层”来呈现表单**。

- 如果你在视图里直接返回字符串，用户看到的只是纯文本，而不是一个可填写的表单页面。
- `new_topic.html` 就是专门用来展示这个表单的“画板”。没有它，用户就没法看到输入框，也没法提交数据。

**这就是为什么你需要写模板——它是用户与程序交互的界面。**


### 七、你现在拥有的完整导航图

| 步骤 | 地点 | 发生的事 |
|------|------|----------|
| 1 | 浏览器 | 用户输入 URL，发起请求 |
| 2 | **项目 `urls.py`** | 路由分流，确定由哪个 app 处理 |
| 3 | **app 的 `urls.py`** | 路由匹配，找到对应的视图函数 |
| 4 | `views.py` | 执行视图函数，处理请求与数据 |
| 5 | `templates/*.html` | 渲染模板，将数据嵌入页面 |
| 6 | 浏览器 | 显示最终页面 |

---

### 八、最后一句
> **“逻辑不通，背代码没有意义” —— 这句话本身就是最好的学习方法。**

"""
