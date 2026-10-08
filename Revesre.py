def rev(n):
  result = ""

  for ch in n:
    result = ch + result
  return result

Text = input("Enter the string : " )

print( " revese order : "  , rev(Text))