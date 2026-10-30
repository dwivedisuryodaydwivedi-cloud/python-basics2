"""
  *                *
    *            *
      *        *
        *    *
          *
        *    *
      *        *
    *            *
  *                *
"""
# Upper part of the diamond
for i in range(1, 6):  # Outer loop runs from 1 to 5 (5 rows)

    for j in range(1, i+1):  # Prints left-side spaces, increasing in each row
        print(" ", end=" ")

    print("*", end="")  # Prints the left-side star

    for k in range(i, 5):  # Controls the middle space, decreasing in each row
        print("  ", end="  ")

    if i != 5:  # Prints the right-side star except in the last row
        print("*")
    else:
        print()


# Lower part of the diamond
for i in range(4, 0, -1):  # Outer loop runs from 4 to 1 (4 rows)

    for j in range(1, i+1):  # Prints left-side spaces, decreasing in each row
        print(" ", end=" ")

    print("*", end="")  # Prints the left-side star

    for k in range(i, 5):  # Controls the middle space, increasing in each row
      print("  ", end="  ")
   print("*")  # Prints the right-side star
