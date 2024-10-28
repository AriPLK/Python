import os

directory = r'C:\Users\rrrrs\PycharmProjects\Python\Module7\second'
os.walk(directory)

os.path.join(r'C:\Users\rrrrs\PycharmProjects\Python\Module7',
             r'C:\Users\rrrrs\PycharmProjects\Python\Module7\second\third')

print(os.path.getmtime(r'C:\Users\rrrrs\PycharmProjects\Python\Module7\module_7_1.py'))
print(os.path.getsize(r'C:\Users\rrrrs\PycharmProjects\Python\Module7\module_7_1.py'))
print(os.path.dirname(r'C:\Users\rrrrs\PycharmProjects\Python\Module7\module_7_1.py'))
