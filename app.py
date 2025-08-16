# -*- coding: utf-8 -*-
"""
主应用文件
功能：初始化Flask应用，配置路由和数据库
输入：无
输出：运行Flask应用
"""
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 初始化Flask应用
app = Flask(__name__, static_folder='static', template_folder='.')

# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev_key')

# 初始化数据库
db = SQLAlchemy(app)
# 初始化迁移工具
migrate = Migrate(app, db)
# 启用CORS
CORS(app)

# 导入路由
from routes.auth import auth_bp
from routes.booking import booking_bp

# 注册蓝图
app.register_blueprint(auth_bp)
app.register_blueprint(booking_bp)

# 首页路由
@app.route('/')
def index():
    return render_template('index.html')

# 关于我们路由
@app.route('/about')
def about():
    return render_template('about.html')

# 登录路由
@app.route('/login')
def login():
    return render_template('login.html')

# 预约路由
@app.route('/booking')
def booking():
    return render_template('booking.html')

# 解决循环导入问题：在需要使用模型的地方再导入
# 注意：在实际生产环境中，可能需要考虑更复杂的重构方案

# 错误处理 - 404
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': '页面不存在'}), 404

# 错误处理 - 500
@app.errorhandler(500)
def server_error(e):
    return jsonify({'error': '服务器内部错误'}), 500

if __name__ == '__main__':
    # 创建数据库表
    with app.app_context():
        db.create_all()
    # 运行应用
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=True)