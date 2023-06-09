import uuid

import khayyam
from sqlalchemy import Column, Integer, String, Boolean, Date, Float, DateTime, BigInteger
from werkzeug.security import check_password_hash

from navak.extensions import db


class Education(db.Model):
    """
        base Model For keep all degree of education
    """
    __tablename__ = "navak_education_degree"
    id = Column(Integer(), primary_key=True)
    Name = Column(String(64), nullable=False, unique=True)
    employee = db.relationship("Employee", backref="education", lazy=True)


class WorkPosition(db.Model):
    """
        base Model For keep all WorkPositions
    """
    __tablename__ = "navak_work_position"
    id = Column(Integer(), primary_key=True)
    Name = Column(String(64), nullable=False, unique=True)
    employee = db.relationship("Employee", backref="workposition", lazy=True)




class Employee(db.Model):
    """
        Base Model For all Employee's
    """
    __tablename__ = "navak_employee"

    id = Column(Integer(), primary_key=True)

    UserName = Column(String(64), nullable=False, unique=True)
    password = Column(String(102), nullable=False)
    FirstName = Column(String(64), nullable=False)
    LastName = Column(String(64), nullable=False)
    FatherName = Column(String(64), nullable=False)
    BirthDay = Column(Date(), nullable=True)
    MeliCode = Column(String(32), nullable=True, unique=True)
    BirthLocation = Column(String(64), nullable=True)
    PhoneNumber = Column(String(11), nullable=True, unique=True)
    EmergencyPhone = Column(String(11), nullable=True)
    Address = Column(String(256), nullable=True)

    Education = Column(Integer(), db.ForeignKey("navak_education_degree.id"), nullable=True)
    StaffCode = Column(Integer(), nullable=False, unique=True)

    ContractType = Column(String(64), nullable=True)
    StartContract = Column(Date(), nullable=False)
    EndContract = Column(Date(), nullable=False)

    WorkPosition = Column(Integer(), db.ForeignKey("navak_work_position.id"), nullable=False)
    VacationHourTotal = Column(Float(), nullable=False)
    VacationHourTaken = Column(Float(), nullable=False)
    PublicKey = Column(String(36), unique=True, nullable=False)

    Married = Column(Boolean(), nullable=False)
    Children = Column(Integer(), nullable=True, default=0)
    BaseSalary = Column(BigInteger(), nullable=False)

    Created_Time = Column(DateTime(), nullable=False, default=khayyam.JalaliDatetime.now)

    Active = Column(Boolean(), default=False)
    EmployeeTrffic = db.relationship("TrafficControl", backref="employee", lazy=True)

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

    def set_password(self, password):
        self.password = password

    def check_password(self, password):
        return check_password_hash(password, self.password)

    def calculate_vacation_hour(self):
        """
            this Method Calculate vacation hour for each employee by its contract time
            each 30 days => 2.5 Day vacation
        """
        day_delta = (self.EndContract - self.StartContract).days
        vacation = ((day_delta / 30) * 2.5) * 8

        # format number to 1 digit after point ==> 2.59898989: 2.6
        vacation = round(vacation)
        self.VacationHourTotal = vacation
        self.VacationHourTaken = 0
