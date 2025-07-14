# 🧾 User Info Printer

This Python script traverses a nested dictionary structure and prints all user-related information, including each user's details and a list of their friends.

---

## 🧠 Logic Breakdown

1. Loop through each user in the list `a_dict`.
2. For each user (which is a dictionary), iterate through all key-value pairs using `.items()`.
3. If the value is a list (like the `"frieds"` key), pass it to the `fried_func()` to handle nested friend data.
4. Otherwise, print the key-value pair directly.
5. The `fried_func()` is a helper function that:
    - Loops through each friend dictionary.
    - Prints each friend’s information with a tab for better formatting.

---

## 🧰 Function & Method Explanations

### 🔁 `dict.items()`

- In Python, the .items() method is a built-in dictionary method that returns a view object. This view object contains all the key-value pairs of the dictionary as tuples, where each tuple is in the format (key, value).

#### Example:
```python
{"name": "gara"}.items()  # ➝ [('name', 'gara')]
```
### 🧪 `isinstance()`

-  isinstance(object, type) is used to check the type of a value at runtime.
