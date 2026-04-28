from flask import Blueprint, jsonify, render_template, request
from .crud import *
from util import login_required


portfolio_bp = Blueprint('portfolio_bp', __name__)


@portfolio_bp.route('/portfolio')
@login_required
def portfolio():
    portfolio_data = get_portfolio()
    return render_template('portfolio.html', portfolio=portfolio_data)


@portfolio_bp.route('/add_portfolio_item', methods=['POST'])
def add_portfolio_item_route():
    data = request.json
    category = data["category"]
    item = data["item"]
    add_portfolio_item(category, item)
    return jsonify(success=True)


@portfolio_bp.route('/update_portfolio_item', methods=['POST'])
def update_portfolio_item_route():
    data = request.json
    category = data["category"]
    old_item = data["old_item"]
    new_item = data["new_item"]
    update_portfolio_item(category, old_item, new_item)
    return jsonify(success=True)


@portfolio_bp.route('/delete_portfolio_item', methods=['POST'])
def delete_portfolio_item_route():
    data = request.json
    category = data["category"]
    item = data["item"]
    delete_portfolio_item(category, item)
    return jsonify(success=True)

