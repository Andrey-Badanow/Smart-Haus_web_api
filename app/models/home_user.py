from sqlalchemy import Table, Column, ForeignKey, Integer
from app.backend.db import Base

home_user = Table(
    "home_user",
    Base.metadata,
    Column("home_id", Integer, ForeignKey("my_home.id"), primary_key=True),
    Column("user_id", Integer, ForeignKey("user_model.id"), primary_key=True),
)