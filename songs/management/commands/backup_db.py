from django.core.management.base import BaseCommand
from datetime import datetime
from django.conf import settings
import os
import subprocess

class Command(BaseCommand):
    help = "Backup the database"

    def add_arguments(self, parser):
        parser.add_argument(
            "--output-path",
            type=str,
            help="specify the output path",
        )

        parser.add_argument(
            "--db-type",
            type=str,
            help="specify the type of database to backup",
        )

    def handle(self, *args, **kwargs):
        output_path = kwargs.get("--output-path") or os.path.join(settings.BASE_DIR, "backup.sql")
        db_type = kwargs.get("--db-type") or "default"

        if db_type == 'postgresql':
            backup_command = f'pg_dump {settings.DATABASES[db_type]["NAME"]} > {output_path}'
        elif db_type == 'mysql':
            backup_command = f'mysqldump -u {settings.DATABASES[db_type]["USER"]} -p{settings.DATABASES[db_type]["PASSWORD"]} {settings.DATABASES[db_type]["NAME"]} > {output_path}'
        elif db_type == 'default' or db_type == 'sqlite3':
            backup_command = f'cp {os.path.join(settings.BASE_DIR, settings.DATABASES[db_type]["NAME"])} {output_path}'
        else:
            self.stderr.write(self.style.ERROR(f'Unsupported database type: {db_type}'))
            return

        subprocess.check_call(backup_command, shell=True)
        self.stdout.write(
            self.style.SUCCESS(f"Successfully created backup: {output_path}")
        )


