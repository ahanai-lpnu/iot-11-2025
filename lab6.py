class MyFileNotFoundError(Exception):
    pass

class MyFileCorruptedError(Exception):
    pass

class GradeError(Exception):
    pass

def logged(exception_cls, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_cls as e:
                err_msg = f"Помилка в {func.__name__}: {e}"
                if mode == "console":
                    print(err_msg)
                elif mode == "file":
                    try:
                        with open("errors.log", "a", encoding="utf-8") as f:
                            f.write(err_msg + "\n")
                        print("Помилку записано у файл errors.log")
                    except:
                        print("Не вдалося записати лог файл")
                raise e
            except Exception as e:
                print(f"Невідома помилка в {func.__name__}: {e}")
                raise e
        return wrapper
    return decorator

class FileManager:
    def __init__(self, path, filename):
        sep = "/"
        if path.endswith("/") or path.endswith("\\"):
            sep = ""
        self.full_path = path + sep + filename
        
        print(f"Перевіряю наявність файлу: {self.full_path}")
        try:
            f = open(self.full_path, "r")
            f.close()
            print("Файл знайдено.")
        except FileNotFoundError:
            raise MyFileNotFoundError(f"Файл не знайдено: {self.full_path}")

    @logged(MyFileCorruptedError, mode="console")
    def read_file(self):
        print(" Читаю файл...")
        data = []
        try:
            with open(self.full_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    clean = line.strip()
                    if len(clean) > 0:
                        parts = clean.split(",")
                        data.append(parts)
            return data
        except Exception as e:
            raise MyFileCorruptedError(f"Помилка читання: {e}")

    @logged(MyFileCorruptedError, mode="file")
    def write_file(self, data):
        print("Записую у файл...")
        try:
            with open(self.full_path, "w", encoding="utf-8") as f:
                for row in data:
                    line = ",".join(str(x) for x in row)
                    f.write(line + "\n")
        except Exception as e:
            raise MyFileCorruptedError(f"Помилка запису: {e}")

    def add_subject_grade(self, subject, grade):
        print(f"Обробка предмета: {subject} з оцінкою {grade}")
        current_data = self.read_file()
        
        if len(current_data) > 0:
            header = current_data[0]
            body = current_data[1:]
        else:
            header = ["Subject", "Grade"]
            body = []

        found = False
        for row in body:
            if row[0] == subject:
                found = True
                try:
                    old_grade = int(row[1])
                except ValueError:
                    old_grade = 0
                
                if grade <= old_grade:
                    raise GradeError(f"Нова оцінка ({grade}) не вища за стару ({old_grade})!")
                else:
                    print(f"Оновлюю оцінку {old_grade} -> {grade}")
                    row[1] = str(grade)
                break
        
        if not found:
            try:
                row = next(r for r in body if r[0] == subject)

                try:
                    old_grade = int(row[1])
                except ValueError:
                    old_grade = 0
            
                if grade <= old_grade:
                    raise GradeError(f"Нова оцінка ({grade}) не вища за стару ({old_grade})!")
                else:
                    print(f"Оновлюю оцінку {old_grade} -> {grade}")
                    row[1] = str(grade)

        body.sort(key=lambda x: int(x[1]), reverse=True)
        
        final_data = [header] + body
        self.write_file(final_data)


def main():
    filename = "grades.csv"
    try:
        f = open(filename, "w", encoding="utf-8")
        f.write("Subject,Grade\n") 
        f.write("Math,80\n")
        f.write("History,75\n")
        f.close()
        print("Старий файл перезаписано, створено нові тестові дані.")
    except Exception as e:
        print(f"Не вдалося підготувати файл: {e}")
        return

    try:
        manager = FileManager(".", filename)
        print("\nДодаємо Python (100)")
        try:
            manager.add_subject_grade("Python", 100)
        except GradeError as e:
            print(f"Увага: {e}")

        print("\nПокращуємо Math (з 80 на 95)")
        try:
            manager.add_subject_grade("Math", 95)
        except GradeError as e:
            print(f"Увага: {e}")

        print("\nПробуємо додати ту саму оцінку для Python (100)")
        try:
            manager.add_subject_grade("Python", 100)
        except GradeError as e:
            print(f"Успішно спіймали очікувану помилку: {e}")

        print("\nПробуємо погіршити History (з 75 на 60)")
        try:
            manager.add_subject_grade("History", 60)
        except GradeError as e:
            print(f"Успішно спіймали очікувану помилку: {e}")

        print("\nФінальний результат у файлі:")
        final_data = manager.read_file()
        for line in final_data:
            print(line)

    except MyFileNotFoundError as e:
        print(f"Головна помилка файлу: {e}")
    except MyFileCorruptedError as e:
        print(f"Файл пошкоджено: {e}")
    except Exception as e:
        print(f"Критична помилка: {e}")

if __name__ == "__main__":
    main()
