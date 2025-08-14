from sqlalchemy import Column, Integer, String, DateTime, Text, Float, Boolean, Table, ForeignKey
from app.db.db import Base
from datetime import datetime
from sqlalchemy.orm import relationship


class OperationRequest(Base):
    __tablename__ = "operation_requests"

    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String, nullable=False)
    input_data = Column(Text, nullable=False)  
    result = Column(Text, nullable=False)      
    timestamp = Column(DateTime, default=datetime.utcnow)
    execution_time_ms = Column(Float, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    user = relationship("User", back_populates="operation_requests")

user_roles = Table(
    "user_roles", Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("role_id", ForeignKey("roles.id"), primary_key=True)
)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    roles = relationship("Role", secondary=user_roles, back_populates="users")
    operation_requests = relationship("OperationRequest", back_populates="user")

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False, index=True)
    users = relationship("User", secondary=user_roles, back_populates="roles")
