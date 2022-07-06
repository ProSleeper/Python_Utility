
import os

# sql lee/bob 데이터 맥에 넣는 도중 못 넣은 데이터들만 추출하는 코드
# print(os.getcwd())

# count = 0
# with open(os.getcwd() + "/FileLineRead/SQL Error/Sales insert error.txt", "r") as f:
#     while True:
#         readedLine1 = f.readline()
#         if (readedLine1.find('==========================[Start Time') != -1):
#             readedLine2 = f.readline()
#             readedLine3 = f.readline()
#             readedLine4 = f.readline()
#             readedLine5 = f.readline()
#             if (readedLine5.find('실행 완료.') == -1):
#                 readedLine6 = f.readline();
#                 readedLine7 = f.readline();
#                 readedLine8 = f.readline();
#                 count += 1
#                 with open(os.getcwd() + "/FileLineRead/SQL Error/Sales Only insert error.txt", "a") as file:
#                     file.writelines(readedLine1);
#                     file.writelines(readedLine2);
#                     file.writelines(readedLine3);
#                     file.writelines(readedLine4);
#                     file.writelines(readedLine5);
#                     file.writelines(readedLine6);
#                     file.writelines(readedLine7); 
#                     file.writelines(readedLine8);
        
#         if not readedLine1: break;
# print(count)
# print("퉤스트")

print(os.getcwd())

count = 0
with open(os.getcwd() + "/FileLineRead/SQL Error/error/Company Only insert error.txt", "r") as f:
    while True:
        readedLine = f.readline()
        if (readedLine.find('SQL > INSERT INTO') != -1):
            with open(os.getcwd() + "/FileLineRead/SQL Error/error/Company Only last insert error.txt", "a") as file:
                file.writelines(readedLine);
        
        if not readedLine: break;


print(count)
print("퉤스트")