

# 번호 제목 작성자 의견제출기관 등록일

# 파일 읽어서 번호 제목 등 타이틀 제거 해서 다시 파일로 저장함
# with open("lawlist.txt", mode="r") as file:
#     content = list()
#     with open("lawlist_title-remove.txt", mode="w") as file2:
#         for f in file:
#             if f.find("의견제출기관") != -1:
#                 continue
#             file2.writelines(f);

agreement = 0;
opposition = 0;
content = list()
tempStr = 1
with open("lawlist_title-remove.txt", mode="r") as file:
    with open("lawlist_graph-data.txt", mode="w") as file2:
        for f in file:
            if f.find("찬성") != -1:
                agreement += 1;
                file2.writelines(str(tempStr) + ' -1\n')
                tempStr+=1;
            elif f.find("반대") != -1:
                opposition += 1;
                file2.writelines(str(tempStr) + ' +1\n')
                tempStr+=1;