from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

# Load FHIR data
with open('static/data/fhir_bundle.json') as f:
    fhir_data = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET'])
def get_data():
    drug_name = request.args.get('drug')
    if drug_name:
        filtered_data = [entry for entry in fhir_data['entry'] if entry['resource']['code']['coding'][0]['display'].lower() == drug_name.lower()]
        return jsonify(filtered_data)
    return jsonify(fhir_data['entry'])

if __name__ == '__main__':
    app.run(debug=True)
