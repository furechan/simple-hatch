from simple_hatch import get_sample


def test_sample():
    assert get_sample()


def test_imports():
    import simple_hatch_mod
    import simple_hatch_bis
