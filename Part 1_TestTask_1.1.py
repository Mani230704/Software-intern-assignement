from Part_1_Programming fundamentals import smooth


def test_basic_moving_average():
    assert smooth([1, 2, 3, 4, 5]) == [1.0, 1.5, 2.0, 2.5, 3.0]


def test_missing_values_are_forward_filled_and_smoothed():
    assert smooth([None, 10, 20, 30, 40], window=2) == [10.0, 10.0, 15.0, 25.0, 35.0]


def test_spike_is_replaced_by_previous_mean_when_outlier():
    assert smooth([5, 5, 5, 100, 5, 5], window=3) == [
        5.0,
        5.0,
        5.0,
        36.666666666666664,
        36.666666666666664,
        36.666666666666664,
    ]


def test_empty_input_returns_empty_list():
    assert smooth([], window=3) == []


def test_invalid_window_raises_value_error():
    try:
        smooth([1, 2], window=0)
        raise AssertionError("Expected ValueError for window < 1")
    except ValueError:
        pass
