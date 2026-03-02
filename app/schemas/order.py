from decimal import Decimal
from enum import Enum
from pydantic import BaseModel
from app.schemas.product import ProductResponse


class OrderStatus(str, Enum):
    pending = "pending"
    paid = "paid"
    shipped = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"


class PaymentStatus(str, Enum):
    pending = "pending"
    completed = "completed"
    failed = "failed"
    refunded = "refunded"


class OrderCreate(BaseModel):
    address_id: int


class OrderItemResponse(BaseModel):
    id: int
    product: ProductResponse
    quantity: int
    unit_price: Decimal

    model_config = {"from_attributes": True}


class PaymentResponse(BaseModel):
    id: int
    stripe_payment_id: str
    amount: Decimal
    status: PaymentStatus

    model_config = {"from_attributes": True}


class OrderResponse(BaseModel):
    id: int
    status: OrderStatus
    total_price: Decimal
    items: list[OrderItemResponse]
    payment: PaymentResponse | None

    model_config = {"from_attributes": True}
