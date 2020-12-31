import datetime
import os

import pytz
from django.contrib.auth.models import User

from reservations_backend.apps.brand.models import Brand
from reservations_backend.apps.event.models import Event, EventType
from reservations_backend.apps.profile.models import Profile
from reservations_backend.apps.reservation.models import Reservation

# from reservations_backend.data.samples import seed_data
# seed_data()


def seed_data():
    brand_one = Brand(
        name="XYZ Winery",
        city="Napa",
        logo="https://www.google.com/imgres?imgurl=http%3A%2F%2Feaglesnestatbannerelk.com%2Fwp-content%2Fuploads%2F2019%2F02%2FWineryView.jpg&imgrefurl=http%3A%2F%2Feaglesnestatbannerelk.com%2Feagles-nest-winery-to-open-in-fall-2019%2F&tbnid=sCFB5O09YsN_OM&vet=12ahUKEwjZ5_GA0_HtAhXvIzQIHSIRAQsQMygDegUIARDTAQ..i&docid=rAaTTRDhmgy0pM&w=1920&h=701&q=winery&ved=2ahUKEwjZ5_GA0_HtAhXvIzQIHSIRAQsQMygDegUIARDTAQ")
    brand_two = Brand(
        name="Great Winery",
        city="Sonoma",
        logo="https://www.mediaplace.us/wp-content/uploads/2019/07/Ava-Winery-Teaser.jpg"
    )
    brand_one.save()
    brand_two.save()
    # user = User.objects.create_user(
    #     os.environ["SUPERUSER_USERNAME"],
    #     os.environ["SUPERUSER_EMAIL"],
    #     os.environ["SUPERUSER_PASSWORD"]
    # )

    event_one = Event(
        name="New Tasting",
        event_type=EventType.Tasting.value,
        date_started=datetime.datetime.now(pytz.utc),
        date_ended=datetime.datetime.now(pytz.utc),
        brand=brand_one
    )
    event_two = Event(
        name="Visit",
        event_type=EventType.Tasting.value,
        date_started=datetime.datetime.now(pytz.utc),
        date_ended=datetime.datetime.now(pytz.utc),
        brand=brand_two
    )
    # user.save()
    event_one.save()
    event_two.save()
