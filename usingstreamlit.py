# import streamlit as st
# from gradio_client import Client
# from rdkit import Chem
# from rdkit.Chem import Draw
# import sqlite3

# # Initialize Gradio client
# client = Client("https://gt4sd-paccmann-gp.hf.space/")

# # Function to generate molecules from protein sequence using Hugging Face API
# def generate_molecules(protein_sequence):
#     result = client.predict(
#         "fast-example-v1,fast-example-v1",  # Algorithm version
#         ["qed"],  # Property goals
#         protein_sequence,  # Protein target
#         0.5,  # Decoding temperature
#         5,  # Maximal sequence length
#         1,  # Number of samples
#         1,  # Limit
#         1,  # Number of steps
#         1,  # Number of initial points
#         1,  # Number of optimization rounds
#         0.01,  # Sampling variance
#         1,  # Samples used for evaluation
#         1,  # Maximum number of sampling steps
#         5,  # Seed
#         api_name="/predict"
#     )
#     return result

# # Function to convert SMILES to molecule image
# def smiles_to_image(smiles):
#     mol = Chem.MolFromSmiles(smiles)
#     img = Draw.MolToImage(mol)
#     return img

# # Create SQLite connection and cursor
# conn = sqlite3.connect('protein_db.sqlite')
# c = conn.cursor()

# # Create table for storing protein information
# c.execute('''CREATE TABLE IF NOT EXISTS proteins
#              (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, sequence TEXT)''')
# conn.commit()

# # Streamlit app
# st.title("Protein to Molecule Generator")

# # Add protein to the database
# name = st.text_input("Enter protein name:")
# sequence = st.text_area("Enter protein sequence:")
# if st.button("Add Protein"):
#     c.execute("INSERT INTO proteins (name, sequence) VALUES (?, ?)", (name, sequence))
#     conn.commit()
#     st.success("Protein added successfully.")

# # Select protein from the database
# selected_protein_name = st.selectbox("Select protein:", [""] + [row[1] for row in c.execute("SELECT name FROM proteins").fetchall()])
# if selected_protein_name:
#     selected_protein_sequence = c.execute("SELECT sequence FROM proteins WHERE name=?", (selected_protein_name,)).fetchone()[0]
#     generated_molecules = generate_molecules(selected_protein_sequence)
#     st.write("Generated Molecules:")
#     for i, molecule in enumerate(generated_molecules):
#         st.image(smiles_to_image(molecule), caption=f"Molecule {i+1}", use_column_width=True)

# # Close SQLite connection
# conn.close()


import streamlit as st
from gradio_client import Client
from rdkit import Chem
from rdkit.Chem import Draw

# Initialize Gradio client
client = Client("https://gt4sd-paccmann-gp.hf.space/")

# Function to generate molecules from parameters using Hugging Face API
def generate_molecules(params):
    result = client.predict(
        "fast-example-v1,fast-example-v1",  # Algorithm version
        ["qed"],  # Property goals
        params['protein_sequence'],  # Protein target
        params['decoding_temperature'],  # Decoding temperature
        params['max_sequence_length'],  # Maximal sequence length
        params['num_samples'],  # Number of samples
        params['limit'],  # Limit
        params['num_steps'],  # Number of steps
        params['num_initial_points'],  # Number of initial points
        params['num_optimization_rounds'],  # Number of optimization rounds
        params['sampling_variance'],  # Sampling variance
        params['samples_used_for_evaluation'],  # Samples used for evaluation
        params['max_num_sampling_steps'],  # Maximum number of sampling steps
        params['seed'],  # Seed
        api_name="/predict"
    )
    return result

# Function to convert SMILES to molecule image
def smiles_to_image(smiles):
    mol = Chem.MolFromSmiles(smiles)
    img = Draw.MolToImage(mol)
    return img

# Streamlit app
st.title("Molecule Generator")

# Add input parameters
params = {}
params['protein_sequence'] = st.text_area("Enter protein sequence:")
params['decoding_temperature'] = st.slider("Decoding Temperature", 0.1, 2.0, 0.5, 0.1)
params['max_sequence_length'] = st.number_input("Maximal Sequence Length", min_value=1, max_value=10, value=5)
params['num_samples'] = st.number_input("Number of Samples", min_value=1, max_value=10, value=1)
params['limit'] = st.number_input("Limit", min_value=1, max_value=10, value=1)
params['num_steps'] = st.number_input("Number of Steps", min_value=1, max_value=10, value=1)
params['num_initial_points'] = st.number_input("Number of Initial Points", min_value=1, max_value=10, value=1)
params['num_optimization_rounds'] = st.number_input("Number of Optimization Rounds", min_value=1, max_value=10, value=1)
params['sampling_variance'] = st.slider("Sampling Variance", 0.01, 0.1, 0.01, 0.01)
params['samples_used_for_evaluation'] = st.number_input("Samples Used for Evaluation", min_value=1, max_value=10, value=1)
params['max_num_sampling_steps'] = st.number_input("Maximum Number of Sampling Steps", min_value=1, max_value=10, value=5)
params['seed'] = st.number_input("Seed", min_value=0, max_value=100, value=5)

# Generate molecules based on input parameters
if st.button("Generate Molecules"):
    generated_molecules = generate_molecules(params)
    st.write("Generated Molecules:")
    for i, molecule in enumerate(generated_molecules):
        st.image(smiles_to_image(molecule), caption=f"Molecule {i+1}", use_column_width=True)
