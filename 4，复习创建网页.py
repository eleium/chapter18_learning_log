"""
    创建其他的网页，因为上面的内容，已经创建了一个网页：http://localhosts:8000/,内容：index.html:
    <p>Learning Log</p>
    <p>Learning Log helps you keep track of your learning, for any topics you've interested in.</p>
    
   1, 现在需要建立一个base.html ，类似全局设置，把重复的网页元素写进去：
    这个base.html文件，要放到与index.html的相同目录下： learning_logs/templates/learning_logs/:
    base.html:
    <p>
    <a href="{% url 'learning_logs:index' %}">Learning Log</a>
    </p>

    {% block content %}{% endblock content %}
********
部分	                                            含义
<p>...</p>	                                         一个段落，里面可以放文字、链接、图片等
<a>...</a>	                                         一个超链接（anchor）
href="..."	                                         链接的目标地址（点击后跳转到哪里）
{% url 'learning_logs:index' %}	Django               模板标签，动态生成 URL
Learning Log	                                     链接上显示的文字，用户看到并点击的内容


<p>...</p>之间是一个段落，内容可以是图片，超链接，文本
<a> 标签的 href 属性指定跳转地址
<a> 标签之间的文字是用户看到的链接文字
点击后，浏览器会跳转到 href 指定的地址
-------------------------------------------------------------------------------


  <a href="{% url 'learning_logs:index' %}">Learning Log</a>：
  
  `{% url 'learning_logs:index' %}` **不是指向 `index.html` 文件，而是指向一个 URL 路径**，
  这个路径再由 Django 路由到对应的视图，视图再渲染 `index.html`。


### 逐层拆解
<a href="{% url 'learning_logs:index' %}">Learning Log</a>
| 部分                                           | 含义 |
| `{% url 'learning_logs:index' %}`              | Django 模板标签，**根据路由名反向解析出一个 URL 路径** |
| `href="..."`                                   | 把解析出的 URL 路径作为链接目标 |
| `Learning Log`                                 | 链接上显示的文字 |

### 你理解中的偏差

| 你的说法 | 修正 |
|----------|------|
| `{% url %}` 指向 `index.html` 文件          | ❌ 它指向的是一个 **URL 路径**（如 `/`），不是 HTML 文件 |
| 点击链接会出现 `index.html` 的内容          | ⚠️ 不准确，点击后 Django 会**根据 URL 找到视图**，视图再**渲染模板** |

**正确的流程**：
点击链接
  ↓
浏览器访问 {% url %} 解析出的 URL 路径（如 /）
  ↓
Django 根据 URL 找到对应的视图函数
  ↓
视图函数渲染 index.html
  ↓
浏览器显示渲染后的 HTML

### 一个具体例子

假设你的路由配置是：
# learning_logs/urls.py
app_name = 'learning_logs'

urlpatterns = [
    path('', views.index, name='index'),
]

那么 `{% url 'learning_logs:index' %}` 会被解析为 `/`（根路径）。
因为ll_project/urls.py 和learning_logs/urls.py  path("",views.index,name='index')
urlpatterns=[admin/,admin.site.url,path("",include("learning_logs.urls"),)]
两个urls.py 都是："" ,空字符串，对应的就是 " / ".

用户点击链接后：
1. 浏览器请求 `/`
2. Django 匹配到 `learning_logs` 应用的 `index` 视图
3. 视图执行 `render(request, 'learning_logs/index.html')`
4. 浏览器显示 `index.html` 渲染后的内容

### 关键区别

| 概念 | 是什么 | 作用 |
| `{% url %}`                  | 模板标签                 | 根据路由名生成 URL 路径 |
| URL 路径（如 `/`）           | 字符串                   | 告诉浏览器访问哪个地址 |
| 视图函数                     | Python 函数              | 处理请求，决定用哪个模板 |
| 模板（`index.html`）         | HTML 文件                 | 渲染出最终页面 |
### 总结

| 你的理解 | 修正后 |
|----------|--------|
| `{% url %}` 指向 `index.html`                  | ⚠️ 修正：它指向一个 **URL 路径** |
| 点击链接会出现 `index.html` 的内容             | ⚠️ 修正：点击后 Django 找到视图，视图渲染 `index.html` |
| `href` 形成超链接                              | ✅ 正确 |
| 点击后跳转                                     | ✅ 正确，但跳转的是 URL，不是文件 |

**一句话**：`{% url %}` 生成的是 URL 路径，不是文件路径。点击后，Django 根据这个 URL 找到视图，视图再决定渲染哪个模板。


-----------------------------------------------------------------------------------
{% block content %}{% endblock content %}的意义？

{% block content %}{% endblock %} 是啥意思？	定义一个叫 content 的占位符
为啥是“块内容”？	                            因为它是“一块”可被子模板替换的区域
为啥分开放？	                                不分开，它是母版中的占位符，子模板来填
为啥写成一行？                               	因为母版本身不填内容，写成一行简洁
有什么用？	                                   实现模板继承，让子模板复用母版结构
一句话：{% block content %}{% endblock %} 就是在母版上挖了一个坑，子模板可以往这个坑里填自己的内容。
是base.html必须的。

    """