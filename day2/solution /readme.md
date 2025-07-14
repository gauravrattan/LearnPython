# Python: Understanding *args and **kwargs

This mini project explains how to use `*args` and `**kwargs` in Python functions. These features help you write flexible, reusable, and dynamic functions that can handle varying numbers of inputs.

---

## 📌 What is `*args`?

- `*args` allows a function to accept any number of **positional arguments**.
- These arguments are stored as a **tuple** inside the function.
- Useful when you’re not sure how many values will be passed.

### ✅ Example of `*args`

```python
def add_numbers(*args):
    total = sum(args)
    print("Sum:", total)

add_numbers(10, 20, 30)
```

---

## 📌 What is `**kwargs`?

- `**kwargs` allows a function to accept any number of **keyword arguments**.
- These arguments are stored as a **dictionary** inside the function.
- Useful for handling optional or dynamic key-value inputs.

### ✅ Example of `**kwargs`

```python
def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_info(name="Alice", age=25, city="London")
```
