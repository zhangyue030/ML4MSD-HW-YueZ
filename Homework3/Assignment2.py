from mp_api.client import MPRester
import pandas as pd
import matplotlib.pyplot as plt

api_key = "G8Y1MEs8Cq5taybjmq7kKYdGYJOoOCA0"

with MPRester(api_key) as mpr:
    data = mpr.materials.summary.search(
        band_gap=(0, None),  
        is_metal=False,     
        fields=["material_id", "band_gap", "symmetry", "is_gap_direct"]
    )

flattened = [{k: v for k, v in d.dict().items() if v is not None} for d in data]
mpids = pd.DataFrame.from_records(flattened)
mpids["symmetry.crystal_system"] = mpids["symmetry"].apply(
    lambda x: str(x["crystal_system"]).lower() if isinstance(x, dict) and "crystal_system" in x else None
)
mpids = mpids.dropna(axis=1, how="all")
mpids = mpids.drop(columns=["symmetry", "fields_not_requested"], errors="ignore")
mpids.to_csv("mp_hw_data.csv")


total_counts = mpids["symmetry.crystal_system"].value_counts()
direct_counts = mpids[mpids["is_gap_direct"] == True]["symmetry.crystal_system"].value_counts()
percent_direct = (direct_counts / total_counts * 100).fillna(0)
percent_direct.plot(kind="bar", color="skyblue")
plt.ylabel("Percentage of Direct Band Gap (%)")
plt.title("Direct Band Gap Percentage by Crystal System")
plt.show()
avg_bandgap = mpids.groupby("is_gap_direct")["band_gap"].mean()
avg_bandgap.index = ["Indirect Band Gap", "Direct Band Gap"]
avg_bandgap.plot(kind="bar", color=["orange", "green"])
plt.ylabel("Average Band Gap (eV)")
plt.title("Average Band Gap: Direct vs Indirect")
plt.show()

#From Figure 1, the cubic crystal system exhibits the highest proportion of direct band gap materials,
#while triclinic and monoclinic systems show the lowest. 
#This indicates that higher crystal symmetry tends to favor direct band gap formation.
#From Figure 2, direct band gap materials show a slightly higher average band gap compared to indirect ones, 
# suggesting stronger optical transitions.
