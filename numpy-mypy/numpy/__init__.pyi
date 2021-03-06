"""
Numpy's mypy stub. Only type declarations for ndarray, the scalar hierarchy and array creation
methods are provided.
"""

from typing import (Any, Callable, Dict, Generic, Iterator, List, Optional, Sequence, Tuple, Type,
                    TypeVar, Union, Sized, overload)
from numpy import random, linalg

class dtype: ...
_dtype = dtype


class flagsobj:
    """numpy.flagsobj"""
    aligned = None       # type: bool
    behaved = None       # type: bool
    c_contiguous = None  # type: bool
    carray = None        # type: bool
    contiguous = None    # type: bool
    f_contiguous = None  # type: bool
    farray = None        # type: bool
    fnc = None           # type: bool
    forc = None          # type: bool
    fortran = None       # type: bool
    owndata = None       # type: bool
    updateifcopy = None  # type: bool
    writeable = None     # type: bool
    def __getitem__(self, item: str) -> bool: ...
    def __setitem__(self, item: str, value: bool) -> None: ...

#
# Type variables. _T wasn't used to avoid confusions with ndarray's "T" attribute.
#

_S = TypeVar('_S')
_U = TypeVar('_U')
_V = TypeVar('_V')

#
# Auxiliary types
#

ShapeType = Union[int, Tuple[int, ...]]
AxesType = Union[int, Tuple[int, ...]]
OrderType = Union[str, Sequence[str]]
DtypeType = Union[dtype, type]
ArrayTypeAny = Union[_ArrayLike[Any], List[Any], Tuple[Any, ...]]
ArrayTypeFloat = Union[_ArrayLike[float], List[float], Tuple[float, ...]]

class flatiter(Generic[_S], Iterator[_S]):
    coords = ...  # type: ShapeType
    def copy(self) -> flatiter[_S]: ...


