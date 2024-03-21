import streamlit as st
from gradio_client import Client
from rdkit import Chem
from rdkit.Chem import Draw
import sqlite3

# Initialize Gradio client
client = Client("https://gt4sd-paccmann-gp.hf.space/")

# Function to generate molecules from protein sequence using Hugging Face API
def generate_molecules(protein_sequence):
    result = client.predict(
        "fast-example-v1,fast-example-v1",  # Algorithm version
        ["qed"],  # Property goals
        protein_sequence,  # Protein target
        0.5,  # Decoding temperature
        5,  # Maximal sequence length
        1,  # Number of samples
        1,  # Limit
        1,  # Number of steps
        1,  # Number of initial points
        1,  # Number of optimization rounds
        0.01,  # Sampling variance
        1,  # Samples used for evaluation
        1,  # Maximum number of sampling steps
        5,  # Seed
        api_name="/predict"
    )
    return result

# Function to convert SMILES to molecule image
def smiles_to_image(smiles):
    mol = Chem.MolFromSmiles(smiles)
    img = Draw.MolToImage(mol)
    return img

# Create SQLite connection and cursor
conn = sqlite3.connect('protein_db.sqlite')
c = conn.cursor()

# Create table for storing protein information
c.execute('''CREATE TABLE IF NOT EXISTS proteins
             (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, sequence TEXT)''')
conn.commit()

# Streamlit app
st.title("Protein to Molecule Generator")

# Add protein to the database
name = st.text_input("Enter protein name:")
sequence = st.text_area("Enter protein sequence:")
if st.button("Add Protein"):
    c.execute("INSERT INTO proteins (name, sequence) VALUES (?, ?)", (name, sequence))
    conn.commit()
    st.success("Protein added successfully.")

# Select protein from the database
selected_protein_name = st.selectbox("Select protein:", [""] + [row[1] for row in c.execute("SELECT name FROM proteins").fetchall()])
if selected_protein_name:
    selected_protein_sequence = c.execute("SELECT sequence FROM proteins WHERE name=?", (selected_protein_name,)).fetchone()[0]
    generated_molecules = generate_molecules(selected_protein_sequence)
    st.write("Generated Molecules:")
    for i, molecule in enumerate(generated_molecules):
        st.image(smiles_to_image(molecule), caption=f"Molecule {i+1}", use_column_width=True)

# Close SQLite connection
conn.close()
