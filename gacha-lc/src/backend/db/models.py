class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True, index = True)
    username = Column(String, unique = True, index = True)
    hashed_password = Column(String)
    fuel = Column(Integer, default=0)
    inventory = relationship("InventoryItem", back_populates = "user")

class Card(Base):
    __tablename__ = "cards"
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, unique = True)
    image = Column(String)

class InventoryItem(Base):
    __tablename__ = "inventory"
    user_id = Column(Integer, ForeignKey("users.id"))
    card_id = Column(Integer, ForeignKey("cards.id"))
    user = relationship("User", back_populates = "user")
    card = relationship("Card")
    
