sps = [['Иванова Екатерина','Попова Варвара',''],['Участник проекта','Участник проекта','Участник проекта',],['ekaterina.a.ivanova.704@gmail.com','varvara.popova.15@mail.ru','#']]
for i in range(0,2):
    print(f'<img src="img/{i}.jpeg" width="256" height="256">')
    print(f'<h3>Участник проекта:</h3>')
    print(f'<h2><b>{sps[0][i]}</h2>')
    print(f'<h3>{sps[2][i]}</h3></a>')
    print('<hr></hr>')
