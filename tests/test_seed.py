import random
from rej.seed import seed_everything

def test_seed_is_repeatable():
    seed_everything(42); a = random.random()
    seed_everything(42); b = random.random()
    assert a == b
