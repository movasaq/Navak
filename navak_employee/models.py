import khayyam
import uuid
from sqlalchemy import Column, Integer, String, Boolean, Date, Float, DateTime
from werkzeug.security import generate_password_hash, check_password_hash
from navak.extensions import db



class Education(db.Model):
    """
        base Model For keep all degree of education
    """
    __tablename__ = "navak_education_degree"
    id = Column(Integer(), primary_key=True)
    Name = Column(String(64), nullable=False)
    employee = db.relationship("Employee", backref="Education", lazy="True")


class WorkPosition(db.Model):
    """
        base Model For keep all WorkPositions
    """
    __tablename__ = "navak_work_position"
    id = Column(Integer(), primary_key=True)
    Name = Column(String(64), nullable=False)
    employee = db.relationship("Employee", backref="WorkPosition", lazy="True")




class Employee(db.Model):
    """
        Base Model For all Employee's
    """
    __tablename__ = "navak_employee"

    id = Column(Integer(), primary_key=True)

    UserName = Column(String(64), nullable=False)
    password = Column(String(102), nullable=False)
    FirstName = Column(String(64), nullable=False)
    LastName = Column(String(64), nullable=False)
    FatherName = Column(String(64), nullable=False)
    BirthDay = Column(Date(), nullable=True)
    MeliCode = Column(String(32), nullable=True)
    BirthLocation = Column(String(64), nullable=True)
    PhoneNumber = Column(String(11), nullable=True)
    EmergencyPhone = Column(String(11), nullable=True)
    Address = Column(String(256), nullable=True)

    Education = Column(Integer(), db.ForeignKey("navak_education_degree.id") ,nullable=True)
    StaffCode = Column(Integer(), nullable=False)

    ContractType = Column(String(64), nullable=True)
    StartContract = Column(Date(), nullable=False)
    EndContract = Column(Date(), nullable=False)

    WorkPosition = Column(Integer(), db.ForeignKey("navak_work_position.id"), nullable=False)
    VacationHourTotal = Column(Float(), nullable=False)
    VacationHourTaken = Column(Float(), nullable=False)
    PublicKey = Column(String(36), unique=True, nullable=False)

    Married = Column(Boolean(), nullable=False)
    Children = Column(Integer(), nullable=False)
    BaseSalary = Column(Integer(), nullable=False)

    Created_Time = Column(DateTime(), nullable=False, default=khayyam.JalaliDatetime.now())


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


class ModifyLog(db.Model):
    """
        this Table Log all Actions on Employee Table
    """
    __tablename__ = "navak_emploee_log"
    id = Column(Integer(), primary_key=True)
    # reffer to admin panel
    By = Column(Integer(), )
    Description = Column(String(512), nullable=False)
    LogTime = Column(DateTime(), default=khayyam.JalaliDatetime.now())








