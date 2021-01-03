from flask import Blueprint, request, jsonify
from shared.db_worker import create_user

bp = Blueprint('user', __name__, url_prefix='user')


@bp.route('/', methods=['POST'])
def create():
    return create_user()


@bp.route('/create', methods=['POST'])
def create_from_route():
    return create_user()
