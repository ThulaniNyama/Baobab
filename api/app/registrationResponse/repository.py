from app import db
from app.registration.models import Offer, Registration
from app.users.models import AppUser
from app.events.models import Event

class RegistrationRepository():
    
    @staticmethod
    def get_by_id_with_offer(registration_id):
        """Get a registration by its id."""
        return db.session.query(Registration, Offer).filter(
            Registration.id == registration_id).join(
                Offer, Offer.id == Registration.offer_id
            ).one_or_none()

    @staticmethod
    def get_by_user_id(user_id):
        """Get the registration for a given user id."""
        return db.session.query(Registration).join(
            Offer, Registration.offer_id == Offer.id
        ).filter(
            Offer.user_id == user_id
        ).first()

    @staticmethod
    def get_all_for_event(event_id):
        """Get all registrations for an event"""
        return db.session.query(Registration, Offer, AppUser).join(
            Offer, Registration.offer_id == Offer.id
        ).join(
            AppUser, Offer.user_id == AppUser.id
        ).filter(
            Offer.event_id == event_id
        ).all()

    @staticmethod
    def get_confirmed_for_event(event_id, confirmed):
        """Get registrations for an event according to confirmed status."""
        return db.session.query(Registration, Offer, AppUser).filter(
            Registration.confirmed == confirmed
        ).join(
            Offer, Registration.offer_id == Offer.id
        ).join(
            AppUser, Offer.user_id == AppUser.id
        ).filter(
            Offer.event_id == event_id
        ).all()
