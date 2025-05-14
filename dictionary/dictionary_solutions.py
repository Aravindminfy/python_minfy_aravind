
#Write a function called invert_dictionary that takes a dictionary and returns a new dictionary where the keys become values and values become keys.
def invert_dictionary(d):
    return {v: k for k, v in d.items()}

# Example usage:
print(invert_dictionary({"a": 1, "b": 2, "c": 3}))  # Should return {1: "a", 2: "b", 3: "c"}

#------------------------------------------------------------------------------------------------------------------

#Write a function called merge_dictionaries that takes two dictionaries and merges them. If a key exists in both dictionaries, the value from the second dictionary should be used.

def merge_dictionaries(dict1, dict2):
    result = dict1.copy()   
    result.update(dict2)     
    return result

# Example usage:
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dictionaries(dict1, dict2))  # Should return {"a": 1, "b": 3, "c": 4}

#------------------------------------------------------------------------------------------------------------------


#Write a function called word_frequencies that takes a string of text and returns a dictionary mapping each word to its frequency (count of occurrences).

def word_frequencies(text):
    text = text.split()
    output = {}
    for i in text:
        if i in output:
            output[i] += 1
        else:
            output[i] = 1
    return output


# Example usage:
text = "the quick brown fox jumps over the lazy dog"
print(word_frequencies(text))
# Should return {"the": 2, "quick": 1, "brown": 1, "fox": 1, "jumps": 1, "over": 1, "lazy": 1, "dog": 1}

# -------------------------------------------------------------------------------------------------------------

#Create a function called add_contact that manages a nested dictionary representing a contact book. The function should add a new contact with details or update an existing contact.

def add_contact(contacts, name, **details):
    if name not in contacts:
        contacts[name] = {}
    contacts[name].update(details)


# Example usage:
contacts = {}
add_contact(contacts, "Alice", phone="123-456-7890", email="alice@example.com")
add_contact(contacts, "Bob", phone="987-654-3210")
add_contact(contacts, "Alice", address="123 Main St")  # Updates Alice's info

print(contacts)
# Should return:
# {
#   "Alice": {"phone": "123-456-7890", "email": "alice@example.com", "address": "123 Main St"},
#   "Bob": {"phone": "987-654-3210"}
# }

# -----------------------------------------------------------------------------------------------------------------