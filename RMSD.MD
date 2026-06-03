# NeuroDynamics

### Computational Molecular Dynamics Framework for Protein–Ligand Stability Analysis

---

## Project Summary

NeuroDynamics is a terminal-driven molecular dynamics simulation framework developed to investigate the conformational stability, structural flexibility, and dynamic interactions of protein–ligand complexes associated with neurodegenerative disease targets.

The project integrates molecular docking, molecular dynamics simulations, and post-simulation trajectory analyses using GROMACS and a reproducible command-line workflow.

---

## Highlights

| Module                 | Function                                         |
| ---------------------- | ------------------------------------------------ |
| Protein Preparation    | Structure cleaning and preprocessing             |
| Ligand Preparation     | Ligand optimization and parameter generation     |
| Complex Assembly       | Protein–Ligand complex generation                |
| Topology Generation    | Force-field assignment and topology construction |
| Energy Minimization    | Removal of steric clashes                        |
| Equilibration          | NVT and NPT stabilization                        |
| Production MD          | Molecular dynamics simulations                   |
| RMSD Analysis          | Structural stability evaluation                  |
| RMSF Analysis          | Residue flexibility assessment                   |
| Radius of Gyration     | Compactness determination                        |
| Hydrogen Bond Analysis | Interaction stability monitoring                 |

---

## Computational Environment

| Software                    | Purpose                        |
| --------------------------- | ------------------------------ |
| GROMACS 2026.2              | Molecular Dynamics Simulations |
| AutoDock Vina               | Molecular Docking              |
| Miniconda                   | Environment Management         |
| PyMOL                       | Molecular Visualization        |
| Discovery Studio Visualizer | Interaction Analysis           |

---

## Scientific Workflow

Protein Preparation
↓
Ligand Preparation
↓
Molecular Docking
↓
Complex Construction
↓
Topology Generation
↓
Energy Minimization
↓
NVT Equilibration
↓
NPT Equilibration
↓
Production Molecular Dynamics
↓
Trajectory Processing
↓
RMSD • RMSF • Rg • H-Bond Analysis

---

## Terminal-Based Execution

The complete molecular dynamics workflow was executed using command-line GROMACS utilities within a Miniconda-managed computational environment.

### Core Commands

```bash
gmx pdb2gmx
gmx editconf
gmx solvate
gmx grompp
gmx genion
gmx mdrun
gmx rms
gmx rmsf
gmx gyrate
gmx hbond
```

---

## RMSD Analysis

Root Mean Square Deviation (RMSD) calculations were performed to evaluate the temporal stability of protein–ligand complexes throughout the simulation trajectory.

Stable RMSD profiles indicate preservation of structural integrity and sustained ligand binding, whereas large fluctuations may suggest conformational rearrangements within the system.

---

## RMSF Analysis

Root Mean Square Fluctuation (RMSF) analysis was used to identify flexible and rigid regions of the protein structure during simulation. Residue-level fluctuations provide insights into local mobility and dynamic behavior.

---

## Radius of Gyration

Radius of Gyration (Rg) measurements were calculated to assess structural compactness and global folding stability throughout the simulation period.

---

## Hydrogen Bond Analysis

Hydrogen bond occupancy and persistence were monitored to characterize the stability of protein–ligand interactions and evaluate binding retention during molecular dynamics simulations.

---

## Repository Layout

```text
proteins/
ligands/
complexes/
scripts/
results/
images/
```

---

## Research Applications

* Neurodegenerative Disease Research
* Structure-Based Drug Design
* Computational Pharmacology
* Drug Discovery
* Bioinformatics
* Molecular Modeling
* Computer-Aided Drug Design

---

## Author

Rituraj Kumar

Research Interests:
Computational Biology • Molecular Dynamics Simulation • Molecular Docking • Drug Discovery • Bioinformatics • Pharmacology

---

## License

MIT License
