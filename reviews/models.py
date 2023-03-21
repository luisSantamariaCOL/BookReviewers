from django.db import models
from django.contrib import auth

# Create your models here.


class Publisher(models.Model):
    """A company that publishes books."""
    name = models.CharField(max_length=70,
                            help_text="Enter the name of the publisher.")
    website = models.URLField(help_text="Enter the publisher's website.")
    email = models.EmailField(help_text="Enter the publisher's email address.")


class Book(models.Model):
    """A published book."""
    title = models.CharField(max_length=100,
                             help_text="Enter the title of the book.")
    publication_date = models.DateField(
        verbose_name="Date the book was published.")
    isbn = models.CharField(max_length=20,
                            help_text="Enter the ISBN of the book.")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField(
        'Contributor', through='BookContributor')


class Contributor(models.Model):
    """A contributor to a Book. e.g. author, editor, 
        coauthor, illustrator, etc..."""
    first_names = models.CharField(max_length=50,
                                   help_text="Enter the first name(s) of the contributor.")
    last_names = models.CharField(max_length=50,
                                  help_text="Enter the last name(s) of the contributor.")
    email = models.EmailField(
        help_text="Enter the contributor's email address.")


class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE)
    contributor = models.ForeignKey(
        Contributor,
        on_delete=models.CASCADE)
    role = models.CharField(
        verbose_name="The role this contributor played in the book.", choices=ContributionRole.choices, max_length=20)


class Review(models.Model):
    content = models.TextField(help_text="Enter your review of the book.")
    rating = models.IntegerField(help_text="Enter your rating of the book.")
    date_created = models.DateTimeField(auto_now_add=True, help_text="The date and time this review was created.")
    last_date_edited = models.DateTimeField(null=True, help_text="The date and time this review was last edited.")
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, help_text="The Book this review is for.")
