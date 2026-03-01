from typing import TYPE_CHECKING
from sqlalchemy import String, BigInteger, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import TimeBaseModel

if TYPE_CHECKING:
    from product import Product


class Category(TimeBaseModel):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    parent_id: Mapped[int | None] = mapped_column(
        BigInteger, ForeignKey("categories.id")
    )

    parent: Mapped["Category | None"] = relationship(
        "Category", back_populates="children"
    )
    children: Mapped[list["Category"]] = relationship(
        "Category", back_populates="parent"
    )
    products: Mapped[list["Product"]] = relationship(
        "Product", back_populates="category"
    )
