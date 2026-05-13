# ✅ Задача 1. Исправь баг: Имя Автора Книги должны быть строго буквами
# ✅ Задача 2. Добавить Жанр и Рейтинг
# ✅ Задача 3. Добавить функцию для смены названия книги

from time import sleep

THE_LIBRARY = [
			{"genre": "История", "title" : "Бусидо", "author" : "Юдзан Дайдодзи", "date" : 1998, "rating": 7.6, "read" : False},
			{"genre": "История", "title" : "Хагакурэ", "author" : "Юдзан Дайдодзи", "date" : 2000, "rating": 7.6, "read" : False},
			{"genre": "Роман", "title" : "Метро 2033", "author" : "Дмитрий Глуховский", "date" : 2005, "rating": 7.6, "read" : True}
]

def start():
	print("\n         📚 Моя Библиотека\n")
	print("1. Книги")
	print("2. Статистика")
	print("3. Добавить книгу")
	print("4. Изменить информацию о книге")
	print("5. Удалить книгу")
	print("-------------------------------------")
	print("6. Выйти из Библиотеки")
	print("-------------------------------------")

def get_books_by_author(library, author):
	books = [library[i] for i in range(0, len(library)) if author[0] in library[i]['author'][0]]

	return books

def display_read_status(is_read):
	return ('Нет 📕', 'Да 📗')[is_read]

def display_books(books):
	number_book = 0

	for book in books:
		number_book += 1
		display_book(book, number_book)
		sleep(0.5)

def display_book(the_book, number_book):
	print(f"\n📔 Информация о книге №{number_book}:")
	print()
	print(f"Жанр: {the_book['genre']}")
	print(f"Название: {the_book['title']}")
	print(f"Автор: {the_book['author']}")
	print(f"Год: {the_book['date']}")
	print(f"Рейтинг: {the_book['rating']}")
	print(f"Прочитано: {display_read_status(the_book['read'])}")

def input_genre():
	while True:
		genre = input("Введите жанр книги: ").title()
		if genre.replace(' ', '').isalpha():
			return genre
		print("❌ Название жанра должно состоять строго из букв")

def input_title():
	while True:
		title = input("Введите название новой книги: ").title()
		if title.replace(' ', '').isalpha():
			return title
		print("❌ Название книги должно состоять строго из букв")
		
def input_author():
	while True:
		author = input("Введите автора новой книги: ").title()
		if author.replace(' ', '').isalpha():
			return author
		print("❌ Имя Автора должно состоять строго из букв")

def input_date():
	while True:
		date = input("Введите год новой книги: ").title()
		if is_valid_year(date):
			return int(date)
		print("❌ Год должен быть числом от 1000 до 2026")
		sleep(0.5)

def input_rating():
	while True:
		rating = input("Введите рейтинг от 1 до 10: ")
		if is_valid_digit(rating):
			return float(rating)
		print("❌ Вводите только числа от 1 до 10.")
		sleep(0.5)

def input_read_status():
	while True:
		is_read = input("Выберите 1 или 2 (Прочитано/Непрочитано): ")
		if is_valid_digit(is_read):
			is_read = int(is_read)
			if 1 > is_read or is_read > 2:
				print("❌ Ошибка. Выберите цифру 1 или 2!")
			else:
				if is_read == 1:
					return True
				else:
					return False
		print("❌ ОШИБКА. ИСПОЛЬЗУЙТЕ ТОЛЬКО ЦИФРЫ")
		sleep(0.5)

def read_status(library, mode):
	if mode == 1:
		return [book for book in library if book['read']]
	else:
		return [book for book in library if book['read'] == False]

def is_duplicate(library, title, author):
	for i in range(0, len(library)):
		book = library[i]

		if book['title'] == title and book['author'] == author:
			return True
	
	return False

def is_valid_year(year):
	if len(year) == 4 and year.isdigit() and 1000 <= int(year) <= 2026:
		return True
	else:
		return False

