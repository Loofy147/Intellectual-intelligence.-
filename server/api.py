from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, User, Team, TeamMembership, Compass

api_bp = Blueprint('api', __name__, url_prefix='/api')

# --- Team Routes ---

@api_bp.route('/teams', methods=['POST'])
@jwt_required()
def create_team():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    data = request.get_json()
    team_name = data.get('team_name')

    if not team_name:
        return jsonify({"msg": "Team name is required"}), 400

    new_team = Team(team_name=team_name)
    new_team.members.append(user)
    db.session.add(new_team)

    # Set the creator as the 'owner'
    membership = TeamMembership.query.filter_by(user_id=user.id, team_id=new_team.id).first()
    if membership:
        membership.role = 'owner'

    db.session.commit()
    return jsonify({"msg": "Team created successfully", "team_id": new_team.id}), 201

@api_bp.route('/teams', methods=['GET'])
@jwt_required()
def get_teams():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    teams = [{"id": team.id, "team_name": team.team_name} for team in user.teams]
    return jsonify(teams)

# --- Compass Routes ---

@api_bp.route('/teams/<team_id>/compasses', methods=['POST'])
@jwt_required()
def create_compass(team_id):
    # Security check: Ensure user is a member of the team
    current_user_id = get_jwt_identity()
    membership = TeamMembership.query.filter_by(user_id=current_user_id, team_id=team_id).first()
    if not membership:
        return jsonify({"msg": "Not a member of this team"}), 403

    data = request.get_json()
    title = data.get('title', 'Untitled Compass')

    new_compass = Compass(team_id=team_id, title=title, data={})
    db.session.add(new_compass)
    db.session.commit()
    return jsonify({"msg": "Compass created", "compass_id": new_compass.id}), 201

@api_bp.route('/teams/<team_id>/compasses', methods=['GET'])
@jwt_required()
def get_compasses_for_team(team_id):
    # Security check
    current_user_id = get_jwt_identity()
    membership = TeamMembership.query.filter_by(user_id=current_user_id, team_id=team_id).first()
    if not membership:
        return jsonify({"msg": "Not a member of this team"}), 403

    team = Team.query.get(team_id)
    compasses = [{"id": c.id, "title": c.title, "updated_at": c.updated_at} for c in team.compasses]
    return jsonify(compasses)

@api_bp.route('/compasses/<compass_id>', methods=['GET'])
@jwt_required()
def get_compass(compass_id):
    compass = Compass.query.get(compass_id)
    if not compass:
        return jsonify({"msg": "Compass not found"}), 404

    # Security check
    current_user_id = get_jwt_identity()
    membership = TeamMembership.query.filter_by(user_id=current_user_id, team_id=compass.team_id).first()
    if not membership:
        return jsonify({"msg": "Not authorized to view this compass"}), 403

    return jsonify({
        "id": compass.id,
        "title": compass.title,
        "data": compass.data,
        "updated_at": compass.updated_at
    })

@api_bp.route('/compasses/<compass_id>', methods=['PUT'])
@jwt_required()
def update_compass(compass_id):
    compass = Compass.query.get(compass_id)
    if not compass:
        return jsonify({"msg": "Compass not found"}), 404

    # Security check
    current_user_id = get_jwt_identity()
    membership = TeamMembership.query.filter_by(user_id=current_user_id, team_id=compass.team_id).first()
    if not membership:
        return jsonify({"msg": "Not authorized to edit this compass"}), 403

    data = request.get_json()
    compass.title = data.get('title', compass.title)
    compass.data = data.get('data', compass.data)
    db.session.commit()
    return jsonify({"msg": "Compass updated successfully"})
