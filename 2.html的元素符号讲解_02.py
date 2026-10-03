"""
HTML 的元素（标签）很多，但常用的就那么几十个。我按**用途**分类整理，方便你记忆。

### 一、文档结构类

| 标签                  | 作用                                 | 示例 |
| `<!DOCTYPE html>`     | 声明文档类型                         | 放在文件第一行 |
| `<html>`              | 整个 HTML 文档的根                   | `<html>...</html>` |
| `<head>`              | 文档头部（元信息）                   | `<head>...</head>` |
| `<title>`             | 页面标题（浏览器标签）               | `<title>我的网站</title>` |
| `<body>`              | 页面主体（显示内容）                 | `<body>...</body>` |
| `<meta>`              | 元信息（编码、视口）                 | `<meta charset="UTF-8">` |

### 二、文本内容类

| 标签 | 作用 | 示例 |
| `<h1>`~`<h6>`           | 标题（1 最大，6 最小）          | `<h1>主标题</h1>` |
| `<p>`                   | 段落                            | `<p>这是一段文字</p>` |
| `<br>`                  | 换行（单标签）                  | `第一行<br>第二行` |
| `<hr>`                  | 水平分割线                      | `<hr>` |
| `<strong>`              | 加粗（强调）                    | `<strong>重要</strong>` |
| `<em>`                  | 斜体（强调）                    | `<em>强调</em>` |
| `<span>`                | 行内容器（小块）                | `<span>几个字</span>` |
| `<div>`                 | 块级容器（大块）                | `<div>一整块</div>` |


### 三、列表类

| 标签                | 作用                    | 示例 |
| `<ul>`              | 无序列表（圆点）        | `<ul><li>项目</li></ul>` |
| `<ol>`              | 有序列表（数字）        | `<ol><li>第一步</li></ol>` |
| `<li>`              | 列表项                  | `<li>列表项</li>` |
| `<dl>`              | 定义列表                | `<dl><dt>术语</dt><dd>解释</dd></dl>` |

## 四、链接与媒体类

| 标签                | 作用                  | 示例 |
| `<a>`               | 超链接                | `<a href="/">首页</a>` |
| `<img>`             | 图片                  | `<img src="a.jpg" alt="图">` |
| `<video>`           | 视频                  | `<video src="a.mp4"></video>` |
| `<audio>`           | 音频                  | `<audio src="a.mp3"></audio>` |

### 五、表格类

| 标签                           | 作用                | 示例 |
| `<table>`                      | 表格                | `<table>...</table>` |
| `<tr>`                         | 表格行              | `<tr>...</tr>` |
| `<td>`                         | 表格单元格          | `<td>数据</td>` |
| `<th>`                         | 表头单元格          | `<th>标题</th>` |

---

### 六、表单类

| 标签                              | 作用                        | 示例 |
| `<form>`                          | 表单                        | `<form>...</form>` |
| `<input>`                         | 输入框                      | `<input type="text">` |
| `<textarea>`                      | 多行文本域                  | `<textarea></textarea>` |
| `<button>`                        | 按钮                        | `<button>提交</button>` |
| `<select>`                        | 下拉菜单                    | `<select><option>选项</option></select>` |
| `<label>`                         | 表单标签                    | `<label>姓名</label>` |

---

### 七、语义化容器类（HTML5）

| 标签 | 作用 | 示例 |
| `<header>`                 | 页头                 | `<header>...</header>` |
| `<footer>`                 | 页脚                 | `<footer>...</footer>` |
| `<nav>`                    | 导航栏               | `<nav>...</nav>` |
| `<main>`                   | 主内容区             | `<main>...</main>` |
| `<section>`                | 区块                 | `<section>...</section>` |
| `<article>`                | 文章                 | `<article>...</article>` |
| `<aside>`                  | 侧边栏               | `<aside>...</aside>` |

---

### 八、注释

| 写法                           | 作用 |
| `<!-- 注释内容 -->`            | HTML 注释，浏览器不显示 |

**注意**：Django 模板中，注释里不要写 `{{ }}` 或 `{% %}`，否则会被 Django 解析。
要写 Django 注释，用 `{# #}` 或 `{% comment %}`。

### 九、Django 模板专用

| 标签                         | 作用                   | 示例 |
| `{{ 变量 }}`                 | 输出变量值             | `{{ topic.text }}` |
| `{% 标签 %}`                 | 执行逻辑               | `{% for %}...{% endfor %}` |
| `{# 注释 #}`                 | Django 注释            | `{# 这是注释 #}` |
| `{% comment %}`              | 多行注释               | `{% comment %}...{% endcomment %}` |


### 十、最常用的十个（必记）

| 标签 | 作用 |
|------|------|
| `<div>`                     | 块级容器 |
| `<p>`                       | 段落 |
| `<a>`                       | 链接 |
| `<ul>` + `<li>`             | 无序列表 |
| `<form>`                    | 表单 |
| `<input>`                   | 输入框 |
| `<button>`                  | 按钮 |
| `<img>`                     | 图片 |
| `<h1>`                      | 标题 |
| `<span>`                    | 行内容器 |


### 总结

| 类别 | 常用标签 |
| **结构**              | `<html>`、`<head>`、`<body>`、`<title>` |
| **文本**              | `<h1>`~`<h6>`、`<p>`、`<br>`、`<strong>`、`<em>`、`<span>`、`<div>` |
| **列表**              | `<ul>`、`<ol>`、`<li>` |
| **链接媒体**          | `<a>`、`<img>`、`<video>`、`<audio>` |
| **表格**              | `<table>`、`<tr>`、`<td>`、`<th>` |
| **表单**              | `<form>`、`<input>`、`<textarea>`、`<button>`、`<select>`、`<label>` |
| **语义**              | `<header>`、`<footer>`、`<nav>`、`<main>`、`<section>`、`<article>` |
| **注释**              | `<!-- -->` |
| **Django**            | `{{ }}`、`{% %}`、`{# #}`、`{% comment %}` |

**一句话**：HTML 元素按用途分几大类，最常用的是 `<div>`、`<p>`、`<a>`、`<ul>`、`<li>`、`<form>`、`<input>`。
Django 模板在此基础上增加了 `{{ }}` 和 `{% %}` 两种语法。

---------------------------------------------------------------------------------------------------------------------------



 **Django 模板标签** 和 **HTML 属性**，我按类别整理一下。

### 一、Django 模板标签（`{% %}` 里的关键字）
| 标签           | 作用                    | 示例 |
| `block`        | 定义占位符块            | `{% block content %}{% endblock %}` |
| `endblock`     | 结束块                  | `{% endblock content %}` |
| `extends`      | 继承母版                | `{% extends "base.html" %}` |
| `include`      | 引入其他模板            | `{% include "header.html" %}` |
| `for`          | 循环                    | `{% for topic in topics %}...{% endfor %}` |
| `endfor`       | 结束循环                | `{% endfor %}` |
| `empty`        | 循环为空时执行          | `{% empty %}...` |
| `if`           | 条件判断                | `{% if user.is_authenticated %}...{% endif %}` |
| `endif`        | 结束条件                | `{% endif %}` |
| `else`         | 否则                    | `{% else %}` |
| `elif`         | 否则如果                | `{% elif x > 0 %}` |
| `url`          | 反向解析 URL            | `{% url 'learning_logs:index' %}` |
| `csrf_token`   | CSRF 安全令牌           | `{% csrf_token %}` |
| `load`         | 加载标签库              | `{% load django_bootstrap5 %}` |
| `static`       | 引用静态文件            | `{% static 'style.css' %}` |
| `comment`      | 多行注释                | `{% comment %}...{% endcomment %}` |
| `endcomment`   | 结束注释                | `{% endcomment %}` |
| `block content` | 定义内容块             | `{% block content %}{% endblock content %}` |



### 二、Django 模板变量（`{{ }}` 里的内容）

| 写法                              | 作用                      | 示例 |
| `{{ topic.text }}`                | 输出对象的属性            | 显示主题文本 |
| `{{ topic.id }}`                  | 输出对象的 id             | 用于 URL 传参 |
| `{{ user.username }}`             | 输出当前用户名            | 导航栏显示 |
| `{{ form.as_div }}`               | 渲染表单为 div            | 表单页面 |
| `{{ form.as_p }}`                 | 渲染表单为 p              | 表单页面 |
| `{{ form.as_table }}`             | 渲染表单为 table          | 表单页面 |

---

### 三、HTML 属性（写在标签里的关键字）

| 属性                        | 作用                      | 示例 |
| `href`                      | 链接目标地址              | `<a href="/">首页</a>` |
| `src`                       | 资源地址（图片、视频）    | `<img src="a.jpg">` |
| `alt`                       | 图片替代文字              | `<img src="a.jpg" alt="图">` |
| `id`                        | 元素唯一标识              | `<div id="main">` |
| `class`                     | 元素类名（CSS 用）        | `<p class="text">` |
| `style`                     | 内联样式                  | `<p style="color:red">` |
| `method`                    | 表单提交方法              | `<form method="post">` |
| `action`                    | 表单提交地址              | `<form action="/submit/">` |
| `type`                      | 输入类型                  | `<input type="text">` |
| `name`                      | 表单字段名                | `<input name="username">` |
| `value`                     | 表单字段值                | `<input value="默认">` |
| `placeholder`               | 占位提示                  | `<input placeholder="请输入">` |
| `required`                  | 必填                      | `<input required>` |
| `maxlength`                 | 最大长度                  | `<input maxlength="200">` |
| `cols`                      | 文本域列数                | `<textarea cols="80">` |
| `rows`                      | 文本域行数                | `<textarea rows="10">` |
| `target`                    | 链接打开方式              | `<a target="_blank">` |



### 四、Django 表单相关关键字

| 关键字 | 作用 | 示例 |
| `model`                   | 关联的模型            | `model = Topic` |
| `fields`                  | 包含的字段            | `fields = ['text']` |
| `exclude`                 | 排除的字段            | `exclude = ['date_added']` |
| `labels`                  | 字段标签              | `labels = {'text': ''}` |
| `widgets`                 | 字段控件              | `widgets = {'text': forms.Textarea()}` |
| `attrs`                   | 控件的 HTML 属性      | `attrs={'cols': 80}` |
| `commit=False`            | 暂不保存              | `form.save(commit=False)` |
| `is_valid()`              | 验证表单              | `if form.is_valid():` |
| `cleaned_data`            | 验证后的数据          | `form.cleaned_data['text']` |



### 五、Django 视图/URL 相关关键字

| 关键字 | 作用 | 示例 |
| `path`                       | 定义路由                    | `path('topics/', views.topics)` |
| `include`                    | 引入子路由                  | `include('learning_logs.urls')` |
| `name`                       | 路由名字                    | `name='index'` |
| `app_name`                   | 命名空间                    | `app_name = 'learning_logs'` |
| `request`                    | 请求对象                    | `def index(request):` |
| `render`                     | 渲染模板                    | `render(request, 'index.html', context)` |
| `redirect`                   | 重定向                      | `redirect('learning_logs:topics')` |
| `context`                    | 上下文数据                  | `context = {'topics': topics}` |
| `get_object_or_404`          | 获取对象或 404              | `get_object_or_404(Topic, id=1)` |



### 六、Django 模型相关关键字

| 关键字                         | 作用                      | 示例 |
| `models.Model`                 | 模型基类                  | `class Topic(models.Model):` |
| `CharField`                    | 字符字段                  | `models.CharField(max_length=200)` |
| `TextField`                    | 文本字段                  | `models.TextField()` |
| `DateTimeField`                | 日期时间字段              | `models.DateTimeField(auto_now_add=True)` |
| `ForeignKey`                   | 外键                      | `models.ForeignKey(Topic, on_delete=models.CASCADE)` |
| `on_delete`                    | 删除行为                  | `on_delete=models.CASCADE` |
| `CASCADE`                      | 级联删除                  | 删除主题时条目也删除 |
| `auto_now_add`                 | 自动添加时间              | 创建时自动记录 |
| `objects`                      | 管理器                    | `Topic.objects.all()` |
| `create`                       | 创建记录                  | `Topic.objects.create(text="足球")` |
| `get`                          | 获取单条                  | `Topic.objects.get(id=1)` |
| `filter`                       | 过滤                      | `Topic.objects.filter(text="足球")` |
| `order_by`                     | 排序                      | `order_by('-date_added')` |
| `all`                          | 获取全部                  | `Topic.objects.all()` |
| `save`                         | 保存                      | `topic.save()` |
| `delete`                       | 删除                      | `topic.delete()` |
| `__str__`                      | 字符串表示                | `return self.text` |
| `class Meta`                   | 模型配置                  | `verbose_name_plural = "条目"` |
| `verbose_name`                 | 单数名称                  | `verbose_name = "条目"` |
| `verbose_name_plural`          | 复数名称                  | `verbose_name_plural = "条目"` |


### 七、Django 反向查询关键字

| 关键字                       | 作用                       | 示例 |
| `_set`                       | 反向关联管理器             | `topic.entry_set.all()` |
| `all()`                      | 获取全部                   | `topic.entry_set.all()` |
| `related_name`               | 自定义反向名               | `ForeignKey(Topic, related_name='entries')` |

---

### 八、最常用的 20 个（必记）

| 关键字 | 类别 | 作用 |
| `block`               | 模板             | 定义占位块 |
| `endblock`            | 模板             | 结束块 |
| `extends`             | 模板             | 继承母版 |
| `include`             | 模板/URL         | 引入 |
| `for` / `endfor`      | 模板             | 循环 |
| `if` / `endif`        | 模板             | 条件 |
| `url`                 | 模板             | 反向解析 |
| `csrf_token`          | 模板             | 安全令牌 |
| `href`                | HTML             | 链接地址 |
| `src`                 | HTML             | 资源地址 |
| `id` / `class`        | HTML             | 标识/类名 |
| `method` / `action`   | HTML             | 表单提交 |
| `path`                | URL              | 定义路由 |
| `name`                | URL              | 路由名 |
| `app_name`            | URL              | 命名空间 |
| `render`              | 视图             | 渲染模板 |
| `redirect`            | 视图             | 重定向 |
| `objects`             | 模型             | 管理器 |
| `ForeignKey`          | 模型             | 外键 |
| `__str__`             | 模型             | 字符串表示 |

---

### 总结

| 类别                            | 常用关键字 |
| **Django 模板标签**             | `block`、`endblock`、`extends`、`include`、`for`、`if`、`url`、`csrf_token`、`load`、`static` |
| **Django 模板变量**             | `{{ topic.text }}`、`{{ form.as_div }}` |
| **HTML 属性**                   | `href`、`src`、`id`、`class`、`method`、`action`、`type`、`name` |
| **Django 表单**                 | `model`、`fields`、`labels`、`widgets`、`attrs`、`commit=False` |
| **Django URL**                  | `path`、`include`、`name`、`app_name` |
| **Django 视图**                 | `request`、`render`、`redirect`、`context` |
| **Django 模型**                 | `models.Model`、`CharField`、`ForeignKey`、`objects`、`__str__`、`class Meta` |

**一句话**：
Django 开发中，
模板用 `{% %}` 和 `{{ }}`，
HTML 用 `href`、`src`、`id`、`class` 等属性，
模型用 `CharField`、`ForeignKey`、`objects` 等，
URL 用 `path`、`name`、`app_name`，
视图用 `render`、`redirect`、`context`。
掌握这些关键字，就能读写大部分 Django 代码。"""