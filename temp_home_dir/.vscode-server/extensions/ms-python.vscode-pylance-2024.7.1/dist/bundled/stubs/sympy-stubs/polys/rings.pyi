from types import NotImplementedType
from typing import Any, Iterator, Literal, Self
from typing_extensions import LiteralString

from sympy.core.sympify import CantSympify
from sympy.polys.compatibility import IPolys
from sympy.polys.domains.domainelement import DomainElement
from sympy.polys.fields import FracField
from sympy.printing.defaults import DefaultPrinting
from sympy.series.order import Order
from sympy.utilities import public

@public
def ring(symbols, domain, order=...) -> Any: ...
@public
def xring(symbols, domain, order=...) -> tuple[PolyRing | Any, Any]: ...
@public
def vring(symbols, domain, order=...) -> PolyRing | Any: ...
@public
def sring(exprs, *symbols, **options) -> tuple[PolyRing | Any, Any] | tuple[PolyRing | Any, list[Any]]: ...

_ring_cache: dict[Any, Any] = ...

class PolyRing(DefaultPrinting, IPolys):
    def __new__(cls, symbols, domain, order=...) -> Self | Any: ...
    def __getnewargs__(self) -> tuple[Any, Any, Any]: ...
    def __getstate__(self) -> dict[str, Any]: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def clone(self, symbols=..., domain=..., order=...) -> Self: ...
    def monomial_basis(self, i) -> tuple[Any, ...]: ...
    @property
    def zero(self): ...
    @property
    def one(self): ...
    def domain_new(self, element, orig_domain=...): ...
    def ground_new(self, coeff): ...
    def term_new(self, monom, coeff): ...
    def ring_new(self, element) -> PolyElement: ...

    __call__ = ...
    def from_dict(self, element, orig_domain=...): ...
    def from_terms(self, element, orig_domain=...): ...
    def from_list(self, element): ...
    def from_expr(self, expr): ...
    def index(self, gen) -> int: ...
    def drop(self, *gens) -> Self: ...
    def __getitem__(self, key) -> Self: ...
    def to_ground(self) -> Self: ...
    def to_domain(self) -> Any: ...
    def to_field(self) -> FracField | Any: ...
    @property
    def is_univariate(self) -> bool: ...
    @property
    def is_multivariate(self) -> bool: ...
    def add(self, *objs): ...
    def mul(self, *objs): ...
    def drop_to_ground(self, *gens) -> Self: ...
    def compose(self, other) -> Self: ...
    def add_gens(self, symbols) -> Self: ...
    def symmetric_poly(self, n): ...

