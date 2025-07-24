from  sqlalchemy import ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, mapped_column, Mapped

from app.backend.db import Base
from app.models.user_model import User_Model
from app.models.home_user import home_user


class My_Home(Base):
    __tablename__ = "my_home"
    id:Mapped[int] = mapped_column(Integer(), index=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(60))
    slug: Mapped[str] = mapped_column(String(60))
    user: Mapped[list["User_Model"]] = relationship(
        "User_Model",
        back_populates="home",
        secondary=home_user
        )

    