class _ArrayLike(Generic[_S]):
    """
    "array-like" interface that both numpy.ndarray and all scalars (descendants of numpy.generic)
    implement this interface.
    """
    #
    # Array-like structures attributes
    #
    T = None         # type: _ArrayLike[_S]
    data = None      # type: Any
    dtype = None     # type: _dtype
    flags = None     # type: flagsobj
    flat = None      # type: flatiter[_ArrayLike[_S]]
    imag = None      # type: _ArrayLike[_S]
    real = None      # type: _ArrayLike[_S]
    size = None      # type: int
    itemsize = None  # type: int
    nbytes = None    # type: int
    ndim = None      # type: int
    shape = None     # type: Tuple[int, ...]
    strides = None   # type: Tuple[int, ...]
    base = None      # type: Optional[_ArrayLike[_S]]

    #
    # Array-like methods
    #

    # Once this issue https://github.com/python/mypy/issues/1907 is resolved, most methods that
    # have an 'out' argument, will be implemented using overload instead of with a Union
    # result. mypy is smart enough to assign the proper type (_ArrayLike[_U]) when out is present
    # but it falls back to the union when it's not.
    def all(self, axis: AxesType=None, out: '_ArrayLike[_U]'=None,
            keepdims: bool=False) -> Union['_ArrayLike[_U]', '_ArrayLike[bool]']: ...

    def any(self, axis: AxesType=None, out: '_ArrayLike[_U]'=None,
            keepdims: bool=False) -> Union['_ArrayLike[_U]', '_ArrayLike[bool]']: ...

    def argmax(self, axis: int=None,
               out: '_ArrayLike[_U]'=None) -> Union['_ArrayLike[_U]', '_ArrayLike[int]']: ...

    def argmin(self, axis: int=None,
               out: '_ArrayLike[_U]'=None) -> Union['_ArrayLike[_U]', '_ArrayLike[int]']: ...

    def argpartition(self, kth: Union[int, Sequence[int]], axis: Optional[int]=-1,
                     kind: str='introselect', order: OrderType=None) -> '_ArrayLike[int]': ...

    def argsort(self, axis: int=None, kind: str='quicksort',
                order: OrderType=None) -> '_ArrayLike[int]': ...

    def astype(self, dtype: Any, order: str='K', casting: str='unsafe', subok: bool=True,
               copy: bool=False) -> '_ArrayLike[Any]': ...

    def byteswap(self, inplace: bool=False) -> '_ArrayLike[_S]': ...

    def choose(self, choices:Sequence['_ArrayLike[_V]'], out: '_ArrayLike[_U]'=None,
               mode: str='raise') ->  Union['_ArrayLike[_U]', '_ArrayLike[_V]']: ...

    def clip(self, a_min: Any, a_max: Any,
             out: '_ArrayLike[_U]'=None) -> Union['_ArrayLike[_S]', '_ArrayLike[_U]']: ...

    def compress(self, condition: Sequence[bool], axis: int=None,
                 out: '_ArrayLike[_U]'=None) -> Union['_ArrayLike[_S]', '_ArrayLike[_U]']: ...

    def conj(self) -> '_ArrayLike[_S]': ...

    def conjugate(self) -> '_ArrayLike[_S]': ...

    def copy(self, order: str='C') -> '_ArrayLike[_S]': ...

    def cumprod(self, axis: int=None, dtype: Any=None,
                out: '_ArrayLike[Any]'=None) -> '_ArrayLike[Any]': ...

    def cumsum(self, axis: int=None, dtype: DtypeType=None,
                out: '_ArrayLike[Any]'=None) -> '_ArrayLike[Any]': ...

    def diagonal(self, offset: int=0, axis1: int=0, axis2: int=1) -> '_ArrayLike[_S]': ...

    def dot(self, b: '_ArrayLike[Any]', out: '_ArrayLike[Any]'=None) -> '_ArrayLike[Any]': ...

    def dump(self, file: str) -> None: ...

    def dumps(self) -> str: ...

    def flatten(self, order: str='C') -> '_ArrayLike[Any]': ...

    def fill(self, value: _S) -> None: ...

    def getfield(self, dtype: DtypeType, offset: int=0) -> '_ArrayLike[Any]': ...

    def item(self, args: AxesType) -> generic: ...

    def itemset(self, arg0: Union[int, Tuple[int, ...]], arg1: Any=None) -> None: ...

    def max(self, axis: AxesType=None,
            out: '_ArrayLike[_U]'=None) -> Union['_ArrayLike[_S]', '_ArrayLike[_U]']: ...

    def mean(self, axis: AxesType=None, dtype: Any=None,
             out: '_ArrayLike[_U]'=None, keepdims: bool=False) -> '_ArrayLike[floating]': ...

    def min(self, axis: AxesType=None,
            out: '_ArrayLike[_U]'=None) -> Union['_ArrayLike[_S]', '_ArrayLike[_U]']: ...

    def newbyteorder(self, new_order: str='S') -> '_ArrayLike[_S]': ...

    def nonzero(self) -> '_ArrayLike[int]': ...

    def partition(self, kth: AxesType, axis: int=-1, kind: str='introselect',
                  order: OrderType=None) -> None: ...

    def prod(self, axis: AxesType=None, dtype: DtypeType=None,
             out: '_ArrayLike[_U]'=None, keepdims: bool=False) -> '_ArrayLike[Any]': ...

    def ptp(self, axis: int=None,
            out: '_ArrayLike[_U]'=None) -> Union['_ArrayLike[_S]', '_ArrayLike[_U]']: ...

    def put(self, ind: '_ArrayLike[int]', v: '_ArrayLike[_S]', mode: str='raise') -> None: ...

    def ravel(self, order: str='C') -> '_ArrayLike[_S]': ...

    def repeat(self, repeats: Union[int, Sequence[int]],
               axis: int=None) -> '_ArrayLike[_S]': ...

    def reshape(self, newshape: ShapeType,
                order: str='C') -> '_ArrayLike[_S]': ...

    def resize(self, new_shape: ShapeType, refcheck: bool=True) -> None: ...

    def round(self, decimals: int=0,
              out: '_ArrayLike[_U]'=None) -> Union['_ArrayLike[_S]', '_ArrayLike[_U]']: ...

    def searchsorted(self, v: Union[_S, '_ArrayLike[_S]'], side: str='left',
                     sorter: '_ArrayLike[int]'=None) -> '_ArrayLike[int]': ...

    def setfield(self, val: Any, dtype: DtypeType, offset: int=0) -> None: ...

    def setflags(self, write: bool=None, align: bool=None,
                 uic: bool=None) -> None: ...

    def sort(self, axis: int=-1, kind: str='quicksort', order: OrderType=None) -> None: ...

    def squeeze(self, axis: AxesType=None) -> '_ArrayLike[_S]': ...

    def std(self, axis: AxesType=None, dtype: DtypeType=None,
            out: '_ArrayLike[_U]'=None, ddof: int=0, keepdims: bool=False) -> '_ArrayLike[floating]': ...

    def sum(self, axis: AxesType=None, dtype: DtypeType=None,
            out: '_ArrayLike[_U]'=None,
            keepdims: bool=False) -> '_ArrayLike[Any]': ...

    def swapaxes(self, axis1: int, axis2: int) -> '_ArrayLike[_S]': ...

    def take(self, indices: Sequence[int], axis: int=None,
             out: '_ArrayLike[_U]'=None,
             mode: str='raise') -> Union['_ArrayLike[_S]', '_ArrayLike[_U]']: ...

    def tobytes(self, order: str='C') -> bytes: ...

    def tofile(self, fid: object, sep: str='',  # TODO fix fid definition (There's a bug in mypy io's namespace https://github.com/python/mypy/issues/1462)
               format: str='%s') -> None: ...

    def tolist(self) -> List[Any]: ...

    def tostring(self, order: str='C') -> bytes: ...

    def trace(self, offset: int=0, axis1: int=0, axis2: int=1,
              dtype: DtypeType=None, out: '_ArrayLike[_U]'=None) -> '_ArrayLike[Any]': ...

    def transpose(self, axes: AxesType=None) -> '_ArrayLike[_S]': ...

    def var(self, axis: AxesType=None, dtype: DtypeType=None,
            out: '_ArrayLike[_U]'=None, ddof: int=0, keepdims: bool=False) -> '_ArrayLike[Any]': ...

    def view(self, dtype: Union[DtypeType, Type['ndarray']]=None,
             type: type=None) -> '_ArrayLike[Any]': ...

    #
    # Magic methods
    #

    def __abs__(self) -> '_ArrayLike[_S]': ...

    def __add__(self, value: object) -> '_ArrayLike[Any]': ...

    def __and__(self, value: object) -> '_ArrayLike[int]': ...

    def __array__(self, dtype: DtypeType=None) -> '_ArrayLike[Any]': ...

    def __array_prepare__(self, context: object=None) -> '_ArrayLike[Any]': ...

    def __array_wrap__(self, context: object=None) -> '_ArrayLike[Any]': ...

    def __bool__(self) -> bool: ...

    def __complex__(self) -> complex: ...

    def __contains__(self, key: object) -> bool: ...

    def __copy__(self) -> '_ArrayLike[_S]': ...

    def __deepcopy__(self) -> '_ArrayLike[_S]': ...

    def __delattr__(self, name: str) -> None: ...

    def __delitem__(self, key: str) -> None: ...

    def __dir__(self) -> List[str]: ...

    def __divmod__(self, value: object) -> Tuple['_ArrayLike[int]', '_ArrayLike[float]']: ...

    def __eq__(self, value: object) -> '_ArrayLike[bool]': ...  # type: ignore

    def __float__(self) -> float: ...

    def __floordiv__(self, value: object) -> '_ArrayLike[int]': ...

    def __ge__(self, value: object) -> '_ArrayLike[bool]': ...

    def __getattribute__(self, name: str) -> Any: ...

    def __getitem__(self, key: Any) -> '_ArrayLike[_S]': ...

    def __gt__(self, value: object) -> '_ArrayLike[bool]': ...

    def __iadd__(self, value: object) -> None: ...

    def __iand__(self, value: object) -> None: ...

    def __ifloordiv__(self, value: object) -> None: ...

    def __ilshift__(self, value: object) -> None: ...

    def __imatmul__(self, value: '_ArrayLike[Any]') -> None: ...

    def __imod__(self, value: object) -> None: ...

    def __imul__(self, value: object) -> None: ...

    def __index__(self) -> int: ...

    def __int__(self) -> int: ...

    def __invert__(self) -> '_ArrayLike[_S]': ...

    def __ior__(self, value: object) -> None: ...

    def __ipow__(self, value: object) -> None: ...

    def __irshift__(self, value: object) -> None: ...

    def __isub__(self, value: object) -> None: ...

    def __iter__(self) -> Iterator['_ArrayLike[_S]']: ...

    def __itruediv__(sel, value: object) -> None: ...

    def __ixor__(self, value: object) -> None: ...

    def __le__(self, value: object) -> '_ArrayLike[bool]': ...

    def __len__(self) -> int: ...

    def __lshift__(self, value: object) -> '_ArrayLike[_S]': ...

    def __lt__(self, value: object) -> '_ArrayLike[bool]': ...

    def __matmul__(self, value: '_ArrayLike[Any]') -> '_ArrayLike[Any]': ...

    def __mod__(self, value: object) -> '_ArrayLike[_S]': ...

    def __mul__(self, value: object) -> '_ArrayLike[Any]': ...

    def __ne__(self, value: object) -> '_ArrayLike[bool]': ...  # type: ignore

    def __neg__(self) -> '_ArrayLike[_S]': ...

    def __or__(self, value: object) -> '_ArrayLike[_S]': ...

    def __pos__(self) -> '_ArrayLike[_S]': ...

    def __pow__(self, value: object) -> '_ArrayLike[Any]': ...

    def __radd__(self, value: object) -> '_ArrayLike[Any]': ...

    def __rand__(self, value: object) -> '_ArrayLike[_S]': ...

    def __rdivmod__(self, value: object) -> Tuple['_ArrayLike[int]', '_ArrayLike[float]']: ...

    def __rfloordiv__(self, value: object) -> '_ArrayLike[Any]': ...

    def __rlshift__(self, value: object) -> '_ArrayLike[Any]': ...

    def __rmatmul__(self, value: object) -> '_ArrayLike[Any]': ...

    def __rmod__(self, value: object) -> '_ArrayLike[Any]': ...

    def __rmul__(self, value: object) -> '_ArrayLike[Any]': ...

    def __ror__(self, value: object) -> '_ArrayLike[_S]': ...

    def __rpow__(self, value: object) -> '_ArrayLike[Any]': ...

    def __rrshift__(self, value: object) -> '_ArrayLike[Any]': ...

    def __rshift__(self, value: object) -> '_ArrayLike[Any]': ...

    def __rsub__(self, value: object) -> '_ArrayLike[Any]': ...

    def __rtruediv__(self, value: object) -> '_ArrayLike[Any]': ...

    def __rxor__(self, value: object) -> '_ArrayLike[_S]': ...

    def __setattr__(self, name: str, value: Any) -> None: ...

    def __setitem__(self, key: Any, value: Any) -> None: ...

    def __str__(self) -> str: ...

    def __sub__(self, value: object) -> '_ArrayLike[Any]': ...

    def __truediv__(sel, value: object) -> '_ArrayLike[Any]': ...

    def __xor__(self, value: object) -> '_ArrayLike[_S]': ...

