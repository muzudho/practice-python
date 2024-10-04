#
# cd openpyxl
# python create_a_excel_file.py
#
# Excel ファイルを作ろう
#
import traceback
import openpyxl as xl
import os


########################################
# コマンドから実行時
########################################
if __name__ == '__main__':

    try:
        # ワークブックの作成
        wb = xl.Workbook()

        while True:
            file_name = input(f"""\
Excel ファイルを作ろう！
例： hello.xlsx
ファイル名を入力してください> """)

            if os.path.isfile(file_name):
                command = input(f"""\
{file_name} という名前のファイルは既にあります。
上書きしますか(Y/n)? """)

                if command == 'n':
                    continue

            break

        wb.save(file_name)

        print(f"""\
{file_name} を保存しました
""")

        sheet_name = input(f"""\
最初に作るシートの名前を決めよう！
例： Hello world
シート名を入力してください> """)

        # 最初に Sheet という名前のシートができているので、それを参照します
        ws = wb["Sheet"]

        # シートの名前を変更します
        ws.title = sheet_name
        wb.save(file_name)

        print(f"""\
シートの名前を {ws.title} に変更しました。
{file_name} を保存しました
""")

        column_name = input(f"""\
{ws.title} シートの左上のセルに列名を入れてみましょう。
例: Name
列名を入力してください> """)

        ws['A1'] = column_name
        wb.save(file_name)

        print(f"""\
{ws.title} シートの左上のセルに {column_name} と入れました。
{file_name} を保存しました
""")


        dust = input(f"""\
{ws.title} シートの１行目について、２列目から Age, Address, Phone, Web site と入れるサンプルを示します。
何か入力してエンターキーを押してください> """)

        column_names = [
            'Age',
            'Address',
            'Phone',
            'Web site',
        ]

        for index, column_name in enumerate(column_names, 2):   # 2 列目から
            cell_address = f'{xl.utils.get_column_letter(index)}1'
            ws[cell_address] = column_name

        wb.save(file_name)

        print(f"""\
{ws.title} シートの１行目について、２列目から列名を入れました。
{file_name} を保存しました
""")

        sheet_name = input(f"""\
２つ目のシートを新規作成するサンプルを示します。
例： Good morning
シート名を入力してください> """)

        ws = wb.create_sheet(title=sheet_name)
        wb.save(file_name)

        print(f"""\
{ws.title} シートを作成しました。
{file_name} を保存しました
""")


    except Exception as err:
        print(f"""\
おお、残念！　例外が投げられてしまった！  
{type(err)=}  {err=}

以下はスタックトレース表示じゃ。
{traceback.format_exc()}
""")
