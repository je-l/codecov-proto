from mypy_coverage_demo.main import another_typed


def test_another_typed_capitalizes():
    assert another_typed('abc') == 'A'
