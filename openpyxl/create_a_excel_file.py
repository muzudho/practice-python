#
# cd openpyxl
# python create_a_excel_file.py
#
# Excel ファイルを作ろう
#
import traceback
import openpyxl as xl


########################################
# コマンドから実行時
########################################
if __name__ == '__main__':
        try:

                # ワークブックの作成
                wb = xl.Workbook()

                file_name = input(f"""\
Excel ファイルを作ろう！
例： hello.xlsx
ファイル名を入力してください> """)

                wb.save(file_name)

                print(f"""\
{file_name} を保存しました。
""")

        except Exception as err:
            print(f"""\
おお、残念！　例外が投げられてしまった！  
{err=}  {type(err)=}

以下はスタックトレース表示じゃ。
{traceback.format_exc()}
""")
