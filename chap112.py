print("Hello Python interpreter!")
print("Hello World!")
message = "Hello Python World!"
print(message)
name = "ada lovelace"
print(name.title())  # 单词首字母大写
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)

print("Hello, " + full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"
print(message)

print("Python")
print("\tPython")  # 制表符\t
print("Languages:\nPython\nC\nJavaScript")  # 换行符\n
print("Language:\n\tPython\n\tC\n\tJavaScript")

favorite_language = " python "
print(favorite_language)
print(favorite_language.rstrip())  # 去掉右边right空白
print(favorite_language.lstrip())   # 去掉左边left空白
print(favorite_language.strip())    # 去掉两边的空白
favorite_language = favorite_language.strip()
print(favorite_language)

message = "  \t  Adss "
print(message)
print(message.strip())