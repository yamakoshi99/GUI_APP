import flet
from flet import ElevatedButton, Page, TextField, Column, Row


def main(page: flet.Page):
    page.title = "メインアプリ"

    # カウンターアプリのUIを格納するコンテナ
    counter_container = Column()
    counter_container.visible = False  # 初期状態では非表示

    txt_count = TextField(value="0", text_align="right", width=100)
    btn_count_up = ElevatedButton(text="カウントアップ")
    btn_count_down = ElevatedButton(text="カウントダウン")
    btn_count_reset = ElevatedButton(text="カウントリセット")

    # カウントを増やす関数
    def count_up(e):
        txt_count.value = str(int(txt_count.value) + 1)
        page.update()

    # カウントを減らす関数
    def count_down(e):
        txt_count.value = str(int(txt_count.value) - 1)
        page.update()

    # カウントをリセットする関数
    def count_reset(e):
        txt_count.value = "0"
        page.update()

    btn_count_up.on_click = count_up
    btn_count_down.on_click = count_down
    btn_count_reset.on_click = count_reset

    # カウンターアプリのコンテナにウィジェットを追加
    counter_container.controls.extend(
        [txt_count, btn_count_up, btn_count_down, btn_count_reset]
    )
    page.add(counter_container)

    # カウントアプリを表示/非表示する関数
    def show_counter_app(e):
        counter_container.visible = (
            not counter_container.visible
        )  # 表示状態を切り替える
        page.update()

    # カウントアプリを開くためのボタンを追加
    btn_open_counter = ElevatedButton(text="カウントアプリ", on_click=show_counter_app)
    page.add(btn_open_counter)

    # 賃金計算アプリのUI
    wage_container = Column()
    wage_container.visible = False  # 初期状態では非表示

    txt_wage = TextField(label="時給", value="", text_align="right", width=100)
    txt_hours = TextField(label="時間", value="", text_align="right", width=100)
    txt_minutes = TextField(label="分", value="", text_align="right", width=100)
    txt_seconds = TextField(label="秒", value="", text_align="right", width=100)
    txt_result = TextField(
        label="合計金額", value="", text_align="right", width=100, read_only=True
    )
    btn_calculate = ElevatedButton(text="計算")

    # 賃金を計算する関数
    def calculate_wage(e):
        try:
            wage = float(txt_wage.value)  # 時給
            hours = float(txt_hours.value)  # 時間
            minutes = float(txt_minutes.value)  # 分
            seconds = float(txt_seconds.value)  # 秒

            # 分と秒を時間に変換
            total_hours = hours + minutes / 60 + seconds / 3600

            # 賃金計算
            total = wage * total_hours
            txt_result.value = str(total) + "円"
        except ValueError:
            txt_result.value = "入力エラー"
        page.update()

    btn_calculate.on_click = calculate_wage

    # 賃金計算アプリのコンテナにウィジェットを追加
    wage_container.controls.extend(
        [txt_wage, txt_hours, txt_minutes, txt_seconds, btn_calculate, txt_result]
    )
    page.add(wage_container)

    # 賃金計算アプリを表示/非表示する関数
    def show_wage_app(e):
        wage_container.visible = not wage_container.visible
        page.update()

    # 賃金計算アプリを開くためのボタンを追加
    btn_open_wage = ElevatedButton(text="賃金計算アプリ", on_click=show_wage_app)
    page.add(btn_open_wage)

    # 省略: その他のUIコンポーネントやイベントハンドラ...


# アプリケーションを起動
flet.app(target=main)