def is_valid_digit(input_text, data_type=0):
	while True:
		num = input(input_text)
		if num.isdigit():
			return data_type + int(num)
		print("❌ Вводите только цифры.")

def find_book(the_library, is_book_num, count_objects):
	display_books(the_library)

	for book in the_library:
		count_objects += 1
		if is_book_num - 1 == count_objects:
			return book, is_book_num
			
	return "❌ Нет книги с таким №", False

start()

select_option = is_valid_digit("Выберите пункт: ")

while select_option != 6:

	# 1. Вывести все книги
	if select_option == 1:
		print("1. Вывести все книги")
		print("2. Поиск по названию")
		print("3. Фильтровать по авторам")
		print("4. Фильтровать по статусу прочтения")
		print("-------------------------------------")

		select_filter = int(input("Выберите пункт: "))

		# 1. Вывести все книги
		if select_filter == 1:
			display_books(THE_LIBRARY)
			input("Нажмите Enter чтобы продолжить...")

		# 2. Поиск по названию
		elif select_filter == 2:
			search_book = input("Поиск (по названию): ")
			if search_book == "":
				print("❌ Ошибка. Пустая строка")
			else:
				print(f"\n🔎 Поиск: {search_book}")
				print("Возможные варианты: ")

				number_book = 0

				for book in THE_LIBRARY:
					if search_book.title() in book['title']:
						number_book += 1
						display_book(book, number_book)
					sleep(0.5)
				print("---------------------------")

		# 3. Фильтровать по авторам
		elif select_filter == 3:
			
			author_fio = input("Введите ФИО Автора: ").title()
			books = get_books_by_author(THE_LIBRARY, author_fio)

			if books == []:
				print("\nТакого автора нет в Библиотеке!")
			else:
				print(f"\nКниги автора: {author_fio}")
				print("-----------------------------------")

				display_books(books)

				print("\n-----------------------------------")

		# 4. Фильтровать по статусу прочтения
		elif select_filter == 4:
			print("1. Вывести прочитанные")
			print("2. Вывести непрочитанные")

			select_category = int(input("Выберите пункт: "))

			books = read_status(THE_LIBRARY, select_category)
			number_book = 0

			# 1. Прочитанные книги
			if select_category == 1:
				print("\nНиже прочитанные вами книги:")
				print("---------------------------")

				if books != []:
					display_books(books)
				else:
					print('Прочитанных книг нет.')
					
				print("---------------------------")

			# 2. Непрочитанные книги
			elif select_category == 2:
				print("\nНиже НЕпрочитанные вами книги:")
				print("---------------------------")

				if books != []:
					display_books(books)
				else:
					print('Непрочитанных книг нет.')

				print("---------------------------")
			else:
				print('Вводи только 1 или 2.')

	# 2. Статистика
	elif select_option == 2:
		print("\n1. Авторы из Библиотеки:\n")
		print(*sorted({book['author'] for book in THE_LIBRARY}), sep="\n")
		print("----------------------")
		input("Нажмите Enter чтобы продолжить...")
		sleep(1)
		
		print("\n2. Книги, отсортированные по году издания:\n")
		print(*sorted([(int(book['date']), book['title']) for book in THE_LIBRARY]), sep="\n")
		print("----------------------")
		input("Нажмите Enter чтобы продолжить...")
		sleep(1)

		print('\n3. Количество прочитанных и непрочитанных книг:\n')
		print("Прочитанных:", len([(THE_LIBRARY[i]['title']) for i in range(0, len(THE_LIBRARY)) if THE_LIBRARY[i]['read']]), end=", ")
		print("Непрочитанных:", len([(THE_LIBRARY[i]['title']) for i in range(0, len(THE_LIBRARY)) if THE_LIBRARY[i]['read'] == False]))
		input("Нажмите Enter чтобы продолжить...")
		sleep(1)

	# 3. Добавить книгу
	elif select_option == 3:
		genre = input_genre()
		title = input_title()
		author = input_author()
		date_book = input_date()
		rating = input_rating()
		is_read = input_read_status()

		if is_duplicate(THE_LIBRARY, title, author):
			print("📚 Книга уже есть в Библиотеке!")
		else:
			new_book = {"genre" : genre, "title" : title, "author" : author, "date" : date_book, "rating" : rating, "read" : is_read}
			THE_LIBRARY.append(new_book)
			print("\n📗 Книга успешно добавлена")
			input("Нажмите Enter чтобы продолжить...")
					
	# 4. Изменить информацию о книге
	elif select_option == 4:
		print("1. Изменить год книги")
		print("2. Изменить автора книги")
		print("3. Изменить название книги")
		print("4. Изменить статус прочтения")
		print("-------------------------------------")
		
		change_menu = is_valid_digit("Выберите опцию: ")

		# 1. Изменить НАЗВАНИЕ книги
		if change_menu == 1:
			book, book_num = find_book(THE_LIBRARY, is_valid_digit("Введите № книги: "), -1)
			
			if book_num:
				while True:
					print('-------------------')
					book['date'] = input(f"Введите новую дату книги <{book['title']}>: ")
					if is_valid_year(book['date']):
						book['date'] = int(book['date'])
						print(f"✅ Книга <{book['title']}> получила новую дату {book['date']}")
						input("Нажмите Enter чтобы продолжить...")
						break
					print("❌ Вводите только числа от 1000 до 2026")
			else:
				print('------------------------')
				print(book)
				input("Нажмите Enter чтобы продолжить...")

		# 2. Изменить АВТОРА книги
		elif change_menu == 2:
			book, book_num = find_book(THE_LIBRARY, is_valid_digit("Введите № книги для смены автора: "), -1)

			if book_num:
				while True:
					print('-------------------')
					book['author'] = input(f"Введите новое ФИО Автора книги <{book['title']}>: ")
					if book['author'].replace(' ', '').isalpha():
						print(f"✅ Книга <{book['title']}> получила нового автора {book['author']}")
						input("Нажмите Enter чтобы продолжить...")
						break
					print("❌ Вводите только буквы.")
			else:
				print('------------------------')
				print(book)
				input("Нажмите Enter чтобы продолжить...")

		# В разработке
		elif change_menu == 3:
			pass
		
		# 4. Изменить СТАТУС прочтения
		elif change_menu == 4:
			book, book_num = find_book(THE_LIBRARY, is_valid_digit("Введите № книги для смены статуса: "), -1)

			if book_num:
				if book['read']:
					book['read'] = False
					print(f"\n✅ Статус: Книга <{book['title']}> Непрочитана (Только что)")
					print("---------------------------------")
				else:
					book['read'] = True
					print(f"\n✅ Статус: Книга <{book['title']}> Прочитана (Только что)")
					print("---------------------------------")

				print("Примечание: Если книга была 'прочитана', статус изменится на 'Непрочитано' и наоборот.\n")
			else:
				print('------------------------')
				print(book)
				input("Нажмите Enter чтобы продолжить...")

	# 5. Удалить книгу
	elif select_option == 5:
		book, book_num = find_book(THE_LIBRARY, is_valid_digit("Введите № книги для удаления: "), -1)

		if book_num:
			confirm = input("\nУдалить?(Y/N): ").lower()
			count_books = -1
		
			if confirm == 'y':
				del THE_LIBRARY[book_num - 1]
				print("Книга была удалена.")
				input("Нажмите Enter чтобы продолжить...")
			elif confirm == 'n':
				print("Операция прервана.")
				input("Нажмите Enter чтобы продолжить...")
			else:
				print("Вводите только Y или N.")
				input("Нажмите Enter чтобы продолжить...")
		else:
			print('------------------------')
			print(book)
			input("Нажмите Enter чтобы продолжить...")

	start()

	select_option = is_valid_digit("Выберите пункт: ")
