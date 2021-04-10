import time
import datetime
import PySimpleGUI as sg
import sys
import simpleaudio as sa

sg.theme('default 1')

dt_now = datetime.datetime.now()
###アラームの設定
wave_obj = sa.WaveObject.from_wave_file("木山裕策－home.wav")
###時間設定[入力]
layout1 = [
    [sg.Text('あるイベントまでの残り時間をお知らせします',font=('',24),pad=(((10,10),(10,10))))],
    [sg.Text('イベント名：',font=('',18)), sg.InputText(key='-event-')],
    [sg.Text('日時：',font=('',18)),
    sg.InputText(dt_now.year, key='-year-',size=(8,1)),sg.Text('年',font=('',18)),
    sg.Combo([f'{i}' for i in range(1,13)],key='-month-',size=(8,1)),sg.Text('月',font=('',18)),
    sg.InputText(key='-day-',size=(8,1)),sg.Text('日',font=('',18)),
    sg.InputText(key='-hour-',size=(8,1)),sg.Text('時',font=('',18)),],
    [sg.Button(image_filename='player_button.png',key='実行ボタン') ,sg.Text('',key='-出力-',size=(30,1))],
]
window1 = sg.Window('修論タイマー', layout1)
while True:
    event, values = window1.read()
    if event in (None,):
        sys.exit()
    elif event in '実行ボタン':
        try:
            year=int(values['-year-'])
            month=int(values['-month-'])
            day=int(values['-day-'])
            hour=int(values['-hour-'])
            date = datetime.datetime(year=year,month=month,day=day, hour=hour)
            break
        except:
            window1['-出力-'].update('正しく入力できてません。',font=('',18))
window1.close()
# ウィンドウの内容を定義する
layout2 = [
            [sg.Text(str(dt_now.year)+"年", key='years',font=('',50))],
            [sg.Text(values['-event-']+"締め切りまで・・・", key='-output-',font=('',50))],
            [sg.Text(size=(25,1), key='-clock-',enable_events=True ,font=("Helvetica", 60),text_color='red')],
            [sg.Text("です。", key='desu',font=('',50))],
            [sg.Image(filename='ganbarou.png',key=f'{i}') for i in range(1,10)]
          ]
# ウィンドウを作成する
window2 = sg.Window('修論タイマー', layout2,alpha_channel=0.9)
# イベントループを使用してウィンドウを表示し、対話する
while True:
    event, values = window2.read(timeout=30,timeout_key='-timeout-')
    if event in (None,):
        sys.exit()
    elif event in '-timeout-':
        deadline = date - datetime.datetime.now()
        if deadline.days >= 0:
            window2['-clock-'].update("残り"+str(deadline))
        else:
            break
window2['-output-'].update('')
window2['desu'].update('')
window2['-clock-'].update('提出は締め切られています。')
play_obj = wave_obj.play()
while True:
    event, values = window2.read()
    if event in (None,):
        break
window2.close()
