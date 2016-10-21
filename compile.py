from oddt.scoring.functions import rfscore
from compiledtrees import CompiledRegressionPredictor

r = rfscore.load('RFScoreVS_v2_vina_sklearn.pickle')
r.model = CompiledRegressionPredictor(r.model, n_jobs=-1)
r.score_title = 'RFScoreVS_v2'
pkl_file = 'RFScoreVS_v2_vina.pickle'
r.save(pkl_file)
