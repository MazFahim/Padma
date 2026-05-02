from flask import Blueprint, jsonify, render_template, request
from .crud import *
from util import login_required


community_bp = Blueprint('community_bp', __name__)


@community_bp.route('/community')
@login_required
def community():
    rows = get_tracker_rows()
    wishlist = get_wishlist()
    return render_template('community.html', rows=rows, wishlist=wishlist)


@community_bp.route('/community/update', methods=['POST'])
def update_row():
    data = request.get_json()
    update_tracker_row(data['category'], data['last_stage'], data['next_stage'])
    return jsonify({"status": "ok"})


@community_bp.route('/community/wishlist/add', methods=['POST'])
@login_required
def add_wish_route():
    data = request.get_json()
    add_wish(data['category'], data['wish'])
    return jsonify({"status": "ok"})

@community_bp.route('/community/wishlist/delete', methods=['POST'])
@login_required
def delete_wish_route():
    data = request.get_json()
    delete_wish(data['category'], data['wish'])
    return jsonify({"status": "ok"})

@community_bp.route('/community/wishlist/update', methods=['POST'])
@login_required
def update_wish_route():
    data = request.get_json()
    update_wish(data['category'], data['old_wish'], data['new_wish'])
    return jsonify({"status": "ok"})
