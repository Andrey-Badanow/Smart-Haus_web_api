from sqlalchemy import Integer, Boolean, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.home_user import home_user
from app.models.my_home_model import My_Home


from app.backend.db import Base

class User_Model(Base):
    __tablename__ = "user_model"
    id: Mapped[int] = mapped_column(Integer(), primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String(60))
    last_name: Mapped[str] = mapped_column(String(60))
    email: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(60))
    home: Mapped[list["My_Home"]] = relationship(
        "My_Home",
        secondary=home_user, 
        back_populates="user")
