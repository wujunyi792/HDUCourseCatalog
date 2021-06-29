import openpyxl
import json

workbook = openpyxl.load_workbook("../data/csv/2021-01raw.xlsx")
worksheet = workbook["Sheet1"]
res = []
isTrue = True
count = 0
for row in worksheet.rows:
    if isTrue:
        isTrue = False
        continue
    line = []
    for cell in row:
        line.append(str(cell.value))
    currow = {
        '序号': str(count + 10001),
        '学年': line[0],
        '学期': line[1],
        '星期几': line[2],
        '上课节次': line[3],
        '起始结束周': line[4],
        '课程名称': line[5],
        '姓名': line[6],
        '教师所属学院': line[7],
        '场地上课起始周': line[8],
        '学分': line[9],
        '总学时': line[10],
        '开课学院': line[11],
        '上课地点': line[12],
        '课程性质': line[13],
        '专业组成': line[14],
    }
    count += 1
    res.append(currow)

main_struc = {'total': count, 'rows': res}
# print(main_struc)
main_json = json.dumps(main_struc, ensure_ascii=False)
outfp = open("../data/json/2021new.json", "w", encoding="utf-8")
outfp.write(main_json)
