import csv
import json
from django.core.management.base import BaseCommand
from search_app.models import Restaurant

class Command(BaseCommand):
    help = 'Load data from CSV file'

    def handle(self, *args, **kwargs):
        file_path = r'C:\Study\Projects\Restaurant_search_task\Restaurant_csv.csv'  # Adjust path as needed
        column_names = ['id', 'name', 'location', 'items', 'lat_long', 'full_details']
        
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_names)
            next(reader)  # Skip header row if your CSV file has headers
            
            for row in reader:
                try:
                    # Parse JSON fields if they exist
                    items = json.loads(row['items']) if row['items'] else {}
                    full_details = json.loads(row['full_details']) if row['full_details'] else {}
                    
                    restaurant = Restaurant(
                        id=int(row['id']),  # Convert 'id' to integer
                        name=row['name'],
                        location=row['location'],
                        items=items,
                        lat_long=row['lat_long'],
                        full_details=full_details
                    )
                    restaurant.save()
                    
                    self.stdout.write(self.style.SUCCESS(f'Successfully loaded restaurant: {restaurant.name}'))
                except ValueError as e:
                    self.stdout.write(self.style.ERROR(f'Error processing row: {row}'))
                    self.stdout.write(self.style.ERROR(str(e)))
                except json.JSONDecodeError as je:
                    self.stdout.write(self.style.ERROR(f'Error decoding JSON: {row["items"]} or {row["full_details"]}'))
                    self.stdout.write(self.style.ERROR(str(je)))
        
        self.stdout.write(self.style.SUCCESS('Data loading completed'))
