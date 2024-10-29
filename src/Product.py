from dataclasses import dataclass
from datetime import date

@dataclass
class Product:
    product_id: int
    product_name: str
    category: str
    price: float
    stock: int
    discount: float
    rating: float
    reviews: int
    sales_volume: int
    return_rate: float
    supplier_id: int
    shipping_time: int
    is_premium_supplier: bool
    customer_segment: str
    purchase_frequency: int
    profit_margin: float
    last_restocked_date: date
