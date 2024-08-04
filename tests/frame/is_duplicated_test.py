from __future__ import annotations

from typing import Any

import numpy as np

import narwhals.stable.v1 as nw


def test_is_duplicated(constructor_eager: Any) -> None:
    data = {"a": [1, 3, 2], "b": [4, 4, 6], "z": [7.0, 8, 9]}
    df_raw = constructor_eager(data)
    df = nw.from_native(df_raw, eager_only=True)
    result = nw.concat([df, df.head(1)]).is_duplicated()
    expected = np.array([True, False, False, True])
    assert (result.to_numpy() == expected).all()
