import os


def get_condition_task(task_name, seed=None):
    """
    Возвращает текст условия задания для указанного названия задания и seed.

    Args:
        task_name (str): Название задания.
        seed (int): Seed для выбора варианта задания. Если не указан, используется значение по умолчанию (None).

    Returns:
        str: Текст условия задания.

    Raises:
        FileNotFoundError: Если файл с условием задания не найден.
    """
    base_path = os.path.dirname(__file__)
    task_path = os.path.join(base_path, 'tasks', task_name + '.txt')

    if not os.path.exists(task_path):
        raise FileNotFoundError(f"Описание задания для '{task_name}' не найдено.")

    with open(task_path, 'r', encoding='utf-8') as file:
        description = file.read()

    return description


def main():
    print(get_condition_task('basics_condition'))


if __name__ == '__main__':
    main()
