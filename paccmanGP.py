from gradio_client import Client

client = Client("https://gt4sd-paccmann-gp.hf.space/")
result = client.predict(
		"fast-example-v1",	# str (Option from: [('fast-example-v1', 'fast-example-v1'), ('v0', 'v0'), ('v11', 'v11'), ('v12', 'v12'), ('v10', 'v10'), ('fast-example-v0', 'fast-example-v0')]) in 'Algorithm version' Dropdown component
		["qed"],	# List[str]  in 'Property goals' Checkboxgroup component
		"MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTT",	# str  in 'Protein target' Textbox component
		0.5,	# int | float (numeric value between 0.5 and 2) in 'Decoding temperature' Slider component
		5,	# int | float (numeric value between 5 and 400) in 'Maximal sequence length' Slider component
		1,	# int | float (numeric value between 1 and 50) in 'Number of samples' Slider component
		1,	# int | float (numeric value between 1 and 8) in 'Limit' Slider component
		1,	# int | float (numeric value between 1 and 32) in 'Number of steps' Slider component
		1,	# int | float (numeric value between 1 and 32) in 'Number of initial points' Slider component
		1,	# int | float (numeric value between 1 and 4) in 'Number of optimization rounds' Slider component
		0.01,	# int | float (numeric value between 0.01 and 1) in 'Sampling variance' Slider component
		1,	# int | float (numeric value between 1 and 10) in 'Samples used for evaluation' Slider component
		1,	# int | float (numeric value between 1 and 64) in 'Maximum number of sampling steps' Slider component
		5,	# int | float  in 'Seed' Number component
		api_name="/predict"
)
print(result)