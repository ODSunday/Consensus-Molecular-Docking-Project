from pymol import cmd

cmd.load("02_receptors/raw_pdb/azoR1_dimer.pdb", "azoR1")
cmd.load("02_receptors/raw_pdb/azoR1_4M0C_anchor.pdb", "anchor")

result = cmd.align("azoR1", "anchor")
print(f"ALIGN RESULT: RMSD={result[0]:.3f}  atoms_aligned={result[1]}  cycles={result[2]}")

coords = cmd.get_coords("anchor and resn FMN and chain A")
cx, cy, cz = coords.mean(axis=0)
print(f"BOX CENTRE: {cx:.3f} {cy:.3f} {cz:.3f}")

coords_B = cmd.get_coords("anchor and resn FMN and chain B")
cx2, cy2, cz2 = coords_B.mean(axis=0)
print(f"BOX CENTRE (chain B FMN): {cx2:.3f} {cy2:.3f} {cz2:.3f}")

cmd.remove("not polymer.protein")
cmd.save("02_receptors/raw_pdb/azoR1_clean.pdb", "azoR1")
print("Saved azoR1_clean.pdb")
