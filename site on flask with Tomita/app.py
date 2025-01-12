import os
import codecs
from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/exercises")
def exercises():
    return render_template("exercises.html")


@app.route("/extract", methods=["POST"])
def extract():
    txt0 = request.form["txt"]

    # Абсолютные пути
    base_dir = os.path.abspath(os.path.dirname(__file__))
    tomita_dir = os.path.join(base_dir, "tomita")
    input_path = os.path.join(tomita_dir, "input.txt")
    config_path = os.path.join(tomita_dir, "config.proto")
    output_path = os.path.join(tomita_dir, "output.txt")
    tomita_parser_path = os.path.join(tomita_dir, "tomitaparser")

    # Проверка наличия базовой директории
    if not os.path.exists(base_dir):
        return render_template(
            "index.html", error=f"Базовая директория не найдена: {base_dir}"
        )

    # Проверка наличия конфигурационного файла
    if not os.path.exists(config_path):
        return render_template(
            "index.html", error=f"Файл конфигурации не найден: {config_path}"
        )

    # Проверка наличия исполняемого файла
    if not os.path.exists(tomita_parser_path):
        return render_template(
            "index.html",
            error=f"Исполняемый файл Томита парсера не найден: {tomita_parser_path}",
        )

    # Проверка прав доступа к исполняемому файлу
    if not os.access(tomita_parser_path, os.X_OK):
        return render_template(
            "index.html", error=f"Нет прав на выполнение для: {tomita_parser_path}"
        )

    # Запись текста в файл
    try:
        with codecs.open(input_path, "w", "utf-8") as f:
            f.write(str(txt0))
    except Exception as e:
        return render_template(
            "index.html", error=f"Ошибка при записи в файл ввода: {str(e)}"
        )

    # Проверка успешности записи файла
    if not os.path.exists(input_path):
        return render_template(
            "index.html", error=f"Файл ввода не найден после записи: {input_path}"
        )

    # Проверка прав доступа к директории и файлам
    if not os.access(tomita_dir, os.W_OK):
        return render_template(
            "index.html", error=f"Нет прав на запись в директорию: {tomita_dir}"
        )

    # Запуск Томита парсера
    command = [tomita_parser_path, "config.proto"]
    try:
        output = subprocess.check_output(
            command, stderr=subprocess.STDOUT, cwd=tomita_dir
        )
    except subprocess.CalledProcessError as e:
        return render_template(
            "index.html",
            error=f"Ошибка при выполнении Томита парсера: {e.output.decode()}",
        )
    except FileNotFoundError:
        return render_template(
            "index.html", error="Не удалось найти исполняемый файл Томита парсера."
        )
    except Exception as e:
        return render_template(
            "index.html",
            error=f"Неизвестная ошибка при запуске Томита парсера: {str(e)}",
        )

    # Проверка наличия выходного файла
    if not os.path.exists(output_path):
        return render_template(
            "index.html", error=f"Файл результата не найден: {output_path}"
        )

    # Чтение результатов
    try:
        with open(output_path, "r", encoding="utf-8") as f:
            results = f.read()
    except Exception as e:
        return render_template(
            "index.html", error=f"Ошибка при чтении файла результата: {str(e)}"
        )

    return render_template("pretty.html", input_text=txt0, results=results)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
