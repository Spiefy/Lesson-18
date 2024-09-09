def test_function():
    def inner_function():
        a = "Я в области видимости функции test_function"
        print(a)
    inner_function()


# inner_function() При использовании вне функции не может определить имя
test_function()
