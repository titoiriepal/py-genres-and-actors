from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet[Actor]:
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Dramma")

    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    genre_to_update = Genre.objects.get(name="Dramma")
    genre_to_update.name = "Drama"
    genre_to_update.save()

    actor_to_update = Actor.objects.get(first_name="George", last_name="Klooney")
    actor_to_update.last_name = "Clooney"
    actor_to_update.save()

    actor_to_update = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    actor_to_update.first_name = "Keanu"
    actor_to_update.last_name = "Reeves"
    actor_to_update.save()

    genre_to_delete = Genre.objects.get(name="Action")
    genre_to_delete.delete()

    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")

