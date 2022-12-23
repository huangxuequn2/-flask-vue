from flask import jsonify
from app.api import bp

@bp.route('/ping',methods=['GET'])
def ping():
    '''前端vue.js用来测试与后端flask API的连通性'''
    return jsonify('Pong!')