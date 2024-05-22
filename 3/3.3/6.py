text = 'Мама мыла раму!'
print({i : text.lower().count(i) for i in set(text.lower()) if 'а' <= i <= 'я'})
