from pymol import cmd
import glob

targets = {
    "chainA_FMN": (15.564, 1.717, 1.876),
    "chainB_FMN": (22.517, 1.873, -26.863),
}

pocket_files = sorted(glob.glob("02_receptors/raw_pdb/azoR1_clean_out/pockets/pocket*_atm.pdb"))

for pf in pocket_files:
    name = pf.split("/")[-1]
    cmd.load(pf, "p")
    coords = cmd.get_coords("p")
    cx, cy, cz = coords.mean(axis=0)
    for label, (tx, ty, tz) in targets.items():
        dist = ((cx-tx)**2 + (cy-ty)**2 + (cz-tz)**2) ** 0.5
        if dist < 15:
            print(f"{name}: center=({cx:.2f},{cy:.2f},{cz:.2f})  distance to {label} = {dist:.2f} Å")
    cmd.delete("p")
