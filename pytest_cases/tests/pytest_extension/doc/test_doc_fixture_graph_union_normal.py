# Authors: Sylvain MARIE <sylvain.marie@se.com>
#          + All contributors to <https://github.com/smarie/python-pytest-cases>
#
# License: 3-clause BSD, <https://github.com/smarie/python-pytest-cases/blob/master/LICENSE>
from pytest_cases import fixture, parametrize


@fixture(autouse=True)
@parametrize(ie=[-1, 1])
def e(ie):
    return "e%s" % ie


@fixture
def d():
    return "d"


@fixture
def c():
    return "c"


@fixture
@parametrize(ia=[0, 1])
def a(c, d, ia):
    return "a%s" % ia + c + d


@parametrize(i2=['x', 'z'])
def test_2(a, i2):
    assert (a + i2) in ("a0cdx", "a0cdz", "a1cdx", "a1cdz")


@fixture
@parametrize(ib=['x', 'z'])
def b(a, c, ib):
    return "b%s" % ib + c + a


def test_1(a, b):
    assert a in ("a0cd", "a1cd")
    assert a == b[-4:]
    assert b[:-4] in ("bxc", "bzc")


@parametrize("e", [-1], indirect=True)
def test_synthesis_1(module_results_dct):
    assert list(module_results_dct) == [
        'test_2[ie=-1-ia=0-i2=x]',
        'test_2[ie=-1-ia=0-i2=z]',
        'test_2[ie=-1-ia=1-i2=x]',
        'test_2[ie=-1-ia=1-i2=z]',
        'test_2[ie=1-ia=0-i2=x]',
        'test_2[ie=1-ia=0-i2=z]',
        'test_2[ie=1-ia=1-i2=x]',
        'test_2[ie=1-ia=1-i2=z]',
        'test_1[ie=-1-ia=0-ib=x]',
        'test_1[ie=-1-ia=0-ib=z]',
        'test_1[ie=-1-ia=1-ib=x]',
        'test_1[ie=-1-ia=1-ib=z]',
        'test_1[ie=1-ia=0-ib=x]',
        'test_1[ie=1-ia=0-ib=z]',
        'test_1[ie=1-ia=1-ib=x]',
        'test_1[ie=1-ia=1-ib=z]'
    ]
