import uuid
import khayyam
from navak.extensions import db
from sqlalchemy import Column, String, Integer, DateTime



class Mailing(db.Model):
    """
        base Model For mailing in system
    """
    __tablename__ = "navak_mailes"
    id = Column(Integer(), primary_key=True)

    MailTitle = Column(String(128))
    MailCaption = Column(String(4096))
    MailTime = Column(DateTime(), default=khayyam.JalaliDatetime.now)

    From = Column(Integer(), db.ForeignKey("navak_users.id"), nullable=False)
    To = Column(Integer(), db.ForeignKey("navak_users.id"), nullable=False)

    PublicKey = Column(String(36), nullable=False)


    def __str__(self):
        return f"{self.id}-{self.MailTitle[:15]}"

    def set_public_key(self):
        while True:
            key = str(uuid.uuid4())
            key_db = Mailing.query.filter(Mailing.PublicKey == key).first()
            if not key_db:
                self.PublicKey = key
                break
            else:
                continue




