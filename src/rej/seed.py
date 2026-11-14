import random

def seed_everything(seed: int = 0) -> None:
    """Make an experiment repeatable: same seed, same numbers."""
    random.seed(seed)
    try:
        import numpy as np
        np.random.seed(seed)
    except ImportError:
        pass
    try:
        import torch
        torch.manual_seed(seed)
    except ImportError:
        pass
