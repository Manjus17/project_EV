from datetime import datetime

def generate_id():
        current_time = datetime.now()
        id_str = str(current_time)
        id_str = remove_non_numeric_characters(id_str)
        n = int(id_str)
        fi = format(n, 'x')
        return fi

def remove_non_numeric_characters(input_str):
        return ''.join(char for char in input_str if char.isdigit())

value = generate_id()
print(value)