#
# numpy's scalar hierarchy (http://docs.scipy.org/doc/numpy/reference/arrays.scalars.html#scalars)
#

class generic(_ArrayLike[_S], Generic[_S]): ...
class bool_(generic[bool]):
    def __init__(self, value : Any = None) -> None: ...
bool8 = bool_
class object_(generic[Any]):
    def __init__(self, value : Any = None) -> None: ...
class number(generic[_S], Generic[_S]): ...
class integer(number[int]): ...
class signedinteger(integer): ...
class byte(signedinteger):
    def __init__(self, value : Any = None) -> None: ...
class short(signedinteger):
    def __init__(self, value : Any = None) -> None: ...
class intc(signedinteger):
    def __init__(self, value : Any = None) -> None: ...
class int_(signedinteger):
    def __init__(self, value : Any = None) -> None: ...
class longlong(signedinteger):
    def __init__(self, value : Any = None) -> None: ...
class int8(signedinteger):
    def __init__(self, value : Any = None) -> None: ...
class int16(signedinteger):
    def __init__(self, value : Any = None) -> None: ...
class int32(signedinteger):
    def __init__(self, value : Any = None) -> None: ...
class int64(signedinteger):
    def __init__(self, value : Any = None) -> None: ...
class unsignedinteger(integer): ...
class ubyte(unsignedinteger):
    def __init__(self, value : Any = None) -> None: ...
