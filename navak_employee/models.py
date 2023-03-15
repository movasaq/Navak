import uuid
from sqlalchemy import Column, Integer, String, Date, Boolean, DateTime, Date, Float
from werkzeug.security import generate_password_hash, check_password_hash
from navak.extensions import  db

class Employee(db.Model):
    """
        Base Model For all Employee's
    """
    __tablename__ = "navak_employee"


    id = Column(Integer(), primary_key=True)

    FirstName = Column(String(64), nullable=False)
    LastName = Column(String(64), nullable=False)
    father_name = Column(String())
    BirthDay = Column(Date(), nullable=True)
    MeliCode = Column(String(24), nullable=True)
    BirthLocation = Column(String(128), nullable=True)
    PhoneNumber = Column(String(11), nullable=True)
    EmergencyPhone = Column(String(11), nullable=True)
    Address = Column(String(256), nullable=True)

    Education = Column(String(128), nullable=True)
    StaffCode = Column(Integer(), nullable=False)

    ContractType = Column(String(64), nullable=True)
    StartContract = Column(Date(), nullable=False)
    EndContract = Column(Date(), nullable=False)

    WorkPosition = Column()
    VacationHourTotal = Column(Integer(), nullable=False)
    VacationHourTaken = Column(Integer(), nullable=False)
    PublicKey = Column(String(36), unique=True, nullable=False)

    Married = Column(Boolean())
    Children = Column(Integer())

    BaseSalary = Column(String(64))

    def set_public_key(self):
        while True:
            key = str(uuid.uuid4())
            key_db = Employee.query.filter(Employee.public_key == key).first()
            if not key_db:
                self.public_key = key
                return True
            else:
                continue

    def set_vacation_counter(self):
        """
            this method calculate vacation day for each employee by its contract time
            each 30 days => 2.5 vacation
        """
        day_delta = (self.end_contract - self.start_contract).days
        vataction = ((day_delta / 30) * 2.5) * 8

        # format number to 1 digit after point ==> 2.59898989: 2.6
        vataction = round(vataction)
        self.vacation_count_hour = vataction
        self.vacation_total_hour = vataction