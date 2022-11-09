from typing import Optional

from sqlalchemy.orm import Session

import models
import schemas


def get_link(db: Session, link_id: int) -> Optional[models.Link]:
    return db.query(models.Link).filter(models.Link.id == link_id).first()


def create_link(db: Session, link: schemas.LinkCreate) -> models.Link:
    db_link = models.Link(url=link.url)
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link

def update_link(db: Session, link_id: int, link_update: schemas.LinkUpdate) -> models.Link:
    # link = get_link(db, link_id=link_update.id)
    # link.status = link_update.status
    # db.commit()
    # db.refresh(link)
    db.query(models.Link).filter(models.Link.id == link_id).update({'status': link_update.status})
    db.commit()
    return get_link(db, link_id=link_id)
