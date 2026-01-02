from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Attempt(Base):
    __tablename__ = "attempts"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    # What was attempted (flexible for MVP)
    activity_type: Mapped[str] = mapped_column(String, nullable=False)  # e.g., "practice", "content"
    topic: Mapped[str] = mapped_column(String, nullable=True)          # optional tagging
    score: Mapped[int] = mapped_column(Integer, nullable=True)         # optional

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
