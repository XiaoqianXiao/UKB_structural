import pandas as pd
import os

with open("all_dmri_paths.txt") as f:
    paths = [line.strip() for line in f]

data = []
for p in paths:
    filename = os.path.basename(p).replace(".zip","")
    eid, field_id, instance, _ = filename.split("_")
    data.append({
        "filepath": p,
        "param": "Diffusion MRI",
        "eid": eid,
        "field_id": field_id,
        "ins": instance
    })

df = pd.DataFrame(data)
df.to_csv("dmri_manifest.csv", index=False)
