# 这是一个网页！

不过只是一个 Demo。

目录结构：

```bash
.
├── app
│   ├── __init__.py
│   ├── models.py
│   ├── routes
│   │   ├── api.py
│   │   └── main.py
│   ├── static
│   │   ├── css
│   │   ├── img
│   │   └── js
│   └── templates
├── config.py
├── README.md
├── requirements.txt
└── run.py
```

`app` 中存放网页的主要文件。其中 `./app/__init__.py` 用于初始化 Flask 应用，`./app/routes` 用于定义路由，`./app/templates` 用于存放 HTML 模板，`./app/static` 用于存放静态文件，静态文件包括 CSS、JavaScript 和图片等。

配置信息存放在 `config.py` 中，依赖的 Python 包在 `requirements.txt` 中列出，使用 `run.py` 启动网页。