class ushort(unsignedinteger):
    def __init__(self, value : Any = None) -> None: ...
class uintc(unsignedinteger):
    def __init__(self, value : Any = None) -> None: ...
class uint(unsignedinteger):
    def __init__(self, value : Any = None) -> None: ...
class ulonglong(unsignedinteger):
    def __init__(self, value : Any = None) -> None: ...
class uint8(signedinteger):
    def __init__(self, value : Any = None) -> None: ...
class uint16(signedinteger):
    def __init__(self, value : Any = None) -> None: ...
class uint32(signedinteger):
    def __init__(self, value : Any = None) -> None: ...
class uint64(signedinteger):
    def __init__(self, value : Any = None) -> None: ...
class inexact(number[float]): ...
class floating(inexact): ...
class half(floating):
    def __init__(self, value : Any = None) -> None: ...
class single(floating):
    def __init__(self, value : Any = None) -> None: ...
class float_(floating):
    def __init__(self, value : Any = None) -> None: ...
class longfloat(floating):
    def __init__(self, value : Any = None) -> None: ...
class float16(floating):
    def __init__(self, value : Any = None) -> None: ...
class float32(floating):
    def __init__(self, value : Any = None) -> None: ...
class float64(floating):
    def __init__(self, value : Any = None) -> None: ...
