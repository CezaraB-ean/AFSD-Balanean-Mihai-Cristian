from flask import Blueprint, jsonify, request
import json
import os

items_bp = Blueprint('items', __name__)
DATA_FILE = os.path.join(os.path.dirname(__file__), '../data/items.json')

def load_items():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_items(items):
    with open(DATA_FILE, 'w') as f:
        json.dump(items, f, indent=4)

@items_bp.route('/items', methods=['GET'])
def get_all_items():
    return jsonify(load_items()), 200

@items_bp.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    items = load_items()
    for item in items:
        if str(item['id']) == item_id:
            return jsonify(item), 200
    return jsonify({'error': 'Not found'}), 404

@items_bp.route('/items', methods=['POST'])
def create_item():
    items = load_items()
    new_item = request.get_json()
    new_item['id'] = max((item['id'] for item in items), default=0) + 1
    items.append(new_item)
    save_items(items)
    return jsonify(new_item), 201

@items_bp.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    items = load_items()
    data = request.get_json()
    for item in items:
        if str(item['id']) == item_id:
            item.update(data)
            save_items(items)
            return jsonify(item), 200
    return jsonify({'error': 'Not found'}), 404

@items_bp.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    items = load_items()
    new_items = [item for item in items if str(item['id']) != item_id]
    if len(items) == len(new_items):
        return jsonify({'error': 'Not found'}), 404
    save_items(new_items)
    return jsonify({'message': 'Deleted'}), 200
