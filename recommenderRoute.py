from flask import Flask, jsonify, request
from flask_cors import CORS
from recommender import Recommender
app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes
dbPath = './datasets/recipes.csv'
recipeRecommender = Recommender(dbPath, 'recipes')
recipeRecommender.setup('name', 'ingredients')

@app.route('/run_script', methods=['GET'])
def run_script():
    return jsonify({'result': 'Replace this with your Python script output'})

@app.route('/recommendations',methods=['GET'])
def recommendation():
    query = request.args.get('query')
    return (jsonify(recipeRecommender.find_ksimilar(query,10,'name').tolist()))


if __name__ == '__main__':
    app.run(port=5000)
