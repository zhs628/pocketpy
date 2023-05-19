from typing import overload

class vec2:
    x: float
    y: float

    def __init__(self, x: float, y: float) -> None: ...
    def copy(self) -> vec2: ...
    def __add__(self, other: vec2) -> vec2: ...
    def __sub__(self, other: vec2) -> vec2: ...
    def __mul__(self, other: float) -> vec2: ...
    def __truediv__(self, other: float) -> vec2: ...
    def dot(self, other: vec2) -> float: ...
    def cross(self, other: vec2) -> float: ...
    def length(self) -> float: ...
    def length_squared(self) -> float: ...
    def normalize(self) -> vec2: ...
    def rotate(self, radians: float) -> vec2: ...

class vec3:
    x: float
    y: float
    z: float

    def __init__(self, x: float, y: float, z: float) -> None: ...
    def copy(self) -> vec3: ...
    def __add__(self, other: vec3) -> vec3: ...
    def __sub__(self, other: vec3) -> vec3: ...
    def __mul__(self, other: float) -> vec3: ...
    def __truediv__(self, other: float) -> vec3: ...
    def dot(self, other: vec3) -> float: ...
    def cross(self, other: vec3) -> float: ...
    def length(self) -> float: ...
    def length_squared(self) -> float: ...
    def normalize(self) -> vec3: ...

class mat3x3:
    _11: float
    _12: float
    _13: float
    _21: float
    _22: float
    _23: float
    _31: float
    _32: float
    _33: float

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, _11, _12, _13, _21, _22, _23, _31, _32, _33) -> None: ...
    @overload
    def __init__(self, a: list[list]): ...

    def set_zeros(self) -> None: ...
    def set_ones(self) -> None: ...
    def set_identity(self) -> None: ...

    def copy(self) -> mat3x3: ...
    def __getitem__(self, index: tuple[int, int]) -> float: ...
    def __setitem__(self, index: tuple[int, int], value: float) -> None: ...
    def __add__(self, other: mat3x3) -> mat3x3: ...
    def __sub__(self, other: mat3x3) -> mat3x3: ...
    def __mul__(self, other: float) -> mat3x3: ...
    def __truediv__(self, other: float) -> mat3x3: ...
    @overload
    def __matmul__(self, other: mat3x3) -> mat3x3: ...
    @overload
    def __matmul__(self, other: vec3) -> vec3: ...
    @overload
    def matmul(self, other: mat3x3) -> mat3x3: ...
    @overload
    def matmul(self, other: vec3) -> vec3: ...
    def determinant(self) -> float: ...
    def transpose(self) -> mat3x3: ...
    def inverse(self) -> mat3x3: ...

    @staticmethod
    def zeros() -> mat3x3: ...
    @staticmethod
    def ones() -> mat3x3: ...
    @staticmethod
    def identity() -> mat3x3: ...

    # affine transformations
    @staticmethod
    def trs(t: vec2, r: float, s: vec2) -> mat3x3: ...

    def is_affine(self) -> bool: ...
    def inverse_affine(self) -> mat3x3: ...
    def matmul_affine(self, other: mat3x3) -> mat3x3: ...

    def translation(self) -> vec2: ...
    def rotation(self) -> float: ...
    def scale(self) -> vec2: ...

    def transform_point(self, p: vec2) -> vec2: ...
    def transform_vector(self, v: vec2) -> vec2: ...
