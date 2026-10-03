"""

在本地准备 `requirements.txt` 并推送它，确实是第一步，但不是唯一的一步。
为了确保在 PythonAnywhere 上能一次部署成功，建议你在本地先做好这几件事，可以省去很多后续在远程服务器上调试的麻烦。

### ✅ 在本地需要完成的准备清单
#### 1. 创建并更新 `requirements.txt`（你需要做的）

这个文件是 PythonAnywhere 识别并安装你项目所有依赖的“购物清单”。
**这个文件必须推送到 GitHub**，否则 PythonAnywhere 在克隆代码后，无法知道要安装哪些包。

在本地项目根目录（`manage.py` 所在目录）的终端中运行：
```bash
pip freeze > requirements.txt

**⚠️ 关键检查**：生成后，请打开 `requirements.txt` 文件，确保里面至少包含 `Django`、`django-bootstrap5` 等核心库。
同时，**务必删掉**与部署环境无关的本地工具，比如 `djlint`、`cssbeautifier` 这些代码格式化工具，
否则在 PythonAnywhere 安装时可能会因为找不到或版本不兼容而报错。

#### 2. 修改 `settings.py` 以适配生产环境
你的 `settings.py` 目前是为本地开发配置的，需要做一些调整才能让它在 PythonAnywhere 上正常运行。

*   **设置 `ALLOWED_HOSTS`**：这是为了安全，必须添加 PythonAnywhere 分配给你的域名。
    ```python
    # 在 settings.py 中找到并修改 ALLOWED_HOSTS
    ALLOWED_HOSTS = ['你的用户名.pythonanywhere.com', 'localhost', '127.0.0.1']
    ```

*   **配置静态文件目录 (`STATIC_ROOT`)**：你需要告诉 Django，当执行 `collectstatic` 命令时，把收集到的所有静态文件放到哪个地方去。
    ```python
    # 在 settings.py 文件末尾附近添加
    # 确保 BASE_DIR 已经在文件开头定义过了
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    ```

*   **切换 `DEBUG` 模式**：在生产环境运行，`DEBUG` 必须设为 `False`。虽然这会在页面出错时显示更少的调试信息，但这是安全且必须的。
    ```python
    # 将 DEBUG 改为 False
    DEBUG = False
    ```

#### 3. （可选但推荐）创建 `.gitignore` 文件

这个文件告诉 Git 哪些文件或文件夹**不要**上传到 GitHub，能有效避免仓库体积膨胀和敏感信息泄露。
在你的项目根目录下创建一个名为 `.gitignore` 的文件，并写入以下基本内容：

```
ll_venv/          # 虚拟环境，不需要上传
__pycache__/      # Python 缓存文件
*.pyc             # 编译后的字节码文件
db.sqlite3        # SQLite 数据库文件（建议本地和线上分开）
.DS_Store         # macOS 系统文件
/staticfiles/     # 这个文件夹是运行 collectstatic 时生成的，不需要上传
```

#### 4. 提交并推送所有更改到 GitHub

完成以上修改后，你需要在本地进行一次 Git 提交，并推送到 GitHub 远程仓库，这样 PythonAnywhere 才能拉取到最新的代码。

```bash
git add .
git commit -m "准备部署到 PythonAnywhere：更新配置和依赖"
git push origin main  # 如果默认分支是 master，则用 git push origin master
```

---

### 💎 总结一下你现在要做的事

1.  **在本地**：运行 `pip freeze > requirements.txt`，并检查文件内容。
2.  **在本地**：修改 `settings.py` 中的 `ALLOWED_HOSTS`、`STATIC_ROOT` 和 `DEBUG`。
3.  **（可选）在本地**：创建 `.gitignore` 文件，避免上传无关文件。
4.  **在本地**：通过 `git add`、`git commit` 和 `git push`，将以上所有更改推送到 GitHub。

完成这些，你的本地准备工作就绪了。
接下来，你就可以在 PythonAnywhere 的 Bash 控制台里，通过 `git clone` 拉取代码，然后按照我们上次讨论的步骤，一步步部署上线了。

💪
****************************************************************************************
下一步：进入项目目录并开始部署到托管平台、服务器平台
******************************************************************************************

在 Bash 终端中，依次执行以下命令：
### 1. 进入项目目录
bash
cd chapter18_learning_log

### 2. 查看文件是否完整（可选）
bash
ls -la
你应该能看到 `manage.py`、`ll_project/`、`learning_logs/`、`user_accounts/`、`requirements.txt` 等文件和文件夹。

### 3. 创建虚拟环境
bash
python -m venv myvenv

### 4. 激活虚拟环境
bash
source myvenv/bin/activate

激活后，终端提示符前面会出现 `(myvenv)`。

### 5. 安装依赖包
bash
pip install -r requirements.txt
这会根据你精简后的 `requirements.txt` 安装 Django、django-bootstrap5 等必要包。

### 6. 收集静态文件
bash
python manage.py collectstatic
输入 `yes` 确认，Django 会把所有静态文件收集到 `staticfiles` 目录。

### 7. 迁移数据库
bash
python manage.py migrate

这会创建 SQLite 数据库和所有需要的表。

### 8. 创建超级用户（可选，方便管理后台）
bash
python manage.py createsuperuser

按提示输入用户名、邮箱、密码。

## 完成这些后，去 Web 页面配置

1. 回到 PythonAnywhere 仪表板，点击 **Web** 页面
2. 点击 **Add a new web app**，选择 **Manual Configuration**，Python 版本选你本地用的版本（如 3.12）
3. 在 **Code** 部分：
   - **Source code**：`/home/eleium/chapter18_learning_log`
   - **Virtualenv**：`/home/eleium/chapter18_learning_log/myvenv`
4. 编辑 **WSGI configuration file**，配置 Django 入口
5. 在 **Static files** 部分添加 `/static/` → `/home/eleium/chapter18_learning_log/staticfiles`
6. 点击 **Reload** 启动网站
💪
"""
