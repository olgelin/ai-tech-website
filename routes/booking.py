# -*- coding: utf-8 -*-
"""
预约路由文件
功能：处理预约表单提交和管理
输入：HTTP请求
输出：JSON响应
"""
from flask import Blueprint, request, jsonify

# 创建蓝图
booking_bp = Blueprint('booking', __name__)

@booking_bp.route('/api/booking/create', methods=['POST'])
def create_booking():
    """创建预约
    请求参数：
        user_id: 用户ID
        name: 姓名
        phone: 手机号
        company: 公司名称
        need_type: 需求类型
        description: 需求描述
    返回：
        JSON: 预约结果
    """
    # 延迟导入，解决循环依赖
    from models import Booking, User
    from app import db

    data = request.json
    user_id = data.get('user_id')
    name = data.get('name')
    phone = data.get('phone')
    company = data.get('company')
    need_type = data.get('need_type')
    description = data.get('description')

    # 验证参数
    if not all([user_id, name, phone, company, need_type, description]):
        return jsonify({'code': 400, 'message': '参数不完整'}), 400

    # 验证用户是否存在
    user = User.query.get(user_id)
    if not user:
        return jsonify({'code': 404, 'message': '用户不存在'}), 404

    # 创建预约
    booking = Booking(
        user_id=user_id,
        name=name,
        phone=phone,
        company=company,
        need_type=need_type,
        description=description
    )
    db.session.add(booking)
    db.session.commit()

    return jsonify({'code': 200, 'message': '预约创建成功', 'data': booking.to_dict()})

@booking_bp.route('/api/booking/list', methods=['GET'])
def list_bookings():
    """获取用户预约列表
    请求参数：
        user_id: 用户ID
    返回：
        JSON: 预约列表
    """
    # 延迟导入，解决循环依赖
    from models import Booking, User

    user_id = request.args.get('user_id')

    if not user_id:
        return jsonify({'code': 400, 'message': '用户ID不能为空'}), 400

    # 验证用户是否存在
    user = User.query.get(user_id)
    if not user:
        return jsonify({'code': 404, 'message': '用户不存在'}), 404

    # 获取预约列表
    bookings = Booking.query.filter_by(user_id=user_id).order_by(Booking.created_at.desc()).all()
    booking_list = [booking.to_dict() for booking in bookings]

    return jsonify({'code': 200, 'message': '获取成功', 'data': booking_list})

@booking_bp.route('/api/booking/detail', methods=['GET'])
def booking_detail():
    """获取预约详情
    请求参数：
        booking_id: 预约ID
    返回：
        JSON: 预约详情
    """
    # 延迟导入，解决循环依赖
    from models import Booking

    booking_id = request.args.get('booking_id')

    if not booking_id:
        return jsonify({'code': 400, 'message': '预约ID不能为空'}), 400

    # 获取预约详情
    booking = Booking.query.get(booking_id)
    if not booking:
        return jsonify({'code': 404, 'message': '预约不存在'}), 404

    return jsonify({'code': 200, 'message': '获取成功', 'data': booking.to_dict()})

@booking_bp.route('/api/booking/cancel', methods=['POST'])
def cancel_booking():
    """取消预约
    请求参数：
        booking_id: 预约ID
        user_id: 用户ID
    返回：
        JSON: 取消结果
    """
    # 延迟导入，解决循环依赖
    from models import Booking
    from app import db

    data = request.json
    booking_id = data.get('booking_id')
    user_id = data.get('user_id')

    if not all([booking_id, user_id]):
        return jsonify({'code': 400, 'message': '参数不完整'}), 400

    # 获取预约
    booking = Booking.query.get(booking_id)
    if not booking:
        return jsonify({'code': 404, 'message': '预约不存在'}), 404

    # 验证用户权限
    if booking.user_id != int(user_id):
        return jsonify({'code': 403, 'message': '无权操作此预约'}), 403

    # 取消预约
    booking.status = 'canceled'
    db.session.commit()

    return jsonify({'code': 200, 'message': '预约已取消', 'data': booking.to_dict()})