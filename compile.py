from oddt.scoring.functions import rfscore
from compiledtrees import CompiledRegressionPredictor

import platform

if platform.system() == 'Windows':
    import win32file
    win32file._setmaxstdio(2048)
else:
    import resource
    if resource.getrlimit(resource.RLIMIT_NOFILE)[0] < 2048:
        resource.setrlimit(resource.RLIMIT_NOFILE,
                           (2048, resource.getrlimit(resource.RLIMIT_NOFILE)[1]))

r = rfscore.load('RFScoreVS_v2_vina_sklearn.pickle')
r.model = CompiledRegressionPredictor(r.model, n_jobs=-1)
r.score_title = 'RFScoreVS_v2'
pkl_file = 'RFScoreVS_v2_vina.pickle'
r.save(pkl_file)
