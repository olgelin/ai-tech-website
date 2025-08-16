# -*- coding: utf-8 -*-
"""
认证路由文件
功能：处理用户登录、注册等认证请求
输入：HTTP请求
输出：JSON响应
"""
from flask import Blueprint, request, jsonify
import re
import random
import time

# 创建蓝图
auth_bp = Blueprint('auth', __name__)

# 模拟短信验证码存储
sms_codes = {}

@auth_bp.route('/api/register', methods=['POST'])
def register():
    """用户注册
    请求参数：
        phone: 手机号
        password: 密码
        code: 验证码
    返回：
        JSON: 注册结果
    """
    # 延迟导入，解决循环依赖
    from models import User
    from app import db

    data = request.json
    phone = data.get('phone')
    password = data.get('password')
    code = data.get('code')

    # 验证参数
    if not all([phone, password, code]):
        return jsonify({'code': 400, 'message': '参数不完整'}), 400

    if not re.match(r'^1[3-9]\d{9}$', phone):
        return jsonify({'code': 400, 'message': '手机号格式不正确'}), 400

    if len(password) < 6:
        return jsonify({'code': 400, 'message': '密码长度不能少于6位'}), 400

    # 验证验证码
    if phone not in sms_codes or sms_codes[phone] != code:
        return jsonify({'code': 400, 'message': '验证码错误'}), 400

    # 检查用户是否已存在
    existing_user = User.query.filter_by(phone=phone).first()
    if existing_user:
        return jsonify({'code': 400, 'message': '该手机号已被注册'}), 400

    # 创建新用户
    user = User(phone=phone, name=f'用户{phone[-4:]}')
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    # 注册成功后删除验证码
    del sms_codes[phone]

    return jsonify({'code': 200, 'message': '注册成功', 'data': user.to_dict()})

@auth_bp.route('/api/login', methods=['POST'])
def login():
    """用户登录
    请求参数：
        phone: 手机号
        password: 密码
    返回：
        JSON: 登录结果
    """
    # 延迟导入，解决循环依赖
    from models import User

    data = request.json
    phone = data.get('phone')
    password = data.get('password')

    # 验证参数
    if not all([phone, password]):
        return jsonify({'code': 400, 'message': '参数不完整'}), 400

    # 查找用户
    user = User.query.filter_by(phone=phone).first()
    if not user or not user.check_password(password):
        return jsonify({'code': 401, 'message': '手机号或密码错误'}), 401

    # 这里简化处理，实际应用中应使用JWT或session
    return jsonify({'code': 200, 'message': '登录成功', 'data': user.to_dict()})

@auth_bp.route('/api/send_code', methods=['POST'])
def send_code():
    """发送验证码
    请求参数：
        phone: 手机号
    返回：
        JSON: 发送结果
    """
    data = request.json
    phone = data.get('phone')

    # 验证参数
    if not phone or not re.match(r'^1[3-9]\d{9}$', phone):
        return jsonify({'code': 400, 'message': '手机号格式不正确'}), 400

    # 生成验证码
    code = ''.join(random.sample('0123456789', 6))

    # 模拟发送短信
    print(f'向手机号 {phone} 发送验证码: {code}')

    # 存储验证码（有效期5分钟）
    sms_codes[phone] = code
    # 设置过期时间（实际应用中应使用redis等存储）
    time.sleep(1)  # 模拟发送延迟

    return jsonify({'code': 200, 'message': '验证码发送成功'})

@auth_bp.route('/api/user_info', methods=['GET'])
def user_info():
    """获取用户信息
    请求参数：
        user_id: 用户ID
    返回：
        JSON: 用户信息
    """
    # 延迟导入，解决循环依赖
    from models import User

    user_id = request.args.get('user_id')

    if not user_id:
        return jsonify({'code': 400, 'message': '用户ID不能为空'}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({'code': 404, 'message': '用户不存在'}), 404

    return jsonify({'code': 200, 'message': '获取成功', 'data': user.to_dict()})