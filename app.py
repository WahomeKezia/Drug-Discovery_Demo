from flask import Flask, request, jsonify
from gradio_client import Client

app = Flask(__name__)
client = Client("https://gt4sd-paccmann-gp.hf.space/")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    result = client.predict(
        data["algorithm_version"],
        data["property_goals"],
        data["protein_target"],
        data["decoding_temperature"],
        data["maximal_sequence_length"],
        data["number_of_samples"],
        data["limit"],
        data["number_of_steps"],
        data["number_of_initial_points"],
        data["number_of_optimization_rounds"],
        data["sampling_variance"],
        data["samples_used_for_evaluation"],
        data["maximum_number_of_sampling_steps"],
        data["seed"],
        api_name="/predict"
    )
    return jsonify(result)

@app.route('/')
def home():
    return "Server is running!"

@app.route('/interface')
def interface():
    # Create Gradio interface here if needed
    return "Gradio interface here"

if __name__ == '__main__':
    app.run(debug=True)
