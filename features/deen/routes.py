from flask import Blueprint, jsonify, render_template, request
from .crud import *
from util import login_required


deen_bp = Blueprint('deen_bp', __name__)


@deen_bp.route('/deen')
@login_required
def deen():
    rows = get_tracker_rows()
    wishlist = get_wishlist()
    return render_template('deen.html', rows=rows, wishlist=wishlist)


@deen_bp.route('/deen/update', methods=['POST'])
def update_row():
    data = request.get_json()
    update_tracker_row(data['category'], data['last_stage'], data['next_stage'])
    return jsonify({"status": "ok"})


@deen_bp.route('/deen/wishlist/add', methods=['POST'])
@login_required
def add_wish_route():
    data = request.get_json()
    add_wish(data['category'], data['wish'])
    return jsonify({"status": "ok"})

@deen_bp.route('/deen/wishlist/delete', methods=['POST'])
@login_required
def delete_wish_route():
    data = request.get_json()
    delete_wish(data['category'], data['wish'])
    return jsonify({"status": "ok"})

@deen_bp.route('/deen/wishlist/update', methods=['POST'])
@login_required
def update_wish_route():
    data = request.get_json()
    update_wish(data['category'], data['old_wish'], data['new_wish'])
    return jsonify({"status": "ok"})
