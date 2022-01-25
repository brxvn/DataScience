from json.tool import main

def run():
  my_lis = [1, "hello", True, 4.5]
  my_dict = {"firstname":"Bryan", "lastname":"González", "age":25}

  super_list = [
    {"firstname":"Bryan", "lastname":"González", "age":25},
    {"firstname":"Ramon", "lastname":"González", "age":25},
    {"firstname":"Rene", "lastname":"González", "age":25},
    {"firstname":"Valeria", "lastname":"González", "age":25}, 
    {"firstname":"Kenia", "lastname":"González", "age":25},
  ]

  super_dict = {
    "natural_numbers": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "integer_numbers": [-2, -1, 0, 1, 2],
    "floating_numbers": [1.1, 1.2, 1.3, 1.4, 1.5],
  }

  for value in super_list:
    print(f"{value}")


if __name__ == '__main__':
  run()