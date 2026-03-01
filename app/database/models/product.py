from decimal import Decimal
from typing import TYPE_CHECKING
from sqlalchemy import String, Text, Numeric, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import TimeBaseModel

if TYPE_CHECKING:
    from category import Category


class Product(TimeBaseModel):
    __tablename__ = "products"

    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    price: Mapped[Decimal] = mapped_column(Numeric, nullable=False)
    stock: Mapped[int] = mapped_column(Integer, default=0)
    image_url: Mapped[str | None] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    category_id: Mapped[int | None] = mapped_column(ForeignKey("categories.id"))

    category: Mapped["Category | None"] = relationship(
        "Category", back_populates="products"
    )
