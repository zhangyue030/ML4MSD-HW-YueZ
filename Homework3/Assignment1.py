from pymatgen.core import Lattice, Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

def generate_perovskites(A: str, B: str, c_to_a_ratio: float, save_cifs: bool = True):
    a = 4.0
    cubic_lattice = Lattice.cubic(a)
    cubic_structure = Structure(
        cubic_lattice,
        [A, B, "O", "O", "O"],
        [
            [0, 0, 0],
            [0.5, 0.5, 0.5],
            [0.5, 0.5, 0],
            [0.5, 0, 0.5],
            [0, 0.5, 0.5],
        ],
    )

    c = a * c_to_a_ratio
    tetragonal_lattice = Lattice.tetragonal(a, c)
    tetragonal_structure = Structure(
        tetragonal_lattice,
        [A, B, "O", "O", "O"],
        [
            [0, 0, 0],
            [0.5, 0.5, 0.5],
            [0.5, 0.5, 0],
            [0.5, 0, 0.5],
            [0, 0.5, 0.5],
        ],
    )

    cubic_sg = SpacegroupAnalyzer(cubic_structure).get_space_group_symbol()
    tetragonal_sg = SpacegroupAnalyzer(tetragonal_structure).get_space_group_symbol()
    print(f"Cubic space group: {cubic_sg}")
    print(f"Tetragonal space group: {tetragonal_sg}")

    if save_cifs:
        cubic_structure.to(fmt="cif", filename=f"{A}{B}O3_cubic.cif")
        tetragonal_structure.to(fmt="cif", filename=f"{A}{B}O3_tetragonal.cif")

    return cubic_structure, tetragonal_structure


cperov, tperov = generate_perovskites("Ba", "Ti", 1.3)
print(cperov)
print(tperov)
