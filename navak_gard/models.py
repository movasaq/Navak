import uuid
import khayyam
from navak.extensions import db
from sqlalchemy import Column, String, Integer, DateTime, Boolean



class TrafficControl(db.Model):
    """
        base Model For gard traffic control
    """
    __tablename__ = "navak_traffic_control"
    id = Column(Integer(), primary_key=True)

    EnterTime = Column(DateTime(), nullable=False)
    ExitTime = Column(DateTime(), nullable=False)
    Employee_id = Column(Integer(), db.ForeignKey("navak_employee.id"), nullable=False)

    PublicKey = Column(String(36), nullable=False)


    def __str__(self):
        return f"{self.id}"


    def set_public_key(self):
        while True:
            key = str(uuid.uuid4())
            key_db = TrafficControl.query.filter(TrafficControl.PublicKey == key).first()
            if not key_db:
                self.PublicKey = key
                break
            else:
                continue



class GuestTrafficControl(db.Model):
    """
        base Model For guest traffic control
    """
    __tablename__ = "navak_guest_traffic_control"
    id = Column(Integer(), primary_key=True)

    EnterTime = Column(DateTime(), nullable=False)
    ExitTime = Column(DateTime(), nullable=False)
    title = Column(String(64), nullable=False)
    description = Column(String(512), nullable=False)
    PublicKey = Column(String(36), nullable=False)

    def __str__(self):
        return f"{self.id}-{self.title[:15]}"


    def set_public_key(self):
        while True:
            key = str(uuid.uuid4())
            key_db = GuestTrafficControl.query.filter(GuestTrafficControl.PublicKey == key).first()
            if not key_db:
                self.PublicKey = key
                break
            else:
                continue


