from django.core.management import BaseCommand
from catalog.models import Category, Product
import json


class Command(BaseCommand):

    def handle(self, *args, **options) -> None:

        Product.objects.all().delete()
        Category.objects.all().delete()

        with open('./././data.json') as data:

            data_dict = json.loads(data.read())
            categoryes_for_create, products_for_create = [], []

            for elem in data_dict:
                if elem['model'] == 'catalog.product':
                    products_for_create.append(Product(**elem['fields']))
                else:
                    categoryes_for_create.append(Category(**elem['fields']))

            Category.objects.bulk_create(categoryes_for_create)
            Product.objects.bulk_create(products_for_create)
