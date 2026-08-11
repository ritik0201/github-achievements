import importlib.util, numpy
print('numpy file:', numpy.__file__)
print('spec:', importlib.util.find_spec('numpy._core'))
import numpy._core as nc
print('nc loaded', hasattr(nc,'__name__'))
