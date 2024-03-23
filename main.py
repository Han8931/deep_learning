import torch
import numpy as np

def set_random_seeds(seed):
    SEED = seed
    random.seed(SEED)
    np.random.seed(SEED)
    torch.manual_seed(SEED)
    torch.backends.cudnn.deterministic = True

if __name__ == "__main__":
    pass
