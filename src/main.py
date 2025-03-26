from tasks import StoreTask


task = StoreTask.get_task('basic_task')

if task is None:
    raise ValueError("Task 'basic_task' not found")

dict_task = {
    'condition': task.get_condition_task(),
    'code': task.get_code_template(),
    'coderunner': task.get_template_coderunner()
}

for t in dict_task:
    print(t + ': ')
    print(dict_task[t])
    print()
