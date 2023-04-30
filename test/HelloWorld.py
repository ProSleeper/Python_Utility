class MyClass:
    @classmethod
    def my_class_method(cls, arg1, arg2):
        cls.varr = 2;
        print("This is a class method")
        print(cls, arg1, arg2)
        
    @classmethod
    def my_class_method2(cls, arg1, arg2):
        print(cls.varr);

# 클래스명으로 클래스 메소드 호출
MyClass.my_class_method2("hello", "world")
MyClass.my_class_method("hello", "world")
MyClass.my_class_method2("hello", "world")