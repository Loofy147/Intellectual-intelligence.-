from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .app import db
from .models import Team, TeamMembership, User, Compass

api = Blueprint('api', __name__)

@api.route('/teams', methods=['POST'])
@jwt_required()
def create_team():
    data = request.get_json()
    current_user_id = get_jwt_identity()
    user = db.session.get(User, current_user_id)

    if not user:
        return jsonify({"msg": "User not found"}), 404

    team_name = data.get('team_name')
    company_name = data.get('company_name')

    if not team_name:
        return jsonify({"msg": "Missing team_name parameter"}), 400

    new_team = Team(team_name=team_name, company_name=company_name)
    db.session.add(new_team)

    # The creator automatically becomes a member
    membership = TeamMembership(user=user, team=new_team)
    db.session.add(membership)

    db.session.commit()

    return jsonify({
        "id": new_team.id,
        "team_name": new_team.team_name,
        "company_name": new_team.company_name
    }), 201

@api.route('/teams', methods=['GET'])
@jwt_required()
def get_teams():
    current_user_id = get_jwt_identity()
    user = db.session.get(User, current_user_id)

    if not user:
        return jsonify({"msg": "User not found"}), 404

    teams = [
        {
            "id": membership.team.id,
            "team_name": membership.team.team_name,
            "company_name": membership.team.company_name
        }
        for membership in user.teams
    ]

    return jsonify(teams), 200

@api.route('/teams/<string:team_id>/compasses', methods=['POST'])
@jwt_required()
def create_compass(team_id):
    current_user_id = get_jwt_identity()

    membership = TeamMembership.query.filter_by(team_id=team_id, user_id=current_user_id).first()
    if not membership:
        return jsonify({"msg": "Not a member of this team"}), 403

    data = request.get_json()

    new_compass = Compass(
        team_id=team_id,
        q1=data.get('q1', ''),
        q2=data.get('q2', ''),
        q3=data.get('q3', ''),
        ac1=data.get('ac1', ''),
        ac2=data.get('ac2', ''),
        le1=data.get('le1', ''),
        le2=data.get('le2', ''),
        le3=data.get('le3', '')
    )
    db.session.add(new_compass)
    db.session.commit()

    return jsonify({"id": new_compass.id}), 201

@api.route('/compasses/<string:compass_id>', methods=['GET'])
@jwt_required()
def get_compass(compass_id):
    current_user_id = get_jwt_identity()
    compass = db.session.get(Compass, compass_id)

    if not compass:
        return jsonify({"msg": "Compass not found"}), 404

    membership = TeamMembership.query.filter_by(team_id=compass.team_id, user_id=current_user_id).first()
    if not membership:
        return jsonify({"msg": "Not a member of this team"}), 403

    return jsonify({
        "id": compass.id,
        "team_id": compass.team_id,
        "q1": compass.q1,
        "q2": compass.q2,
        "q3": compass.q3,
        "ac1": compass.ac1,
        "ac2": compass.ac2,
        "le1": compass.le1,
        "le2": compass.le2,
        "le3": compass.le3
    })

@api.route('/compasses/<string:compass_id>', methods=['PUT'])
@jwt_required()
def update_compass(compass_id):
    current_user_id = get_jwt_identity()
    compass = db.session.get(Compass, compass_id)

    if not compass:
        return jsonify({"msg": "Compass not found"}), 404

    membership = TeamMembership.query.filter_by(team_id=compass.team_id, user_id=current_user_id).first()
    if not membership:
        return jsonify({"msg": "Not a member of this team"}), 403

    data = request.get_json()

    compass.q1 = data.get('q1', compass.q1)
    compass.q2 = data.get('q2', compass.q2)
    compass.q3 = data.get('q3', compass.q3)
    compass.ac1 = data.get('ac1', compass.ac1)
    compass.ac2 = data.get('ac2', compass.ac2)
    compass.le1 = data.get('le1', compass.le1)
    compass.le2 = data.get('le2', compass.le2)
    compass.le3 = data.get('le3', compass.le3)

    db.session.commit()
    return jsonify({"msg": "Compass updated successfully"})
