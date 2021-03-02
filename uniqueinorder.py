iterable = 'AA'


def unique_in_order(iterable):
  output = []
  for index, letter in enumerate(iterable):
    if letter == iterable[index-1] and len(iterable) != 1:
      continue
    output.append(letter)
  if len(output) == 0:
    output.append(iterable[0])
  return output


unique_in_order(iterable)




def unique_in_order(iterable):
    output = []
    for index, letter in enumerate(iterable):
        if letter == iterable[index-1] and len(iterable) != 1:
            continue
        output.append(letter)
    if len(output) == 0:
        output.append(iterable[0])
    return output
  
  
def alphabet_position(text):
  text = text.lower()
  keys = {key: value for key, value in zip('abcdefghijklmnopqrstuvwxyz', range(1,27))}
  textnums = [keys[x] for x in text if x in keys]
  textnums = ''.join(str(textnums))
  return textnums.strip("[]")

text = "The sunset sets at twelve o' clock."
text = "The narwhal bacons at midnight."
string = alphabet_position(text)

