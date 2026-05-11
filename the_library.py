# Beta v0.4
# ✅ Задача 1. Исправить ошибку в info_book и передавать данные явно
# ✅ Задача 2. Убрать try/except и сделать безопасный ввод без падений
# Задача 3. Убрать дублирование кода — создать вспомогательные функции

from time import sleep

THE_LIBRARY = [
			{"title" : "Бусидо", "author" : "Юдзан Дайдодзи", "year" : "1998", "read" : False},
			{"title" : "Хагакурэ", "author" : "Юдзан Дайдодзи", "year" : "2000", "read" : False},
			{"title" : "Метро 2033", "author" : "Дмитрий Глуховский", "year" : "2005", "read" : True}
]

def start():
	print("\n         📚 Моя Библиотека\n")
	print("1. Вывести информацию о книгах")
	print("2. Добавить книгу")
	print("3. Изменить статус прочтения")
	print("4. Удалить книгу")
	print("-------------------------------------")
	print("5. Выйти из Библиотеки")
	print("-------------------------------------")

def read_status(is_read):
	return ('Нет 📕', 'Да 📗')[is_read]

def info_book(the_book, number_book):
	print(f"\n📔 Информация о книге №{number_book}:")
	print()
	print(f"Название: {the_book['title']}")
	print(f"Автор: {the_book['author']}")
	print(f"Год: {the_book['year']}")
	print(f"Прочитано: {read_status(the_book['read'])}")

def display_books():
	pass

start()

select_option = -1

while select_option != 5:

	number_book = 0

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
			for i in range(0, len(THE_LIBRARY)):
				number_book += 1
				info_book(THE_LIBRARY[i], number_book)
				sleep(0.5)
			sleep(0.5)

		elif select_filter == 2:

			search_book = input("Поиск (по названию): ")

			if search_book == "":
				print("❌ Ошибка. Пустая строка")
			else:
				print(f"\n🔎 Поиск: {search_book}")
				print("Возможные варианты: ")

				number_book = 0

				for i in range(0, len(THE_LIBRARY)):
					if search_book in THE_LIBRARY[i]['title']:
						number_book += 1
						info_book(THE_LIBRARY[i], number_book)
					sleep(0.5)
				print("---------------------------")

		# Фильтровать по авторам
		elif select_filter == 3:
			
			author_fio = input("Введите ФИО Автора: ").title()
			found_author = ""
			number_book = 0
			
			for i in range(0, len(THE_LIBRARY)):
				if author_fio == THE_LIBRARY[i]['author'].title():
					found_author = book

			if found_author == "":
				print("\nТакого автора нет в Библиотеке!")
			else:
				print(f"Книги автора: {found_author['author']}")
				print("-----------------------------------")

				for i in range(0, len(THE_LIBRARY)):
					if found_author['author'] in THE_LIBRARY[i]['author']:
						number_book += 1
						info_book(THE_LIBRARY[i], number_book)
						sleep(0.5)
				print("\n-----------------------------------")

		# Фильтровать по статусу прочтения
		elif select_filter == 4:
			print("1. Вывести прочитанные")
			print("2. Вывести непрочитанные")

			select_category = int(input("Выберите пункт: "))
			number_book = 0

			# Прочитанные книги
			if select_category == 1:
				print("\nНиже прочитанные вами книги:")
				print("---------------------------")

				for i in range(0, len(THE_LIBRARY)):
					if THE_LIBRARY[i]['read']:
						number_book += 1
						info_book(THE_LIBRARY[i], number_book)
					sleep(0.5)
				print("---------------------------")

			# Непрочитанные книги
			elif select_category == 2:
				print("\nНиже НЕпрочитанные вами книги:")
				print("---------------------------")
				for i in range(0, len(THE_LIBRARY)):
					if THE_LIBRARY[i]['read'] == False:
						number_book += 1
						info_book(THE_LIBRARY[i], number_book)
					sleep(0.5)
				print("---------------------------")

	# Добавить книгу
	elif select_option == 2:
		name = input("Введите название новой книги: ")
		author = input("Автор новой книги: ")
		date_book = input("Дата выхода: ")
		is_read = input("Прочитано/Непрочитано? (1, 2): ")

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

				new_book = {"title" : name, "author" : author, "year" : date_book, "read" : is_read}
				THE_LIBRARY.append(new_book)
				print("\n📗 Книга успешно добавлена")
				sleep(0.5)
	# Изменить статус о прочтении
	elif select_option == 3:
		for i in range(0, len(THE_LIBRARY)):
			print(f"📔 Название: «{THE_LIBRARY[i]['title']}»")
			print(f"Прочитано: {read_status(THE_LIBRARY[i]['read'])}\n")

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
	elif select_option == 4:

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
