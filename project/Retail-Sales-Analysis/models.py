from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    Numeric
)

from database import Base


class RetailSale(Base):

    __tablename__ = "retail_sales"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    order_id = Column(
        Integer
    )

    order_date = Column(
        Date
    )

    customer = Column(
        String(100)
    )

    gender = Column(
        String(20)
    )

    city = Column(
        String(100)
    )

    region = Column(
        String(50)
    )

    category = Column(
        String(100)
    )

    product = Column(
        String(100)
    )

    quantity = Column(
        Integer
    )

    unit_price = Column(
        Numeric(12, 2)
    )

    discount = Column(
        Numeric(5, 2)
    )

    sales_amount = Column(
        Numeric(14, 2)
    )