# RF-Score-VS 1.0

RF-Score-VS is a novel Random Forest-based scoring function for Virtual Screening which predicts binding affinity.
Its descriptors are based on RF-Score developed by Pedro Ballester et. al.
Presented binary implements RF-Score-VS v2, meaning, it counts atoms of certain types within a 12A radius, devided into 2A bins.
Further information about reported performance in various scenarios and validation across datasets, see the publication in **[JACS submitted]**

## Supported platforms

* [Linux 64-bit](http://wojcikowski.pl/travis/rf-score-vs_v1.0_linux_2.7.zip)
* [Windows 64-bit](http://wojcikowski.pl/travis/rf-score-vs_v1.0_win_2.7.zip)
* [MacOS 64-bit](http://wojcikowski.pl/travis/rf-score-vs_v1.0_macos_2.7.zip)

## Supported multi-molecular formats:

* SDF/MDL (.sdf, .mol)
* Mol2 (.mol2)
* PDBQT (.pdbqt)
* PDB (.pdb)

## Usage instructions

#### Preparations
Download package appropriate for your platform, which contains the binary and sample data to test the RF-Score-VS.
To use the scoring function uncompress the archive and open a terminal in the same directory as the binary.

#### Basic parameters

* untagged parameters are treated as docked ligands;
user can supply multiple molecular files **[required]**
* `-i` input file format; if not present then based on extension
* `--receptor` a protein file; format based on extension **[required]**
* `-O` output file; if `-o` is not present file format is based on extension
* `-o` output file format; if `-O` is not present then molecules are printed to standard output


#### Rescoring
To rescore docked conformations simply run (on Windows omit the leading `./`):

`./rf-score-vs --receptor protein.pdb ligands.sdf -O ligands_rescored.sdf`

Producing CSV files (additional `--field` parameter to limit output columns):

`./rf-score-vs --receptor protein.pdb ligands.sdf -o csv --field "name" --field "RFScoreVS_v2"`

Running test data included with bundle:

`./rf-score-vs --receptor test/xiap/receptor_rdkit.pdb test/xiap/actives_docked.sdf -ocsv`

To get the list of all available parameters:

`./rf-score-vs --help`

**NOTE:** There is an expected overhead at the beginning of execution of RF-Score-VS binary due to setting up of temporary Python environment.

## Binary implementation details and licensing

* Single binary is obtained by freezing the Python script with [Pyinstaller](https://github.com/pyinstaller/pyinstaller)
* [Open Drug Discovery Toolkit](https://github.com/oddt/oddt) with OpenBabel
* Random forest trees are compiled using [sklearn-compiledtrees](https://github.com/ajtulloch/sklearn-compiledtrees) for extra performance

## Licensing
* Python environment and all dependencies are prepared using [Miniconda](http://conda.pydata.org/miniconda.html) with Intel MKL optimizations (see the [Miniconda LICENSE](http://conda.pydata.org/docs/license.html))
* All components provided here are covered by on permissive [3-clause BSD License](./LICENSE).

## References:

* Wójcikowski M, Ballester P.J, Siedlecki P. Performance of machine-learning scoring functions in structure-based virtual screening. JACS submitted

* Wójcikowski M, Zielenkiewicz P, Siedlecki P. Open Drug Discovery Toolkit (ODDT): a new open-source player in the drug discovery field. J Cheminform. 2015;7: 5317. [doi:10.1186/s13321-015-0078-2](https://dx.doi.org/10.1186/s13321-015-0078-2)

* Ballester PJ, Mitchell JBO. A machine learning approach to predicting protein-ligand binding affinity with applications to molecular docking. Bioinformatics. 2010;26: 1169–1175. [doi:10.1093/bioinformatics/btq112](https://dx.doi.org/10.1093/bioinformatics/btq112)

* Ballester PJ, Schreyer A, Blundell TL. Does a more precise chemical description of protein-ligand complexes lead to more accurate prediction of binding affinity? J Chem Inf Model. 2014;54: 944–955. [doi:10.1021/ci500091r](https://dx.doi.org/10.1021/ci500091r)

* Li H, Leung K-S, Wong M-H, Ballester PJ. Improving AutoDock Vina Using Random Forest: The Growing Accuracy of Binding Affinity Prediction by the Effective Exploitation of Larger Data Sets. Mol Inform. WILEY-VCH Verlag; 2015;34: 115–126. [doi:10.1002/minf.201400132](https://dx.doi.org/10.1002/minf.201400132)
