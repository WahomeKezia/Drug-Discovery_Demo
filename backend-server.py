from flask import Flask, request, jsonify  # Import necessary Flask modules
from gradio_client import Client  # Import Gradio client

app = Flask(__name__)  # Create a Flask application instance
client = Client("https://gt4sd-paccmann-gp.hf.space/")  # Initialize Gradio client

@app.route('/predict', methods=['POST'])  # Define a route for receiving POST requests to /predict
def predict():
    data = request.json  # Extract JSON data from the request
    # Call the Gradio client's predict method with the received data
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
    return jsonify(result)  # Return the result as JSON respo
