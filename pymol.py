import gradio as gr
from gradio_client import Client
from rdkit import Chem
from rdkit.Chem import Draw

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
    return smiles_to_image(result)

# Function to convert SMILES to molecule image
def smiles_to_image(smiles):
    mol = Chem.MolFromSmiles(smiles)
    img = Draw.MolToImage(mol)
    return img

# Define Gradio interface
iface = gr.Interface(
    fn=generate_molecules,
    inputs="text",  # Use 'text' for simple text input
    outputs="image",  # Specify output type as image
    title="Protein to Molecule Generator",
    description="Enter a protein sequence to generate molecules.",
    capture_session=True  # Captures the Gradio session for deployment
)

# Launch Gradio interface
iface.launch()
