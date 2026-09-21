from pymol import cmd

cmd.load("02_receptors/raw_pdb/azoR1_clean.pdb", "azoR1")

# Get extent of the validated pocket (pocket3) to size the box
cmd.load("02_receptors/raw_pdb/azoR1_clean_out/pockets/pocket3_atm.pdb", "pocket3")
extent = cmd.get_extent("pocket3")
(xmin, ymin, zmin), (xmax, ymax, zmax) = extent
print(f"Pocket 3 extent: X {xmax-xmin:.1f}  Y {ymax-ymin:.1f}  Z {zmax-zmin:.1f}")
