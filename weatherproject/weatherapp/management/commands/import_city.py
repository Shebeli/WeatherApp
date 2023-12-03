from typing import Any

from django.core.management.base import BaseCommand, CommandParser

from weatherapp.models import CityCord, CityImportStatus


class Command(BaseCommand):
    help = """
    Import the cities cords into the db. 
    This command should be executed once incase the db doesn't have
    the cordinates of cities.
    """

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("path", type=str, help="The path referencing to JSON file")

    def handle(self, *args: Any, **options: Any) -> str | None:
        if CityImportStatus.objects.filter(is_imported=True).exists():
            self.stdout.write(
                self.style.NOTICE(
                    "The cities data have already been imported to database! Use update_city command for reimporting."
                )
            )
        else:
            file_path = options["path"]  # eg: C:/users/john/cities.json
            with open(file_path) as cities:
                for city in cities:
                    CityCord.objects.create(
                        name=city["name"],
                        country=city["country"],
                        lat=city["lat"],
                        lon=city["lng"],
                    )
            CityImportStatus.objects.create(is_imported=True)
