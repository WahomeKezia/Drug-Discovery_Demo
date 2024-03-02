from gradio_client import Client

client = Client("https://gt4sd-paccmann-rl.hf.space/")
result = client.predict(
		"Protein_v0,Protein_v0",	# str (Option from: [('Protein_v0', 'Protein_v0'), ('Omic_v0', 'Omic_v0')]) in 'Algorithm version' Dropdown component
		"Conditional",	# str  in 'Inference type' Radio component
		"MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTT",	# str  in 'Protein target' Textbox component
		"0.08 0.9 0.47 0.91 0.7 0.88 0.95 0.37 0.72 0.42 0.63 0.77 0.65 0.83 0.48 0.31 0.36 0.33 0.64 0.33 1.0 0.82 0.49 0.98 0.96 0.86 0.1 0.92 0.13 0.41 0.88 0.79 0.88 0.01 0.3 0.98 0.91 0.83 0.06 0.77 0.56 0.87 0.78 0.27 0.97 0.14 0.71 0.1 0.08 0.63 0.53 0.6 0.66 0.04 0.46 0.6 0.59 0.36 0.65 0.57 0.96 0.42 0.37 0.18 0.71 0.5 0.54 0.22 0.21 0.53 0.66 0.9 0.4 0.95 0.48 0.81 0.47 0.27 0.56 0.77 0.32 0.66 0.01 0.82 0.29 0.81 0.7 0.77 0.65 0.36 0.78 0.31 0.85 0.69 0.12 0.04 0.39 0.11 0.13 0.15 0.35 0.97 0.66 0.35 0.78 0.33 0.48 0.8 0.26 0.05 0.69 0.07 0.92 0.22 0.35 0.13 0.22 0.94 0.73 0.81 0.29 0.3 0.13 0.06 0.9 0.62 0.19 0.69 0.72 0.55 0.34 0.26 0.72 0.95 0.81 0.78 0.5 0.47 0.67 0.49 0.48 0.75 0.52 0.91 0.42 0.62 0.8 0.17 1.0 0.35 0.63 0.02 0.79 0.67 0.99 0.86 0.71 0.15 0.13 0.54 0.19 0.81 0.56 0.98 0.16 0.15 0.69 0.17 0.66 0.74 0.65 0.9 0.73 0.61 0.69 0.19 0.04 0.72 0.41 0.35 0.93 0.91 0.34 0.35 0.92 0.45 0.34 0.52 0.73 0.39 0.54 0.83 0.99 0.68 0.16 0.6 0.48 0.18 0.96 0.7 0.18 0.77 0.6 0.07 0.99 0.97 0.41 0.25 0.98 0.85 0.95 0.59 0.77 0.18 0.22 0.39 0.33 0.46 0.07 0.16 0.81 0.0 0.53 0.49 0.9 0.57 0.03 0.26 0.24 0.57 0.63 0.88 0.57 0.73 0.6 0.71 0.29 0.25 0.94 0.23 0.93 0.07 0.35 0.59 0.66 0.51 0.25 0.51 0.47 0.04 0.85 0.15 0.4 0.51 0.0 0.29 0.29 0.07 0.14 0.77 0.1 0.31 0.95 0.52 0.48 0.24 0.71 0.27 0.93 0.77 0.04 0.92 0.08 0.92 0.68 0.32 0.15 0.77 0.63 0.73 0.14 0.83 0.76 0.96 0.72 0.57 0.92 0.35 0.62 0.21 0.46 0.66 0.89 0.52 0.35 0.71 0.0 0.78 0.51 0.34 0.05 0.57 0.34 0.54 0.57 0.81 0.88 0.61 0.53 0.98 0.26 0.34 0.57 0.94 0.09 0.94 0.15 0.81 0.15 0.83 0.83 0.73 0.33 0.69 0.89 0.46 0.96 0.12 0.82 0.89 0.45 0.26 0.84 0.48 0.51 0.43 0.12 0.74 0.32 0.19 0.8 0.04 0.61 0.63 0.23 0.22 0.7 0.14 0.63 0.35 0.89 0.4 0.1 0.1 0.56 0.98 0.7 0.41 0.78 0.14 0.04 0.97 0.32 0.66 0.54 0.66 0.8 0.86 0.36 0.99 0.01 0.41 0.62 0.81 0.14 0.84 0.49 0.3 0.4 0.13 0.2 0.05 0.29 0.11 0.75 0.87 0.71 0.25 0.43 0.67 0.49 0.2 0.77 0.85 0.32 0.94 0.51 0.95 0.54 0.22 0.7 0.97 0.71 0.24 0.88 0.9 0.61 0.99 0.57 0.25 0.01 0.09 0.83 0.83 0.89 0.58 0.95 0.86 0.06 0.88 0.27 0.12 0.7 0.17 0.23 0.43 0.61 0.51 0.65 0.02 0.19 0.61 0.69 0.14 0.89 0.3 0.86 0.55 0.06 0.46 0.78 0.82 0.34 0.63 0.38 0.12 0.15 0.45 0.93 0.08 0.54 0.94 0.64 0.74 0.4 0.23 0.18 0.27 0.44 0.6 0.82 0.19 0.13 0.48 0.19 0.99 0.66 0.69 0.86 0.47 0.15 0.94 0.53 0.07 0.61 0.44 0.62 0.85 0.16 0.66 0.58 0.63 0.55 0.38 0.02 0.68 0.91 0.89 0.63 0.25 0.58 0.93 0.52 0.7 0.64 0.81 0.47 0.21 0.18 0.17 0.78 0.46 0.31 0.2 0.31 0.37 0.66 0.46 0.11 1.0 0.21 0.39 0.12 0.36 0.83 0.52 0.76 0.23 0.62 0.17 0.21 0.07 0.78 0.12 0.59 0.76 0.33 0.49 0.13 0.67 0.44 0.92 0.84 0.18 0.73 0.81 0.68 0.27 0.28 0.14 0.23 0.98 0.07 0.34 0.2 0.78 0.44 0.27 0.7 0.88 0.28 0.96 0.07 0.33 0.65 0.9 0.99 0.75 0.32 0.68 0.54 0.57 0.28 0.57 0.96 0.91 0.0 0.0 0.32 0.66 0.08 0.7 0.14 0.88 0.91 0.85 0.17 0.91 0.31 0.47 0.69 0.41 0.8 0.08 0.59 0.66 0.79 0.82 0.28 0.11 0.05 0.11 0.61 0.66 0.25 0.32 0.53 0.8 0.11 0.5 0.6 0.73 0.31 0.11 0.2 1.0 0.79 0.88 0.77 0.37 0.51 0.25 0.89 0.79 0.8 0.79 0.96 0.45 0.36 0.14 0.64 0.85 0.75 0.23 0.64 0.23 0.64 0.41 0.76 0.78 0.13 0.37 0.48 0.61 0.32 0.58 0.98 0.58 0.27 0.06 0.78 0.05 0.56 0.14 0.57 0.2 0.68 0.61 0.58 0.36 0.39 0.99 0.63 0.12 0.82 0.05 0.54 0.96 0.27 0.2 0.94 0.03 0.55 0.9 0.47 0.61 0.83 0.72 0.9 0.94 0.53 0.11 0.57 0.96 0.64 0.35 0.81 0.72 0.59 0.45 0.85 0.98 0.44 0.08 0.12 0.5 0.17 0.31 0.8 0.49 0.13 0.63 0.83 0.32 0.22 0.13 0.76 0.18 0.4 0.81 0.65 0.02 0.94 0.39 0.0 0.58 0.96 0.93 0.33 0.22 0.12 0.78 0.22 0.65 0.82 0.83 0.79 0.09 0.86 0.55 0.16 0.95 0.76 0.22 0.06 0.21 0.58 0.63 0.31 0.21 0.99 0.19 0.13 0.68 0.33 0.82 0.91 0.42 0.37 0.55 0.66 0.29 0.36 0.75 0.62 1.0 0.71 0.21 0.17 0.73 0.23 0.6 0.99 0.85 0.22 0.58 0.4 0.97 0.46 0.69 0.19 0.78 0.26 0.0 0.74 0.43 0.17 0.05 0.74 0.46 0.23 0.64 0.13 0.47 0.14 0.54 0.48 0.88 0.64 0.23 0.48 0.82 0.81 0.56 0.99 0.07 0.07 0.53 0.74 0.67 0.52 0.66 0.14 0.52 0.46 0.85 0.44 0.05 0.13 0.56 0.38 0.57 0.15 0.84 0.99 0.97 0.0 0.12 0.07 0.79 0.29 0.02 0.54 0.39 0.26 0.28 0.44 0.88 0.62 0.63 0.16 0.67 0.66 0.03 0.97 0.83 0.95 0.84 0.95 0.56 0.67 0.38 0.71 0.16 0.43 0.29 0.34 0.71 0.44 0.63 0.7 0.11 0.72 0.23 0.94 0.02 0.33 0.33 0.92 0.35 0.31 0.17 0.36 0.91 0.75 0.1 0.65 0.83 0.79 0.58 0.43 0.8 0.19 0.64 0.3 0.57 0.01 0.41 0.9 0.46 0.31 0.88 0.19 0.02 0.75 0.07 0.45 0.18 0.25 0.01 0.97 0.75 0.64 0.23 0.34 0.07 0.21 0.22 0.02 0.92 0.02 0.69 0.1 0.86 0.05 0.02 0.81 0.96 0.85 0.13 0.55 0.99 0.49 0.89 0.13 0.52 0.91 0.69 0.97 0.95 0.81 0.12 0.92 0.44 0.89 0.57 0.47 0.47 0.78 0.12 0.26 0.24 0.44 0.74 0.43 0.06 0.32 0.89 0.03 0.64 0.18 0.22 0.25 0.14 0.24 0.72 0.96 0.72 0.96 0.52 0.7 0.66 0.88 0.25 0.91 0.14 0.52 0.7 0.56 0.59 0.43 0.21 0.8 0.67 0.33 0.63 0.55 0.55 0.92 0.16 0.31 0.61 0.29 0.9 0.06 0.69 0.89 0.12 0.58 0.74 0.83 0.8 0.14 0.04 0.69 0.28 0.62 0.77 0.11 0.62 0.18 0.59 0.17 0.58 0.1 0.08 0.61 0.46 0.2 0.6 0.94 0.65 0.1 0.47 0.35 0.51 0.8 0.2 0.06 0.86 1.0 0.73 0.43 0.41 0.88 0.46 0.83 0.5 0.15 0.22 0.85 0.79 0.5 0.67 0.99 0.89 0.75 0.82 0.07 0.45 0.54 0.82 0.34 0.01 0.97 0.41 0.53 0.18 0.56 0.02 0.63 0.64 0.21 0.84 0.25 0.41 0.46 0.73 0.91 0.71 0.16 0.01 0.09 0.95 0.7 0.45 0.86 0.9 0.04 0.98 0.66 0.93 0.58 0.37 0.62 0.73 0.37 0.3 0.71 0.95 0.41 0.79 0.45 0.71 0.57 0.24 0.43 0.07 0.85 0.53 0.57 0.58 0.45 0.82 0.92 0.17 0.23 0.29 0.62 0.03 0.36 0.68 0.5 0.69 0.07 0.07 0.36 0.94 0.06 0.4 0.93 0.48 0.17 0.78 0.66 0.45 0.82 0.93 0.99 0.51 0.19 0.32 0.47 0.69 0.19 0.35 0.19 0.62 0.34 0.52 0.42 0.76 0.05 0.9 0.53 0.59 0.52 0.43 0.73 0.43 0.37 0.09 0.47 0.59 0.78 0.83 0.85 0.21 0.95 0.47 0.87 0.43 0.95 0.18 0.13 0.95 0.79 0.62 0.02 0.79 0.28 0.87 0.71 0.13 0.53 0.02 0.73 0.6 0.13 0.75 0.07 0.02 0.34 0.58 0.55 0.4 0.42 0.46 0.43 0.98 0.86 0.31 0.77 0.64 0.97 0.6 0.91 0.94 0.9 0.34 0.78 0.0 0.49 0.17 0.86 0.47 0.3 0.62 0.33 0.86 0.62 0.65 0.36 0.4 0.08 0.67 0.92 0.76 0.87 0.61 0.41 0.3 0.65 0.25 0.37 0.3 0.57 0.77 0.64 0.1 0.3 0.6 0.52 0.45 0.1 0.02 0.83 0.57 0.41 0.46 0.55 0.41 0.77 0.39 0.03 0.0 0.9 0.42 0.22 0.73 0.48 0.94 0.15 0.14 0.32 0.65 0.6 0.03 0.64 0.15 0.42 0.96 0.41 0.53 0.43 0.3 0.76 0.93 0.32 0.53 0.62 0.31 0.54 0.2 0.66 0.68 0.39 0.01 0.99 0.25 0.71 0.19 0.52 0.93 0.96 0.68 1.0 0.4 0.66 0.64 0.09 0.28 0.47 0.01 0.99 0.36 0.09 0.57 0.79 0.41 0.35 0.3 0.5 0.28 0.71 0.27 0.13 0.06 0.46 0.39 0.37 0.88 0.99 0.3 0.09 0.01 0.98 0.74 0.12 0.01 0.15 0.64 0.68 0.27 0.09 0.89 0.3 0.64 0.34 0.44 0.71 0.01 0.0 0.33 0.12 0.05 0.74 0.81 0.49 0.45 0.94 0.86 0.58 0.56 0.07 0.91 0.54 0.64 0.82 0.17 0.69 0.7 0.99 0.35 0.62 0.6 0.93 0.38 0.32 0.01 0.79 0.62 0.97 0.74 0.71 0.54 0.08 0.01 0.09 0.95 0.53 0.52 0.15 0.18 0.38 0.71 0.57 0.2 0.87 1.0 0.43 0.93 0.49 0.65 0.42 0.29 0.63 0.53 0.34 0.84 0.23 0.38 0.51 0.88 0.07 0.17 0.9 0.13 0.83 0.54 0.54 0.07 0.49 0.83 0.94 0.04 0.79 0.18 0.46 0.51 0.73 0.68 0.04 0.89 0.4 0.16 0.9 0.36 0.73 0.36 0.39 0.42 0.03 0.6 0.85 0.2 0.88 0.64 0.07 0.04 0.58 0.11 0.36 0.19 0.12 0.74 0.54 0.65 0.37 0.31 0.78 0.94 0.02 0.56 0.72 0.18 0.03 0.12 0.3 0.55 0.74 0.22 0.14 0.42 0.23 0.71 0.78 0.66 0.82 0.12 0.83 0.73 0.7 0.22 0.89 0.81 0.34 0.61 0.2 0.68 0.22 0.84 0.03 0.99 0.06 0.23 0.68 0.71 0.41 0.97 0.04 0.78 0.88 0.8 0.72 0.63 0.68 0.94 0.58 0.07 0.53 0.51 0.04 0.45 0.19 0.05 0.23 0.67 0.13 0.41 0.62 0.18 0.01 0.34 0.91 0.88 0.21 0.71 0.47 0.61 0.51 0.65 0.95 0.33 0.0 0.16 0.56 0.21 0.06 0.06 0.06 0.8 0.39 0.83 0.29 0.04 0.74 0.27 0.25 0.35 0.78 0.44 0.23 0.95 0.97 0.89 0.83 0.85 0.41 0.95 0.69 0.09 0.91 0.63 0.96 0.76 0.16 0.75 0.41 0.83 0.63 0.83 0.86 0.82 0.04 0.32 0.3 0.21 0.39 0.48 0.8 0.21 0.4 0.96 0.71 0.63 0.54 0.95 0.81 0.11 0.83 0.63 0.41 0.33 0.32 0.58 0.72 0.82 0.73 0.01 0.5 0.93 0.69 0.91 0.44 0.18 0.28 0.61 0.5 0.98 0.93 0.91 0.72 0.59 0.63 0.03 0.82 0.62 0.07 0.51 0.53 0.89 0.47 0.04 0.08 0.17 0.2 0.88 0.78 0.93 0.71 0.24 0.22 0.32 0.87 0.03 0.01 0.85 0.77 0.82 0.64 0.2 0.83 0.88 0.23 0.44 0.72 0.2 0.98 0.11 0.46 0.59 0.3 0.82 0.01 0.66 0.8 0.91 0.0 0.86 0.84 0.56 0.49 0.22 0.27 0.02 0.62 0.55 0.62 0.79 0.94 0.89 0.56 0.87 0.96 0.43 0.58 0.63 0.22 0.37 0.44 0.85 0.28 0.25 0.4 0.34 0.14 0.8 0.84 0.89 0.06 0.45 0.02 0.07 0.85 0.43 0.13 0.21 0.21 0.05 0.23 0.85 0.44 0.8 0.52 0.39 0.65 0.67 0.64 0.79 0.3 0.01 0.3 0.11 0.02 0.96 0.05 0.44 0.06 0.01 0.77 0.19 0.06 0.31 0.48 0.97 0.64 0.92 0.76 0.07 0.77 0.95 0.98 0.63 0.25 0.27 0.76 0.96 0.24 0.18 0.8 0.0 0.96 0.24 0.52 0.59 0.65 0.17 0.32 0.55 0.59 0.62 0.82 0.59 0.29 0.42 0.12 0.24 0.02 0.66 0.59 0.78 0.37 0.19 0.96 0.18 0.2 0.99 0.76 0.58 0.35 0.54 0.89 0.14 0.58 0.1 0.97 0.38 0.82 0.48 0.06 0.83 1.0 0.99 0.77 0.41 0.08 0.87 0.75 0.13 0.52 0.58 0.68 0.03 0.92 0.55 0.04 0.56 0.63 0.28 0.8 0.39 0.68 0.58 0.01 0.23 0.28 0.98 0.96 0.05 0.28 0.44 0.31 0.91 0.81 0.18 0.65 0.53 0.02 0.41 0.98 0.09 0.12 0.84 0.6 0.17 0.2 0.58 0.35 0.25 0.74 0.83 0.55 0.18 0.8 0.33 0.04 0.56 0.85 0.22 0.83 0.48 0.53 0.54 0.51 0.06 0.76 0.1 0.43 0.21 0.46 0.97 0.48 0.77 0.11 0.36 0.9 0.52 0.06 0.23 0.8 0.09 0.11 0.57 0.59 0.76 0.44 0.15 0.46 0.07 0.86 0.01 0.49 0.05 0.54 0.14 0.29 0.01 0.81 0.45 0.45 0.12 0.82 0.47 0.93 0.51 0.04 0.26 0.14 0.5 0.06 0.25 0.62 0.95 0.07 0.28 0.32 0.03 0.28 0.45 0.86 0.24 0.22 0.78 0.63 0.4 0.33 0.56 0.26 0.41 0.63 0.73 0.73 0.35 0.44 0.67 0.03 0.07 0.68 0.86 0.35 0.58 0.75 0.16 0.37 0.87 0.66 0.59 0.67 0.46 0.64 0.78 0.97 0.45 0.98 0.64 0.41 0.58 0.51 0.97 0.95 0.9 0.34 0.1 0.76 0.37 0.05 0.57 0.72 0.91 0.4 0.43 0.78 0.78 0.39 0.3 0.21 0.88 0.36 0.54 0.87 0.84 0.19 0.22 0.89 0.89 0.85 0.77 0.86 0.46 0.5 0.88 0.18 0.4 0.61 0.07 0.06 0.65 0.05 0.31 0.55 0.87 0.05 0.54 0.28 0.28 0.35 0.1 0.55 0.82 0.86 0.12 0.17 0.69 0.74 0.13 0.08 0.6 0.4 0.97 0.32 0.81 0.14 0.97 0.65 0.72 0.32 0.57 0.69 0.74 0.65 0.75 0.37 0.88 0.97 0.88 0.7 0.98 0.36 0.1 0.35 0.15 0.23 0.09 0.3 1.0 0.21 0.99 0.44 0.23 0.21 0.15 0.43 0.77 0.17 0.32 0.55 0.8 0.08 0.72 0.49 0.31 0.39 0.48 0.29 0.78 0.64 0.04 0.11 0.69 0.76 0.9 0.79 0.32 0.03 0.68 0.67 0.35 0.55 0.01 0.03 0.22 0.31 0.3 0.28 0.14 0.01 0.73 0.86 0.67 0.06 0.45 0.32 0.78 0.22 0.84 0.19 0.29 0.8 0.61 0.23 0.71 0.94 0.04 0.86 0.87 0.88 0.65 0.04 0.93 0.1 0.73 0.38 0.88 0.8 0.54 0.62 0.2 0.76 0.66 0.46 0.0 0.32 0.38 0.92 0.85 0.84 0.9 0.85 0.08 0.32 0.98 0.57 0.72 0.48 0.86 0.23 1.0 0.56 0.48 0.13 0.61 0.46 0.38 0.58 0.06 0.95 0.37 0.94 0.11 0.44 0.53 0.26 0.98 0.67 0.28 0.65 0.28 0.48 0.52 0.58 0.01 0.1 0.03 0.29 0.14 0.33 0.5 0.98 0.99 0.68 0.28 0.12 0.6 0.65 0.77 0.69 0.66 0.5 0.76 0.79 0.79 0.64 0.67 0.35 0.78 0.71 0.47 0.5 0.79 0.69 0.13 0.18 0.89 0.29 0.79 0.92 0.54",	# str  in 'Gene expression target' Textbox component
		0.5,	# int | float (numeric value between 0.5 and 2) in 'Decoding temperature' Slider component
		5,	# int | float (numeric value between 5 and 400) in 'Maximal sequence length' Slider component
		1,	# int | float (numeric value between 1 and 50) in 'Number of samples' Slider component
		api_name="/predict"
)
print(result)