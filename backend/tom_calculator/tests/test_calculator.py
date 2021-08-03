from decimal import Decimal, getcontext

from ward import fixture, test

from tom_calculator.calculator.logic import Calculator


@fixture
def taxes():
    yield {
        "UT": Decimal("0.0685"),
        "NV": Decimal("0.08"),
        "TX": Decimal("0.0625"),
        "AL": Decimal("0.04"),
        "CA": Decimal("0.0825"),
    }


@fixture
def discounts():
    yield {
        Decimal("1000"): Decimal("0.03"),
        Decimal("5000"): Decimal("0.05"),
        Decimal("7000"): Decimal("0.07"),
        Decimal("10000"): Decimal("0.1"),
        Decimal("50000"): Decimal("0.15"),
    }


for qt, pr, res in [
    (Decimal("3"), Decimal("3003.40"), Decimal("630.714")),
    (Decimal("5"), Decimal("10000"), Decimal("7500")),
    (Decimal("3.5"), Decimal("9000"), Decimal("3150")),
]:
    @test("test discount calculation")
    def _(
        discounts=discounts,
        taxes=taxes,
        quantity=qt,
        price=pr,
        result=res,
    ):
        calculator = Calculator(
            discounts=discounts,
            taxes=taxes,
            quantity=quantity,
            price=price,
            state_code="UT",
        )

        assert calculator.discount(quantity * price) == result


for qt, pr, sc, tax, total in [
    (Decimal("5"), Decimal("456"), "TX", Decimal("142.5"), Decimal("2349.83")),
    (Decimal("7"), Decimal("99"), "CA", Decimal("57.1725"), Decimal("750.17")),
    (Decimal("10"), Decimal("45.50"), "AL", Decimal("18.2"), Decimal("473.20")),
]:
    @test("test tax and total calculation")
    def _(
        discounts=discounts,
        taxes=taxes,
        quantity=qt,
        price=pr,
        state_code=sc,
        tax=tax,
        total=total,
    ):
        calculator = Calculator(
            discounts=discounts,
            taxes=taxes,
            quantity=quantity,
            price=price,
            state_code=state_code,
        )

        assert calculator.tax(quantity * price) == tax
        assert calculator.total().total == total
