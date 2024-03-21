import gradio as gr  # Import Gradio module
import requests  # Import requests module for making HTTP requests

# Define algorithm versions dropdown options
algorithm_versions = [
    ('fast-example-v1', 'fast-example-v1'),
    ('v0', 'v0'),
    ('v11', 'v11'),
    ('v12', 'v12'),
    ('v10', 'v10'),
    ('fast-example-v0', 'fast-example-v0')
]

# Define a function to interact with the backend
def predict(algorithm_version, property_goals, protein_target, decoding_temperature, maximal_sequence_length, number_of_samples, limit, number_of_steps, number_of_initial_points, number_of_optimization_rounds, sampling_variance, samples_used_for_evaluation, maximum_number_of_sampling_steps, seed):
    # Send a POST request to the backend with the input data as JSON
    response = requests.post('http://localhost:5000/predict', json={
        "algorithm_version": algorithm_version,
        "property_goals": property_goals,
        "protein_target": protein_target,
        "decoding_temperature": decoding_temperature,
        "maximal_sequence_length": maximal_sequence_length,
        "number_of_samples": number_of_samples,
        "limit": limit,
        "number_of_steps": number_of_steps,
        "number_of_initial_points": number_of_initial_points,
        "number_of_optimization_rounds": number_of_optimization_rounds,
        "sampling_variance": sampling_variance,
        "samples_used_for_evaluation": samples_used_for_evaluation,
        "maximum_number_of_sampling_steps": maximum_number_of_sampling_steps,
        "seed": seed
    })
    return response.json()  # Return the JSON response from the backend

# Create a Gradio interface for the predict function
iface = gr.Interface(
    predict,
    [
        "dropdown", algorithm_versions,  # Use the algorithm_versions list here
        "checkboxgroup", ["qed"],
        "textbox",
        "slider", (0.5, 2),
        "slider", (5, 400),
        "slider", (1, 50),
        "slider", (1, 8),
        "slider", (1, 32),
        "slider", (1, 32),
        "slider", (1, 4),
        "slider", (0.01, 1),
        "slider", (1, 10),
        "slider", (1, 64),
        "number"
    ],
    "json"
)
iface.launch()  # Launch the Gradio interface
