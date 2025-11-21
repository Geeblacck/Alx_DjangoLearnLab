
---

### ✅ Step 5: Combine All CRUD in One File

Create another file named **`CRUD_operations.md`** that combines all the above sections in one document:

```markdown
# CRUD Operations on Book Model

---

## Create
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Output: <Book: 1984 by George Orwell (1949)>
