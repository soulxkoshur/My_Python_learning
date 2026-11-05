from unittest import result


results = ["Mario", "Luigi"]
results.append("princess")
results.append(["Cat", "Dog"]) #it will add the list as it is!, like one item
results.remove(["Cat", "Dog"]) # this is how we remove something unwanted
results.extend(["Cat", "Dog"]) # This is the proper way to add items from a list to another list!
results.insert(1, "Bull dog")  # to insert the item at a specific place!.>first we type index then the item for that index
# results.reverse(), reverses the order of items in the list.
print(results)
