
"""
NeuroDynamicsFlow

AI-Assisted Molecular Docking, Molecular Dynamics Simulation,
and Protein–Ligand Interaction Analysis Platform.

NeuroDynamicsFlow provides a complete computational workflow for:

* Protein structure loading and visualization
* Protein structure preparation and refinement
* Missing residue reconstruction and structural optimization
* Ligand preparation and molecular docking
* Protein–ligand complex generation
* Molecular dynamics simulation setup
* Trajectory processing and analysis
* RMSD, RMSF, Radius of Gyration, and Hydrogen Bond Analysis
* Reproducible command-line scientific computing workflows

Usage:

```
# Run the web interface
$ neurodynamicsflow

# or

$ python -m neurodynamicsflow

# Import in Python

from neurodynamicsflow.app import app
from neurodynamicsflow.structure_preparation import prepare_structure
```

Requirements:

```
- Python >= 3.11
- GROMACS
- AutoDock Vina
- Open Babel
- MDAnalysis
- Biopython
- NumPy
- Pandas
- Matplotlib
```

License: MIT
"""

version = "1.0.0"
author = "Rituraj Kumar"
email = "[riturajkumar14082002@gmail.com](mailto:riturajkumar14082002@gmail.com)"

# Expose key application components

from neurodynamicsflow.app import app

__all__ = ["app", "version"]