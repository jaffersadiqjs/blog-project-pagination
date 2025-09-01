from django.core.management.base import BaseCommand
from blog.models import Category, Post
import random

class Command(BaseCommand):
    help = "Seed database with sample data"

    def handle(self, *args, **kwargs):
        categories = ['Django', 'Python', 'Web Development', 'Tutorial', 'News']
        post_titles = [
            'Getting Started with Django',
            'Advanced Python Tips',
            'Deploying Your App',
            'Django vs Flask',
            'New Features in Django 4',
            'Building REST APIs',
            'Pagination in Django',
            'Search and Filter Techniques',
            'Django ORM Tips',
            'Full Stack Development'
        ]

        # Clear existing data
        Category.objects.all().delete()
        Post.objects.all().delete()

        # Add categories
        category_objs = [Category.objects.create(name=cat) for cat in categories]

        # Add posts
        for title in post_titles:
            Post.objects.create(
                title=title,
                content=f"This is the content for {title}. " * 10,
                category=random.choice(category_objs)
            )

        self.stdout.write(self.style.SUCCESS('Sample data inserted successfully!'))