class float128(floating):
    def __init__(self, value : Any = None) -> None: ...
class complexfloating(inexact): ...
class csingle(complexfloating):
    def __init__(self, value : Any = None) -> None: ...
class complex_(complexfloating):
    def __init__(self, value : Any = None) -> None: ...
class clongfloat(complexfloating):
    def __init__(self, value : Any = None) -> None: ...
class complex64(complexfloating):
    def __init__(self, value : Any = None) -> None: ...
class complex128(complexfloating):
    def __init__(self, value : Any = None) -> None: ...
class complex256(complexfloating):
    def __init__(self, value : Any = None) -> None: ...
class flexible(generic[_S], Generic[_S]): ...
class character(flexible[str]): ...
class str_(character):
    def __init__(self, value : Any = None) -> None: ...
class unicode_(character):
    def __init__(self, value : Any = None) -> None: ...
class void(flexible[None]):
    def __init__(self, value : Any) -> None: ...


class ndarray(_ArrayLike[_S], Generic[_S], Sized):
    """numpy.ndarray"""
    ctypes = None    # type: Any  # TODO Implement ctypes type hint

    # TODO Need to find a way to restrict buffer type
    def __init__(self, shape: Tuple[int, ...], dtype: DtypeType=None,
                 buffer: Any=None, offset: int=None,
                 strides: Tuple[int, ...]=None, order: str=None) -> None: ...

    # repeat ArrayLike magic method for proper type
    def __add__(self, value: object) -> 'ndarray[Any]': ...
    def __sub__(self, value: object) -> 'ndarray[Any]': ...
    def __mul__(self, value: object) -> 'ndarray[Any]': ...
    def __matmul__(self, value: '_ArrayLike[Any]') -> 'ndarray[Any]': ...
    def __array__(self, dtype: DtypeType=None) -> 'ndarray[Any]': ...
    #def __getitem__(self, key: Any) -> _S: ...
    #def __getslice__(self, i: Any, j: Any) -> ndarray[_S]: ...
    def __getitem__(self, key: Any) -> ndarray[_S]: ...
    def __copy__(self) -> 'ndarray[_S]': ...
    def __iter__(self) -> Iterator['ndarray[_S]']: ...
    def __pow__(self, value: object) -> 'ndarray[Any]': ...
    def __pos__(self) -> 'ndarray[_S]': ...
    def __neg__(self) -> 'ndarray[_S]': ...
    def __ge__(self, value: object) -> 'ndarray[bool]': ...
    def __gt__(self, value: object) -> 'ndarray[bool]': ...
    def __le__(self, value: object) -> 'ndarray[bool]': ...
    def __lt__(self, value: object) -> 'ndarray[bool]': ...
    def __eq__(self, value: object) -> 'ndarray[bool]': ...  # type: ignore
    def __ne__(self, value: object) -> 'ndarray[bool]': ...  # type: ignore

    def copy(self, order: str='C') -> 'ndarray[_S]': ...
    def flatten(self, order: str='C') -> 'ndarray[Any]': ...
    def dot(self, b: '_ArrayLike[Any]', out: '_ArrayLike[Any]'=None) -> 'ndarray[Any]': ...
    def transpose(self, axes: AxesType=None) -> 'ndarray[_S]': ...
    def reshape(self, newshape: ShapeType, order: str='C') -> ndarray[_S]: ...


