#!/usr/bin/python3
"""
Place Module for HBNB project
"""

from models.base_model import BaseModel, Base
from os import getenv
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column, ForeignKey, Integer, Float, String, Table
from sqlalchemy.orm import relationship

if getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """
    A place to stay
    """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        # Reviews relationship
        reviews = relationship("Review", backref="place", cascade="delete")
        # Amenities relationship
        amenities = relationship("Amenity", secondary="place_amenity",
                                 back_populates="place_amenities",
                                 viewonly=False)

    else:
        @property
        def reviews(self):
            """
            Get a list of all linked Reviews
            """
            from models import storage
            review_list = []
            for review in list(storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """
            Getter linked Amenities
            """
            from models import storage
            amenity_list = []
            for amenity in list(storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            """
            Setter Linked Amenities
            """
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
