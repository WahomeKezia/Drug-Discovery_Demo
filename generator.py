# small molecules without using the gt4sd tool
import urllib.request
from rdkit import Chem
from rdkit.Chem import AllChem

# Download the PDB file
urllib.request.urlretrieve('https://files.rcsb.org/download/8UIS.pdb', '8UIS.pdb')

# Load the protein structure from the downloaded PDB file
protein = Chem.MolFromPDBFile('8UIS.pdb')

# Generate small molecules from protein structure
mols = AllChem.EditableMol(protein)
mols.AddAtom(Chem.Atom(6))  # Add a carbon atom
mols.AddBond(0, 1, order=Chem.rdchem.BondType.SINGLE)  # Add a bond between the carbon atom and the protein
small_molecule = mols.GetMol()

# Save the small molecule to a file
Chem.MolToPDBFile(small_molecule, 'small_molecule.pdb')