# global attributes
pi: float
inf: float
nan: float


# Array creation routines
def array(object: Any, dtype: Any=None, copy: bool=True,
          order: str=None, subok: bool=False,
          ndmin: int=0) -> ndarray[Any]: ...
def asarray(a: Any, dtype: DtypeType=None, order: str=None) -> ndarray[Any]: ...
def asfarray(a: Any, dtype: DtypeType=float64, order: str=None) -> ndarray[float]: ...
def asanyarray(a: Any, dtype: DtypeType=None, order: str=None) -> ndarray[Any]: ...  # TODO figure out a way to restrict the return type
def asmatrix(data: Any, dtype: DtypeType=None) -> matrix[Any]: ...
def ascontiguousarray(a: Any, dtype: DtypeType=None) -> ndarray[Any]: ...
def copy(a: Any, order: str=None) -> ndarray[Any]: ...
def empty(shape: ShapeType, dtype: DtypeType=float, order: str='C') -> ndarray[Any]: ...
def empty_like(a: Any, dtype: Any=None, order: str='K', subok: bool=True) -> ndarray[Any]: ...
def exp(self, dtype: DtypeType=None) -> ndarray[Any]: ...
def eye(N: int, M: int=None, k: int=0, dtype: DtypeType=float) -> ndarray[Any]: ...
def frombuffer(buffer: Any, dtype: DtypeType=float, count: int=-1,  # TODO figure out a way to restrict buffer
               offset: int=0) -> ndarray[Any]: ...
def fromfile(file: object, dtype: DtypeType=float, count: int=-1, sep: str='') -> ndarray[Any]: ...  # TODO fix file definition (There's a bug in mypy io's namespace https://github.com/python/mypy/issues/1462)
def full(shape: ShapeType, fill_value: Any, dtype: DtypeType=None,
         order: str='C') -> ndarray[Any]: ...
def full_like(a: Any, fill_value: Any, dtype: DtypeType=None, order: str='C',
              subok: bool=True) -> ndarray[Any]: ...
def fromfunction(function: Callable[..., _S], shape: ShapeType, dtype: DtypeType=float) -> ndarray[_S]: ...
def fromiter(iterable: Iterator[Any], dytpe: DtypeType, count: int=-1) -> ndarray[Any]: ...
def fromstring(string: str, dtype: DtypeType=float, count: int=-1, sep: str='') -> ndarray[Any]: ...
def identity(n: int, dtype: DtypeType=None) -> ndarray[Any]: ...
def loadtxt(fname: Any, dtype: DtypeType=float, comments: Union[str, Sequence[str]]='#',
            delimiter: str=None, converters: Dict[int, Callable[[Any], float]]=None,
            skiprows: int=0, usecols: Sequence[int]=None,
            unpack: bool=False, ndmin: int=0) -> ndarray[float]: ...
