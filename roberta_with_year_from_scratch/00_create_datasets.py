import datetime

with open('../test-A/in.tsv','r') as f_in, open(f'./test-A_in.csv', 'w') as f_hf:
    f_hf.write('text\n')
    for line_in in f_in:
        year_cont, date, text = line_in.rstrip('\n').split('\t')
        d = datetime.datetime.strptime(date,"%Y%m%d")
        day_of_year = str(d.timetuple().tm_yday)
        day_of_month = str(d.day)
        month = str(d.month)
        year = str(d.year)
        weekday = str(d.weekday())
        day_of_year = str(d.timetuple().tm_yday)
        text = 'year: ' + year +' month: ' + month + ' day: ' + day_of_month + ' weekday: ' + weekday + ' '+ text
        f_hf.write(text +'\n')


for dataset in 'train', 'dev-0':
    with open(f'../{dataset}/in.tsv') as f_in, open(f'./{dataset}_in.csv','w') as f_hf:
        f_hf.write('text\n')
        for line_in in f_in:
            year_cont,date,text = line_in.rstrip('\n').split('\t')
            d = datetime.datetime.strptime(date,"%Y%m%d")
            day_of_year = str(d.timetuple().tm_yday)
            day_of_month = str(d.day)
            month = str(d.month)
            year = str(d.year)
            weekday = str(d.weekday())
            day_of_year = str(d.timetuple().tm_yday)
            text = 'year: ' + year +' month: ' + month + ' day: ' + day_of_month + ' weekday: ' + weekday + ' '+ text
            f_hf.write(text +'\n')

