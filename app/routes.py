from flask import Blueprint, request, jsonify

bp = Blueprint('main', __name__)

# Sample recommendations data
recommendations = {
    "anxiety": ["Practice mindfulness", "Try deep breathing", "Talk to a therapist"],
    "stress": ["Exercise regularly", "Limit caffeine", "Try relaxation techniques"],
    "depression": ["Seek professional help", "Stay connected with loved ones", "Engage in hobbies"]
}

@bp.route('/recommend', methods=['GET'])
def recommend():
    issue = request.args.get('issue')
    if issue in recommendations:
        return jsonify({"issue": issue, "recommendations": recommendations[issue]})
    else:
        return jsonify({"error": "Issue not found"}), 404
