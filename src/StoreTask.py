class StoreTask:
    _instances = {}
    @classmethod
    def get_instances(cls, class_name):
        return cls._instances.get(class_name, [])

    @classmethod
    def register_instance(cls, instance):
        class_name = instance.__class__.__name__
        if class_name not in cls._instances:
            cls._instances[class_name] = []
        cls._instances[class_name].append(instance)