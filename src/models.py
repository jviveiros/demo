from sqlalchemy import Column, Integer, String, ARRAY, ForeignKey
from sqlalchemy.orm import relationship

from database import Base



class Provider(Base):
    __tablename__ = "providers"
    id = Column(Integer, primary_key=True)
    finch_id = Column(String(50))
    name = Column(String(50))
    finch_api_key = Column(String(60))
    def __repr__(self):
        return f"<Provider {self.name}>"
    
class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    finch_id = Column(String(50))
    legal_name = Column(String(50))
    entity_type = Column(String(50))
    entity_subtype = Column(String(50))
    primary_email = Column(String(50))
    primary_phone_number = Column(String(13))
    departments = Column(ARRAY(String))
    ein = Column(String(50))
    locations = Column(ARRAY(String))
    accounts = Column(ARRAY(String))
    individuals = relationship("Individual", back_populates="company")

    def __repr__(self):
        return f"<Company {self.name}>"
    
class Individual(Base):
    __tablename__ = "indivudals"
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey(Company.id))
    finch_id = Column(String(50))
    
    company = relationship("Company", back_populates="individuals")
    
    def __repr__(self):
        return f"<Individual {self.name}>"
