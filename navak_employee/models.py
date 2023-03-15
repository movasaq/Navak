import uuid
from sqlalchemy import Column, Integer, String, Date, Boolean, DateTime, Date, Float
from werkzeug.security import generate_password_hash, check_password_hash
from navak.extensions import db

class Employee(db.Model):
    """
        Base Model For all Employee's
    """
    __tablename__ = "navak_employee"


    id = Column(Integer(), primary_key=True)

    FirstName = Column(String(64), nullable=False)
    LastName = Column(String(64), nullable=False)
    FatherName = Column(String(64), nullable=False)
    BirthDay = Column(Date(), nullable=True)
    MeliCode = Column(String(32), nullable=True)
    BirthLocation = Column(String(64), nullable=True)
    PhoneNumber = Column(String(11), nullable=True)
    EmergencyPhone = Column(String(11), nullable=True)
    Address = Column(String(256), nullable=True)

    Education = Column(Integer(), db.ForeignKey() ,nullable=True)
    StaffCode = Column(Integer(), nullable=False)

    ContractType = Column(String(64), nullable=True)
    StartContract = Column(Date(), nullable=False)
    EndContract = Column(Date(), nullable=False)

    WorkPosition = Column(Integer(), db.ForeignKey(), nullable=False)
    VacationHourTotal = Column(Float(), nullable=False)
    VacationHourTaken = Column(Float(), nullable=False)
    PublicKey = Column(String(36), unique=True, nullable=False)

    Married = Column(Boolean(), nullable=False)
    Children = Column(Integer(), nullable=False)
    BaseSalary = Column(Integer(), nullable=False)

    def set_public_key(self):
        """
            this Method Set Unique PublicKey For each Employee Object
        """
        while True:
            key = str(uuid.uuid4())
            key_db = Employee.query.filter(Employee.PublicKey == key).first()
            if not key_db:
                self.PublicKey = key
                return True
            else:
                continue

    def __str__(self):
        return f"{self.id}-{self.FirstName} {self.LastName}"


    def CalculateVacationHour(self):
        """
            this Method calculate vacation hour for each employee by its contract time
            each 30 days => 2.5 Day vacation
        """
        day_delta = (self.end_contract - self.start_contract).days
        vacation = ((day_delta / 30) * 2.5) * 8

        # format number to 1 digit after point ==> 2.59898989: 2.6
        vacation = round(vacation)
        self.VacationHourTotal = vacation
