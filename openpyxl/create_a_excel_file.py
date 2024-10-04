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
{file_name} を保存しました。
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
{file_name} を保存しました。
""")


        except Exception as err:
            print(f"""\
おお、残念！　例外が投げられてしまった！  
{err=}  {type(err)=}

以下はスタックトレース表示じゃ。
{traceback.format_exc()}
""")
