# 🌐 Web Scraping

This project documents my journey into web scraping using Python. I explored foundational libraries like `requests` and `BeautifulSoup`, along with the key methods and concepts they offer.

## 📚 Libraries Covered
- **Requests**: For making HTTP requests and handling responses.
- **BeautifulSoup**: For parsing and navigating HTML content.

## 🔍 Key Concepts and Methods Learned

### 1️⃣ Requests Library
- **HTTP Methods**: GET for retrieving web pages.
- **Status Codes**: Understanding codes like 200 (Success), 404 (Not Found), 403 (Forbidden), and 500 (Server Error).
- **Response Attributes**:
  - `response.content`: Raw binary content of the response.
  - `response.text`: Decoded text content of the response.
  - `response.headers`: Metadata about the response.
  - `response.cookies`: Cookies sent by the server.
  - `response.elapsed`: Time taken for the server to respond.

### 2️⃣ BeautifulSoup Library
- **HTML Parsing**: Using `html.parser` for parsing content.
- **Objects in BeautifulSoup**:
  - **Tags**: Represents HTML tags like `<p>` and `<a>`.
  - **NavigableString**: Text content within tags.
  - **Comment**: Represents comments in the HTML.
  - **ResultSet**: Collection of matching elements, such as all paragraphs.
- **Methods**:
  - `find_all()`: Find all matching elements based on tags or attributes.
  - `prettify()`: Format HTML content for better readability.
  - `.text`: Extract the text inside a tag.
  - `find()`: Retrieve the first matching element.
