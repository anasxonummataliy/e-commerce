from decimal import Decimal
from enum import Enum as pyEnum
from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Numeric, String, Integer, ForeignKey, Enum as SqlEnum, Text

from app.database.base import TimeBaseModel

if TYPE_CHECKING:
    from user import User
    from address import Address
    from product import Product


class OrderStatus(pyEnum):
    pending = "pending"
    paid = "paid"
    shipped = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"


class PaymentStatus(pyEnum):
    pending = "pending"
    completed = "completed"
    failed = "failed"
    refunded = "refunded"


class Order(TimeBaseModel):
    __tablename__ = "orders"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    status: Mapped[OrderStatus] = mapped_column(
        SqlEnum(OrderStatus), default=OrderStatus.pending
    )
    total_price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    address_id: Mapped[int] = mapped_column(ForeignKey("addresses.id"), nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="orders")
    items: Mapped[list["OrderItem"]] = relationship("OrderItem", back_populates="order")
    address: Mapped["Address"] = relationship("Address", back_populates="orders")


class OrderItem(TimeBaseModel):
    __tablename__ = "order_items"

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    unit_price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    order: Mapped["Order"] = relationship("Order", back_populates="items")
    product: Mapped["Product"] = relationship("Product")


class Payment(TimeBaseModel):
    __tablename__ = "payments"

    order_id: Mapped[int] = mapped_column(
        ForeignKey("orders.id"), unique=True, nullable=False
    )
    stripe_payment_id: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    status: Mapped[PaymentStatus] = mapped_column(
        SqlEnum(PaymentStatus), default=PaymentStatus.pending
    )

    order: Mapped["Order"] = relationship("Order", back_populates="payment")
