import os
import pandas as pd

# -----------------------------
# Step 1: Define the dMRI folder
# -----------------------------
dmri_folder = "/Bulk/Brain MRI/Diffusion MRI/"

# -----------------------------
# Step 2: Walk the folder tree and find all .zip files
# -----------------------------
dmri_filepaths = []
for root, dirs, files in os.walk(dmri_folder):
    for file in files:
        if file.endswith(".zip"):
            dmri_filepaths.append(os.path.join(root, file))

# -----------------------------
# Step 3: Parse filenames to extract eid, field_id, instance
# -----------------------------
manifest_data = []
for fp in dmri_filepaths:
    filename = os.path.basename(fp).replace(".zip", "")
    try:
        eid, field_id, instance, _ = filename.split("_")
    except ValueError:
        # Skip files that don't follow the standard naming convention
        continue
    manifest_data.append({
        "filepath": fp,
        "param": "Diffusion MRI",
        "eid": eid,
        "field_id": field_id,
        "ins": instance
    })

# -----------------------------
# Step 4: Save manifest as CSV
# -----------------------------
df_manifest = pd.DataFrame(manifest_data)
output_csv = "dmri_manifest.csv"
df_manifest.to_csv(output_csv, index=False)

print(f"Manifest generated: {output_csv}")
print(df_manifest.head())
