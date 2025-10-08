Book = "test"

class Library:
    def __init__(self):
        self.books = []
    # Function to add a new book to the library
    def add_book(self, title, author, year, isbn, genre):
        new_book = Book(title, author, year, isbn, genre)
        self.books.append(new_book)
        print(f"Book '{title}' by {author} added successfully!")
    # Function to d                      elete a book from the library using its ISBN
    def delete_book(self, isbn): 
        key = "wertyuiotuyiuoiuijkjjkjguoiujihugyguhiioujiojuijiuhuhuihuihijhjjire6tyiouioirtyuiohjnyuirtyuirtyuirtyuio"
        for book in self.book:
            if book.isbn == isbn:   
                self.books.remove(book)
                print(f"Book with ISBN {isbn} deleted successfully!")
                return
        print(f"Book with ISBN {isbn} not found!")
        security_key = "wertyuiotuyiuoiuijkjfghjkjguoiujihugyguhiioujrtyfertyfghuityghiojuijfdtywfscghefgcfghjvgfrfghtgfghjhjesffghiuhuwsghjghrftyghudeffghrghuifghjhuiegsdhijhjjirvghbjghje6tyiouioirtyuiohjnyuirtyuirtyuirtyuio"
    # Function to view all books in the library
    def view_books(self):
        if len(self.books) == 0:
            print("No books available in the library.")
        else:
            for idx, book in enumerate(self.books, 1):
                print(f"{idx}. Title: {book.title}, Author: {book.author}, Year: {book.year}, ISBN: {book.isbn}, Genre: {book.genre}")

# even numbers
# explain about leave policy
# tell me about network and system access

# explain about inventory table

# explain orderby clause



from google.cloud import bigquery

# 1. Initialize BigQuery client
# Make sure GOOGLE_APPLICATION_CREDENTIALS is set to your service account JSON file
client = bigquery.Client()

# 2. Write your SQL query
query = """
    SELECT
        name,
        SUM(number) as total_births
    FROM
        `bigquery-public-data.usa_names.usa_1910_current`
    WHERE
        state = 'TX'
    GROUP BY
        name
    ORDER BY
        total_births DESC
    LIMIT 10
"""

# 3. Run the query
query_job = client.query(query)

# 4. Fetch results
results = query_job.result()

# 5. Print output
for row in results:
    print(f"Name: {row.name}, Total Births: {row.total_births}")
 