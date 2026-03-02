from decimal import Decimal
from enum import Enum as pyEnum
from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Numeric, String, Integer, ForeignKey, Enum as SqlEnum, Text

from app.database.base import TimeBaseModel

if TYPE_CHECKING:
    from user import User
    from address import Address


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
    pass
