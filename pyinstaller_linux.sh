#!/bin/bash
export CONDA_ROOT="$HOME/miniconda/envs/oddt_env/"

pyinstaller \
    --clean \
    --additional-hooks-dir=. \
    --hidden-import=six \
    --hidden-import=pybel \
    --hidden-import=sklearn.tree._utils \
    --hidden-import=sklearn.neighbors.typedefs \
    --hidden-import=compiledtrees \
    --exclude-module=tcl \
    --exclude-module=Tkinter \
    --exclude-module=rdkit \
    --add-data "./RFScoreVS_v2_vina.pickle:." \
    --add-data="${CONDA_ROOT}/share/openbabel/*/*:data/" \
    --add-binary="${CONDA_ROOT}/lib/openbabel/*/mdlformat.so:." \
    --add-binary="${CONDA_ROOT}/lib/openbabel/*/mol2format.so:." \
    --add-binary="${CONDA_ROOT}/lib/openbabel/*/pdbformat.so:." \
    --add-binary="${CONDA_ROOT}/lib/openbabel/*/pdbqtformat.so:." \
    --runtime-hook=pyi_rth_obdata.py \
    --nowindow \
    --strip \
    --add-binary "${CONDA_ROOT}/lib/libinchi.so.0:." \
    --add-binary "${CONDA_ROOT}/lib/libmkl_avx.so:." \
    --add-binary "${CONDA_ROOT}/lib/libmkl_avx2.so:." \
    -n rf-score-vs --onefile ./rf-score-vs