class PolyElement(DomainElement, DefaultPrinting, CantSympify, dict):
    def new(self, init) -> Self: ...
    def parent(self): ...
    def __getnewargs__(self) -> tuple[Any, list[tuple[Any, Any]]]: ...

    _hash = ...
    def __hash__(self) -> int: ...
    def copy(self) -> Self: ...
    def set_ring(self, new_ring) -> Self: ...
    def as_expr(self, *symbols) -> Order: ...
    def as_expr_dict(self) -> dict[Any, Any]: ...
    def clear_denoms(self) -> tuple[Any, Self]: ...
    def strip_zero(self) -> None: ...
    def __eq__(p1, p2) -> bool: ...
    def __ne__(p1, p2) -> bool: ...
    def almosteq(p1, p2, tolerance=...) -> bool: ...
    def sort_key(self) -> tuple[int, list[Any]]: ...
    def __lt__(p1, p2) -> bool: ...
    def __le__(p1, p2) -> bool: ...
    def __gt__(p1, p2) -> bool: ...
    def __ge__(p1, p2) -> bool: ...
    def drop(self, gen): ...
    def drop_to_ground(self, gen): ...
    def to_dense(self) -> list[Any] | list[list[Any]]: ...
    def to_dict(self) -> dict[Any, Any]: ...
    def str(self, printer, precedence, exp_pattern, mul_symbol) -> LiteralString: ...
    @property
    def is_generator(self) -> bool: ...
    @property
    def is_ground(self) -> bool: ...
    @property
    def is_monomial(self) -> bool: ...
    @property
    def is_term(self) -> bool: ...
    @property
    def is_negative(self): ...
    @property
    def is_positive(self): ...
    @property
    def is_nonnegative(self): ...
    @property
    def is_nonpositive(self): ...
    @property
    def is_zero(f) -> bool: ...
    @property
    def is_one(f): ...
    @property
    def is_monic(f): ...
    @property
    def is_primitive(f): ...
    @property
    def is_linear(f) -> bool: ...
    @property
    def is_quadratic(f) -> bool: ...
    @property
    def is_squarefree(f) -> Literal[True]: ...
    @property
    def is_irreducible(f) -> Literal[True]: ...
    @property
    def is_cyclotomic(f): ...
    def __neg__(self) -> Self: ...
    def __pos__(self) -> Self: ...
    def __add__(p1, p2) -> Self | PolyElement | NotImplementedType: ...
    def __radd__(p1, n) -> Self | NotImplementedType: ...
    def __sub__(p1, p2) -> Self | NotImplementedType: ...
    def __rsub__(p1, n) -> NotImplementedType: ...
    def __mul__(p1, p2) -> NotImplementedType: ...
    def __rmul__(p1, p2) -> NotImplementedType: ...
    def __pow__(self, n) -> Self: ...
    def square(self): ...
    def __divmod__(p1, p2) -> tuple[Any, Any] | tuple[list[Any], Any] | NotImplementedType | tuple[Self, Self]: ...
    def __rdivmod__(p1, p2) -> NotImplementedType: ...
    def __mod__(p1, p2) -> NotImplementedType | Self: ...
    def __rmod__(p1, p2) -> NotImplementedType: ...
    def __truediv__(p1, p2) -> list[Any] | NotImplementedType | Self: ...
    def __rtruediv__(p1, p2) -> NotImplementedType: ...

    __floordiv__ = ...
    __rfloordiv__ = ...
    def div(self, fv) -> tuple[Any, Any] | tuple[list[Any], Any]: ...
    def rem(self, G): ...
    def quo(f, G) -> list[Any]: ...
    def exquo(f, G) -> list[Any]: ...
    def degree(f, x=...) -> Literal[0]: ...
    def degrees(f) -> tuple[Any, ...]: ...
    def tail_degree(f, x=...) -> Literal[0]: ...
    def tail_degrees(f) -> tuple[Any, ...]: ...
    def leading_expv(self) -> None: ...
    def coeff(self, element): ...
    def const(self): ...
    @property
    def LC(self): ...
    @property
    def LM(self): ...
    def leading_monom(self): ...
    @property
    def LT(self) -> tuple[Any, Any]: ...
    def leading_term(self): ...
    def coeffs(self, order=...) -> list[Any]: ...
    def monoms(self, order=...) -> list[Any]: ...
    def terms(self, order=...) -> list[Any]: ...
    def itercoeffs(self) -> Iterator[Any]: ...
    def itermonoms(self) -> Iterator[Any]: ...
    def iterterms(self) -> Iterator[tuple[Any, Any]]: ...
    def listcoeffs(self) -> list[Any]: ...
    def listmonoms(self) -> list[Any]: ...
    def listterms(self) -> list[tuple[Any, Any]]: ...
    def imul_num(p, c) -> Self | None: ...
    def content(f): ...
    def primitive(f) -> tuple[Any, Self]: ...
    def monic(f) -> Self: ...
    def mul_ground(f, x) -> Self: ...
    def mul_monom(f, monom) -> Self: ...
    def mul_term(f, term) -> Self: ...
    def quo_ground(f, x) -> Self: ...
    def quo_term(f, term) -> Self: ...
    def trunc_ground(f, p) -> Self: ...

    rem_ground = ...
    def extract_ground(self, g) -> tuple[Any, Self, Any]: ...
    def max_norm(f): ...
    def l1_norm(f) -> int: ...
    def deflate(f, *G) -> tuple[tuple[Any, ...], list[Self]] | tuple[tuple[Any, ...], list[Any]]: ...
    def inflate(f, J): ...
    def lcm(self, g): ...
    def gcd(f, g) -> Self: ...
    def cofactors(f, g) -> tuple[Any, Any, Any] | tuple[Self, Self, Self]: ...
    def cancel(self, g) -> tuple[Self, Any] | tuple[Any | Self | PolyElement, Any | Self | PolyElement]: ...
    def canonical_unit(f): ...
    def diff(f, x): ...
    def __call__(f, *values): ...
    def evaluate(self, x, a=...): ...
    def subs(self, x, a=...) -> Self: ...
    def symmetrize(self) -> tuple[Self, Any, list[Any]] | tuple[Any, Self | Any, list[tuple[Any, Any]]]: ...
    def compose(f, x, a=...): ...
    def pdiv(f, g): ...
    def prem(f, g): ...
    def pquo(f, g): ...
    def pexquo(f, g): ...
    def half_gcdex(f, g): ...
    def gcdex(f, g): ...
    def subresultants(f, g): ...
    def resultant(f, g): ...
    def discriminant(f): ...
    def decompose(f): ...
    def shift(f, a): ...
    def sturm(f): ...
    def gff_list(f): ...
    def sqf_norm(f): ...
    def sqf_part(f): ...
    def sqf_list(f, all=...): ...
    def factor_list(f): ...