def ones(shape: ShapeType, dtype: Optional[DtypeType]=..., order: str='C') -> ndarray[Any]: ...
def ones_like(a: Any, dtype: Any=None, order: str='K', subok: bool=True) -> ndarray[Any]: ...
def zeros(shape: ShapeType, dtype: DtypeType=float, order: str='C') -> ndarray[Any]: ...
def zeros_like(a: Any, dtype: Any=None, order: str='K', subok: bool=True) -> ndarray[Any]: ...

# Global array routines (incomplete)

@overload
def abs(x: float, out: float=None) -> float: ...
@overload
def abs(x: _ArrayLike[complexfloating], out: ndarray[_U]=None) -> ndarray[float]: ...
def all(a: _ArrayLike[_S], axis: AxesType=None, out: '_ArrayLike[_U]'=None,
        keepdims: bool=False) -> Union['ndarray[_U]', 'ndarray[bool]']: ...
def argmax(a: _ArrayLike[_U], axis: int=None,
        out: ndarray[_U]=None) -> Union[ndarray[_U], ndarray[int]]: ...
def argmin(a: _ArrayLike[_U], axis: int=None,
        out: ndarray[_U]=None) -> Union[ndarray[_U], ndarray[int]]: ...
def argsort(a: _ArrayLike[Any], axis: int=None, kind: str='quicksort',
            order: OrderType=None) -> ndarray[int]: ...
def concatenate(s: Sequence[_ArrayLike[_S]], axis: AxesType=None) -> ndarray[_S]: ...
def copyto(dst: ndarray[Any], src: _ArrayLike[Any], caseting: str='same_kind',
           where: _ArrayLike[bool]=None) -> None: ...
def delete(arr: _ArrayLike[Any], obj: Union[int, Sequence[int]], axis: AxesType=None) -> ndarray[Any]: ...
@overload
def deg2rad(x: float, out: float=None) -> float: ...
@overload
def deg2rad(x: ArrayTypeFloat, out: ndarray[float]=None) -> ndarray[float]: ...
def diag(v: _ArrayLike[Any], k:int=None) -> ndarray[Any]: ...
def diff(a: ArrayTypeAny, n: int=1, axis: AxesType=-1) -> ndarray[Any]: ...
def dot(a: _ArrayLike[Any], b: _ArrayLike[Any], out: ndarray[Any]=None) -> ndarray[Any]: ...
def hstack(tup: Sequence[_ArrayLike[_S]]) -> ndarray[_S]: ...
def insert(arr: _ArrayLike[Any], obj: Union[int, Sequence[int]], values: Union[Any, _ArrayLike[Any]],
                axis: AxesType=None) -> ndarray[Any]: ...
def mean(a: ArrayTypeFloat, axis: AxesType=None, dtype: Any=None,
             out: ndarray[_U]=None, keepdims: bool=False) -> ndarray[float]: ...
def median(a: ArrayTypeFloat, axis: AxesType=None, out: ndarray[_U]=None,
           overwrite_input: bool=False, keepdims: bool=False) -> ndarray[float]: ...
def min(a: _ArrayLike[_U], axis: AxesType=None, out: ndarray[_U]=None) -> ndarray[_U]: ...
def max(a: _ArrayLike[_U], axis: AxesType=None, out: ndarray[_U]=None) -> ndarray[_U]: ...
def nan_to_num(x: _ArrayLike[Any]) -> ndarray[Any]: ...
def tile(A: _ArrayLike[_S], reps: Union[int, Sequence[int]]) -> ndarray[_S]: ...
@overload
def rad2deg(x: float, out: float=None) -> float: ...
@overload
def rad2deg(x: ArrayTypeFloat, out: ndarray[float]=None) -> ndarray[float]: ...
def reshape(a: _ArrayLike[_S], newshape: ShapeType, order: str='C') -> ndarray[Any]: ...
def repeat(a: _ArrayLike[_S], repeats: Union[int, Sequence[int]], axis: int=None) -> ndarray[_S]: ...
def squeeze(a: _ArrayLike[_S], axis: AxesType=None) -> ndarray[_S]: ...
@overload
def square(v: float, out: float=None) -> float: ...
@overload
def square(v: ArrayTypeAny, out: ndarray[_U]=None) -> ndarray[Any]: ...
@overload
def sqrt(x: float, out: float=None) -> float: ...
@overload
def sqrt(x: ArrayTypeFloat, out: ndarray[_U]=None) -> ndarray[float]: ...
def sum(a: ArrayTypeAny, axis: AxesType=None, dtype: DtypeType=None, out: ndarray[_U]=None,
            keepdims: bool=False) -> ndarray[Any]: ...
