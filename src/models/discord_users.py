from sqlalchemy.sql import func
from sqlalchemy import Column, BigInteger, String, DateTime, Boolean

from .model import database

class DiscordUser(database.Base):
	__tablename__='discord_users'
	id = Column(BigInteger, primary_key=True, unique=True, nullable=False, autoincrement=False)
	created = Column(DateTime(timezone=True), server_default=func.now())
	updated = Column(DateTime(timezone=True), nullable=True)
	blacklisted = Column(Boolean, unique=False, default=False)
	owner = Column(Boolean, unique=False, default=False)
	moderator = Column(Boolean, unique=False, default=False)

	def __repr__(self):
		return f"{self.id}"