# coffee_bot-codecademy-project
def coffee_bot():
  print('Welcome to the cafe!')
  size = get_size()
  drink_type = get_drink_type()
  print('Alright, thats a '+size+' '+drink_type)
  name = input('Can I get your name pleasse?')
  print('Thanks ',name,'! Your drink will be ready shortly.')
  # print(size)
  # print(drink_type)
def get_drink_type():
  res = input('''What type of drink would you like?
  [a] Brewed Coffee
  [b] Mocha
  [c] Latte''')
  if res == 'a':
    return 'brewedcoffee'
  elif res == 'b':
    return 'mocha'
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()
def order_latte():
  res = input('''And what kind of milk for your latte?
  [a] 2% milk
  [b] Non-fat milk
  [c] Soy milk''')
  if res == 'a':
    return 'latte'
  elif res == 'b':
    return 'non-fat-latte'
  elif res == 'c':
    return 'soylatte'
  else:
    print_message()
    return order_latte()
  
def print_message():
  print('''I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.''')
def get_size():
  res = input('What size drink can I get for you? \n[a] Small\n     [b] Medium \n[c] Large \n> ')
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message()
    return get_size()


# Call coffee_bot()!
coffee_bot()
