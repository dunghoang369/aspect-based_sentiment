import sys
sys.path.append("aste")
from pathlib import Path
from data_utils import Data, Sentence, SplitEnum
from wrapper import SpanModel

data_name = "14lap"
random_seed = 4
path_train = f"aste/data/triplet_data/{data_name}/train.txt"
path_dev = f"aste/data/triplet_data/{data_name}/dev.txt"
path_test = f"aste/data/triplet_data/{data_name}/test.txt"
save_dir = f"xlm_abs_15_max_span_width_data_modified"

model = SpanModel(save_dir=save_dir, random_seed=random_seed)
model.fit(path_train, path_dev)
