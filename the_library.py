# ✅ Задача 1. Перепиши фильтр по авторам через функцию
# Задача 2. Исправь баг: Название и Автор Книги должны быть буквами

from time import sleep

THE_LIBRARY = [
			{"title" : "Бусидо", "author" : "Юдзан Дайдодзи", "date" : 1998, "read" : False},
			{"title" : "Хагакурэ", "author" : "Юдзан Дайдодзи", "date" : 2000, "read" : False},
			{"title" : "Метро 2033", "author" : "Дмитрий Глуховский", "date" : 2005, "read" : True}
]

def start():
	print("\n         📚 Моя Библиотека\n")
	print("1. Книги")
	print("2. Статистика")
	print("3. Добавить книгу")
	print("4. Изменить статус прочтения")
	print("5. Удалить книгу")
	print("-------------------------------------")
	print("6. Выйти из Библиотеки")
	print("-------------------------------------")

def info_book(the_book, number_book):
	print(f"\n📔 Информация о книге №{number_book}:")
	print()
	print(f"Название: {the_book['title']}")
	print(f"Автор: {the_book['author']}")
	print(f"Год: {the_book['date']}")
	print(f"Прочитано: {display_read_status(the_book['read'])}")

def get_books_by_author(library, author):
	books = [library[i] for i in range(0, len(library)) if author[0] in library[i]['author'][0]]

	return books

def display_read_status(is_read):
	return ('Нет 📕', 'Да 📗')[is_read]

def display_books(books):
	number_book = 0

	for book in books:
		number_book += 1
		info_book(book, number_book)
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

start()

select_option = -1

while select_option != 6:

	# Вывести информацию о книгах
	if select_option == 1:
		print("1. Вывести все книги")
		print("2. Поиск по названию")
		print("3. Фильтровать по авторам")
		print("4. Фильтровать по статусу прочтения")
		print("-------------------------------------")

		select_filter = int(input("Выберите пункт: "))

		# Вывести все книги
		if select_filter == 1:
			display_books(THE_LIBRARY)
			sleep(0.5)

		elif select_filter == 2:

			search_book = input("Поиск (по названию): ")

			if search_book == "":
				print("❌ Ошибка. Пустая строка")
			else:
				print(f"\n🔎 Поиск: {search_book}")
				print("Возможные варианты: ")

				number_book = 0

				for book in THE_LIBRARY:
					if search_book in book['title']:
						number_book += 1
						info_book(book, number_book)
					sleep(0.5)
				print("---------------------------")

		# Фильтровать по авторам
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

		# Фильтровать по статусу прочтения
		elif select_filter == 4:
			print("1. Вывести прочитанные")
			print("2. Вывести непрочитанные")

			select_category = int(input("Выберите пункт: "))

			books = read_status(THE_LIBRARY, select_category)
			number_book = 0

			# Прочитанные книги
			if select_category == 1:
				print("\nНиже прочитанные вами книги:")
				print("---------------------------")

				if books != []:
					display_books(books)
				else:
					print('Прочитанных книг нет.')
					
				print("---------------------------")

			# Непрочитанные книги
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

	# Статистика
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

	# Добавить книгу
	elif select_option == 3:
		name = input("Введите название новой книги: ").title()
		author = input("Автор новой книги: ").title()
		date_book = input("Дата выхода: ")
		is_read = input("Прочитано/Непрочитано? (1, 2): ")

		while is_valid_year(date_book) == False:
			print("❌ Год должен быть числом от 1000 до 2026")
			sleep(0.5)
			date_book = input("Дата выхода: ")
		else:
			date_book = int(date_book)

			while is_read.isdigit() is not True:
				print("❌ Ошибка. Вы ввели не цифры.")
				sleep(0.5)
				is_read = input("Прочитано/Непрочитано? (1, 2): ")
			else:
				is_read = int(is_read)

				if is_read > 2 or is_read < 1:
					print("❌ Ошибка. Выберите цифру 1 или 2!")
				else:
					if is_read == 1:
						is_read = True
					else:
						is_read = False

					if is_duplicate(THE_LIBRARY, name, author):
						print("📚 Книга уже есть в Библиотеке!")
					else:
						new_book = {"title" : name, "author" : author, "date" : date_book, "read" : is_read}
						THE_LIBRARY.append(new_book)
						print("\n📗 Книга успешно добавлена")
						sleep(0.5)
					
	# Изменить статус о прочтении
	elif select_option == 4:
		for book in THE_LIBRARY:
			print(f"📔 Название: «{book['title']}»")
			print(f"Прочитано: {display_read_status(book['read'])}\n")

		change_status = int(input("Выберите книгу для смены статуса: "))
		found_book = False

		print("---------------------------------")

		for j in range(0, len(THE_LIBRARY)):
			if change_status - 1 == j:
				found_book = True
				book = THE_LIBRARY[j]
				print(f"📔 Название: {book['title']}")

				if book['read']:
					book['read'] = False
					print(f"\nСтатус: Непрочитано (Только что)")
					print("---------------------------------")
				elif book['read'] == False:
					book['read'] = True
					print(f"\nСтатус: Прочитано (Только что)")
					print("---------------------------------")

		print(('❌ Нет книги с таким №', '')[found_book])
		print("Примечание: Если книга была 'прочитана', статус изменится на 'Непрочитано' и наоборот.\n")

	# Удалить книгу
	elif select_option == 5:

		found_book = False
		
		delete_book = input("Введите № книги для удаления: ")
		
		while delete_book.isdigit() is not True:
			print("❌ Ошибка. Вы ввели не цифры.")
			sleep(0.5)
			delete_book = input("Введите № книги для удаления: ")
		else:
			delete_book = int(delete_book) - 1

		for i in range(0, len(THE_LIBRARY)):
			if delete_book == i:
				found_book = True
				print("Будет удалена следующая книга: \n")
				number_book = delete_book
				info_book(THE_LIBRARY[i], number_book + 1)
				sleep(0.5)
				
				confirm = str(input("\nУдалить?(Y/N): ")).lower()

				if confirm == 'y':
					del THE_LIBRARY[number_book]
					print("Книга была удалена.")
					sleep(0.5)
				elif confirm == 'n':
					print("Операция прервана.")
					sleep(0.5)
				else:
					print("Вводите только Y или N.")
					sleep(0.5)

		print(('❌ Нет книги с таким №', '')[found_book])

	start()

	try:
		select_option = int(input("Выберите пункт: "))
	except ValueError:
		print("❌ Ошибка. Вы ввели не цифры.\n")
		select_option = -1
