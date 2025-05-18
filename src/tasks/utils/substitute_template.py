import re


def substitute_template(template: str, params: dict[str, str]) -> str:
    """
    Подставляет в шаблон template параметры param
    """
    pattern = re.compile(r'\$\$(\w+)\$\$')

    def replacer(match):
        key = match.group(1)
        return params.get(key, match.group(0))

    return pattern.sub(replacer, template)