def trace(a: _ArrayLike[Any], offset: int=0, axis1: int=0, axis2: int=1,
          dtype: DtypeType=None, out: ndarray[_U]=None) -> ndarray[Any]: ...
def resize(a: _ArrayLike[_S], new_shape: ShapeType, refcheck: bool=True) -> None: ...
def vstack(tup: Sequence[_ArrayLike[_S]]) -> ndarray[_S]: ...
def where(condition: _ArrayLike[Any], x: _ArrayLike[Any]=None, y: _ArrayLike[Any]=None) -> ndarray[Any]: ...

def save(file: Any, arr: _ArrayLike[Any], allow_pickle: bool=None, fix_imports: bool=None) -> None: ...
def savez(file: str, *args: Any, **kwargs: Any) -> None: ...
def savez_compressed(file: str, *args: Any, **kwargs: Any) -> None: ...
def savetxt(fname: Any, X: _ArrayLike[Any], fmt: Union[str, Sequence[str]]=None, delimiter: str=None,
            newline: str=None, header: str=None, footer: str=None, comments: str=None) -> None: ...
def load(file: Any, mmap_mode: str=None, allow_pickle: bool=None, fix_imports: bool=None,
         encoding: str='ASCII') -> Any: ...

def sin(x: _ArrayLike[Any], out: ndarray[Any]=None) -> ndarray[Any]: ...
def sinh(x: _ArrayLike[Any], out: ndarray[Any]=None) -> ndarray[Any]: ...
def arcsin(x: _ArrayLike[Any], out: ndarray[Any]=None) -> ndarray[Any]: ...
def cos(x: _ArrayLike[Any], out: ndarray[Any]=None) -> ndarray[Any]: ...
def arccos(x: _ArrayLike[Any], out: ndarray[Any]=None) -> ndarray[Any]: ...
def tan(x: _ArrayLike[Any], out: ndarray[Any]=None) -> ndarray[Any]: ...
def tanh(x: _ArrayLike[Any], out: ndarray[Any]=None) -> ndarray[Any]: ...
def arctan(x: _ArrayLike[Any], out: ndarray[Any]=None) -> ndarray[Any]: ...
def arctan2(x1: _ArrayLike[float], x2: _ArrayLike[float], out: ndarray[float]=None) -> ndarray[float]: ...

def unwrap(p: _ArrayLike[float], discont: float=3.141592653589793, axis:AxesType=-1) -> ndarray[float]: ...
def imag(val: _ArrayLike[Any]) -> ndarray[Any]: ...
def real(val: _ArrayLike[Any]) -> ndarray[Any]: ...

def gradient(f: _ArrayLike[Any], *args: Any, edge_order: int=1, axis: AxesType=None) -> ndarray[float]: ...
def std(a: _ArrayLike[float], axis: AxesType=None, dtype: DtypeType=None,
        out: _ArrayLike[_U]=None, ddof: int=0, keepdims: bool=False) -> _ArrayLike[floating]: ...
def var(a: _ArrayLike[float], axis: AxesType=None, dtype: DtypeType=None,
        out: _ArrayLike[_U]=None, ddof: int=0, keepdims: bool=False) -> _ArrayLike[Any]: ...

class matrix(_ArrayLike[_S], Generic[_S]):
    """numpy.matrix"""
    ctypes = None    # type: Any

    T = None   # type: matrix[_S]

    def __init__(self, data: Any, dtype: DtypeType=None,
                 copy: bool=None) -> None: ...

    def transpose(self, axes: AxesType=None) -> matrix[_S]: ...
