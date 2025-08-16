# AI企业官网项目

## 项目简介
这是一个极简科技风的AI企业官网，旨在展示公司AI智能体开发和企业AI工作赋能的核心业务，提供用户登录注册和预约AI定制功能。

## 技术栈
- 前端：HTML + CSS + JavaScript + Tailwind CSS
- 后端：Python + Flask
- 数据库：SQLite (默认) / MySQL
- 其他工具：Flask-SQLAlchemy, Flask-Cors, python-dotenv

## 目录结构
```
wz/
├── .env                # 环境变量配置
├── app.py              # 后端主应用
├── models.py           # 数据模型
├── requirements.txt    # 依赖包列表
├── README.md           # 项目说明
├── index.html          # 首页
├── about.html          # 关于我们
├── login.html          # 登录页面
├── booking.html        # 预约页面
├── routes/             # 路由文件夹
│   ├── auth.py         # 认证路由
│   └── booking.py      # 预约路由
└── static/             # 静态资源文件夹（存放图片等）
```

## 本地开发环境搭建
1. 确保已安装Python 3.12
2. 克隆项目到本地
3. 进入项目目录
   ```
   cd wz
   ```
4. 创建虚拟环境
   ```
   python -m venv venv
   ```
5. 激活虚拟环境
   - Windows: 
     ```
     venv\Scripts\activate
     ```
   - macOS/Linux: 
     ```
     source venv/bin/activate
     ```
6. 安装依赖
   ```
   pip install -r requirements.txt
   ```
7. 修改.env文件，配置数据库和其他参数
8. 运行应用
   ```
   python app.py
   ```
9. 在浏览器中访问 http://localhost:5000

## 部署步骤
### 阿里云虚拟主机部署
1. 购买阿里云虚拟主机（选择支持Python的主机）
2. 通过FTP上传项目文件到主机
3. 在主机控制面板中创建Python环境
4. 安装项目依赖
5. 配置环境变量
6. 启动应用

### 腾讯云轻量应用服务器部署
1. 购买腾讯云轻量应用服务器
2. 通过SSH连接服务器
3. 安装Python 3.12
4. 克隆项目到服务器
5. 创建虚拟环境并安装依赖
6. 配置Nginx作为反向代理
7. 使用Gunicorn运行应用
8. 设置开机自启动

## 基础修改指南
### 更换Banner图
1. 将新图片上传到static文件夹
2. 编辑index.html文件，找到Banner图相关代码
3. 修改图片路径为新图片的路径

### 修改业务描述文字
1. 编辑index.html文件
2. 找到业务板块相关代码
3. 修改对应的文字内容

### 更新公司简介
1. 编辑about.html文件
2. 找到公司简介相关代码
3. 修改文字内容

## 联系方式
如有问题或建议，请联系：contact@aitech.com