from datetime import date

class Reviewer:
    def __init__(self, name, position, organization):
        self.name = name
        self.position = position
        self.organization = organization

    def get_full_identity(self):
        return f"{self.name}, {self.position} - {self.organization}"


class Review:
    def __init__(self, content, reviewer, review_date=None):
        self.content = content
        self.reviewer = reviewer
        self.review_date = review_date if review_date else date.today()

    def get_summary(self):
        return self.content[:50] + "..."


class Book:
    def __init__(self, title, series, publisher, topic):
        self.title = title
        self.series = series
        self.publisher = publisher
        self.topic = topic
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def get_all_reviews(self):
        return self.reviews


# ==== Contoh Penggunaan ====
reviewer1 = Reviewer(
    "Barry Hawkins",
    "Editor",
    "Slashdot.org"
)

book = Book(
    "Head Rush Ajax",
    "Head First Series",
    "O'Reilly",
    "Ajax Web Development"
)

review1 = Review(
    "Head Rush Ajax is a most enjoyable launchpad into Ajax.",
    reviewer1
)

book.add_review(review1)

# Output
for r in book.get_all_reviews():
    print(r.get_summary())
    print(r.reviewer.get_full_identity())