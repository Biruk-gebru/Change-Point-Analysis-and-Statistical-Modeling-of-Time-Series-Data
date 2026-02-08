
import json
import os

notebook_path = '/home/karanos/kiam/week11/prod/notebooks/03_volatility_forecasting.ipynb'

def patch_notebook():
    if not os.path.exists(notebook_path):
        print(f"Error: Notebook not found at {notebook_path}")
        return

    with open(notebook_path, 'r') as f:
        nb = json.load(f)

    modified = False
    
    target_line_part = "s = pm.GaussianRandomWalk('s', sigma=sigma, shape=len(returns))"
    
    new_lines = [
        "    # Latent log volatility process (Gaussian Random Walk)\n",
        "    # Manual implementation to avoid PyTensor OverflowError\n",
        "    step_s = pm.Normal('step_s', 0.0, sigma=sigma, shape=len(returns))\n",
        "    s = pm.Deterministic('s', step_s.cumsum())\n"
    ]

    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            new_source = []
            cell_modified = False
            for line in cell['source']:
                if target_line_part in line:
                    # Found the line. Replace it.
                    # The original line might have indentation.
                    # usage in notebook was: "    s = pm.GaussianRandomWalk('s', sigma=sigma, shape=len(returns))\n"
                    # We can just insert the new lines.
                    
                    new_source.extend(new_lines)
                    cell_modified = True
                    modified = True
                elif "draws=1000" in line:
                    new_source.append(line.replace("draws=1000", "draws=500"))
                    cell_modified = True
                    modified = True
                elif "tune=1000" in line:
                    new_source.append(line.replace("tune=1000", "tune=500"))
                    cell_modified = True
                    modified = True
                else:
                    new_source.append(line)
            
            if cell_modified:
                cell['source'] = new_source

    if modified:
        with open(notebook_path, 'w') as f:
            json.dump(nb, f, indent=1)
        print("Successfully patched the notebook.")
    else:
        print("Target line not found. Notebook not modified.")

if __name__ == "__main__":
    patch_notebook()
