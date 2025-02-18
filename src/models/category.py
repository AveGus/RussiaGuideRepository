from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from services.database import Base


class Category(Base):
    __tablename__ = 'categories'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))