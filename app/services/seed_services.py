from sqlalchemy.orm import Session
from app.models.db_models import Role

def ensure_roles(db: Session, names=("user", "admin")):
    existing = {r.name for r in db.query(Role).all()}
    for name in names:
        if name not in existing:
            db.add(Role(name=name))
    db.commit()
