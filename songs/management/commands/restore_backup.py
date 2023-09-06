from django.core.management.base import BaseCommand
from datetime import datetime
from django.conf import settings
import os
import subprocess


class Command(BaseCommand):
    help = "Restore a database from a specified location"

    def add_arguments(self, parser):
        parser.add_argument(
            "--input-path",
            type=str,
            help="specify the input path",
        )

        parser.add_argument(
            "--db-type",
            type=str,
            default="default",
            help="specify the type of database to backup",
        )

    def handle(self, *args, **options):
        output_path = options.get("--output-path") or os.path.join(
            settings.BASE_DIR, "backup.sql"
        )
        db_type = options.get("--db-type") or "default"

        database_config = settings.DATABASES.get(db_type)

        if database_config["ENGINE"] == "django.db.backends.sqlite3":
            restore_command = (
                f"python manage.py loaddata {backup_path} --database={database_config}"
            )
        elif database_config["ENGINE"] == "django.db.backends.postgresql":
            restore_command = f'pg_restore -d {database_config["NAME"]} -U {database_config["USER"]} -h {database_config["HOST"]} -p {database_config["PORT"]} -v {backup_path}'
        else:
            self.stderr.write(
                self.style.ERROR(
                    f'Unsupported database engine: {database_config["ENGINE"]}'
                )
            )
            return

        subprocess.check_call(restore_command, shell=True)
        self.stdout.write(self.style.SUCCESS("Database restored successfully"))
