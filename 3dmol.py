# import streamlit as st
# import requests

# # Import necessary libraries for protein visualization
# from IPython.display import HTML

# # Function to generate 3Dmol viewer HTML
# def render_3dmol(data):
#     html = '''
#     <script src="https://3Dmol.org/build/3Dmol-min.js"></script>     
#     <script src="https://3Dmol.org/build/3Dmol-ui-min.js"></script>     
#     <div style="height: 400px; width: 100%;" class='viewer_3Dmoljs' data-backgroundcolor='0xffffff' data-style='stick' data-ui='true'>{}</div>
#     '''.format(data)
#     return html

# # Main Streamlit app
# def main():
#     st.title('Protein Visualization')

#     # Input URL for PDB file
#     pdb_url = st.text_input('Enter URL for PDB file')

#     if pdb_url:
#         # Fetch PDB data from URL
#         response = requests.get(pdb_url)
        
#         if response.status_code == 200:
#             pdb_data = response.text
#             st.markdown(render_3dmol(pdb_data), unsafe_allow_html=True)
#         else:
#             st.error('Failed to fetch PDB data from the provided URL')

# if __name__ == '__main__':
#     main()
import streamlit as st
import nglview as nv

def main():
    st.title('Protein Structure Visualization')

    pdb_url = st.text_input('Enter URL for PDB file')

    if st.button('Visualize'):
        if pdb_url:
            view = nv.show_pdbid(pdb_url)
            view._remote_call('setSize', target='Widget', args=['100%', '600px'])
            st.write(view)

if __name__ == '__main__':
    main()
