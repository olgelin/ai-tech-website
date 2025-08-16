# -*- coding: utf-8 -*-
"""
数据模型文件
功能：定义数据库表结构
输入：无
输出：数据模型类
"""
from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    """用户模型
    属性：
        id: 用户ID
        phone: 手机号
        password_hash: 密码哈希
        name: 姓名
        created_at: 创建时间
        updated_at: 更新时间
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(11), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    bookings = db.relationship('Booking', backref='user', lazy=True)

    def set_password(self, password):
        """设置密码
        参数：
            password: 原始密码
        返回：
            无
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """验证密码
        参数：
            password: 输入的密码
        返回：
            bool: 是否匹配
        """
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        """转换为字典
        返回：
            dict: 用户信息字典
        """
        return {
            'id': self.id,
            'phone': self.phone,
            'name': self.name,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

class Booking(db.Model):
    """预约模型
    属性：
        id: 预约ID
        user_id: 用户ID
        name: 姓名
        phone: 手机号
        company: 公司名称
        need_type: 需求类型
        description: 需求描述
        status: 状态
        created_at: 创建时间
        updated_at: 更新时间
    """
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    need_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, processing, completed, canceled
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def to_dict(self):
        """转换为字典
        返回：
            dict: 预约信息字典
        """
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'company': self.company,
            'need_type': self.need_type,
            'description': self.description,
            'status': self.status,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }