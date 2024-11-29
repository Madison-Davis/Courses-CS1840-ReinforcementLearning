"""Flexible Unit Structure Engine (FUSE)"""

from distutils.version import LooseVersion

import ase
import numpy
import spglib
import sklearn

from fuse_rl.assemble_structure import *
from fuse_rl.create_ml_model import *
from fuse_rl.create_random_instructions import *
from fuse_rl.create_random_string import *
from fuse_rl.error_check_structure import *
from fuse_rl.get_distances import *
from fuse_rl.gulp import *
from fuse_rl.make_basin_move import *
from fuse_rl.make_ga_move import *
from fuse_rl.plot_results import *
from fuse_rl.possible_solutions import *
from fuse_rl.run_fuse import *
from fuse_rl.run_gulp import *
from fuse_rl.run_vasp import *
from fuse_rl.compute_amd import *

__all__ = ['get_distances','assemble_structure','assemble_structure','return_factors','create_random_instructions',
'create_random_string','error_check_structure','read_gulp','read_gulp_out','write_gulp',
'make_basin_move','make_ga_move','plot_graph','cube_function','tetragonal_function','orthorhombic_function',
'possible_solutions','run_fuse','run_gulp','cellpar','run_vasp']

__version__ = '1.08'


if LooseVersion(np.__version__) < '1.9':
    # Make isinstance(x, numbers.Integral) work also for np.intxx:
    import numbers
    numbers.Integral.register(np.integer)
    del numbers
