from urllib import request
import json, time, textwrap


class GetNews(object):
    def __init__(self):
        self.news = []
        self.item_name = {'edited_title', 'summary', 'icon', 'url', 'hour', 'time'}
        self.url = 'https://digestapit.geeks.vc/v1/articles'

    def get_data(self):

        try:
            head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
            url = request.Request(self.url, headers=head)
            html = request.urlopen(url)
            h = html.read().decode('utf-8')
            new_data = json.loads(h)
            return new_data
        except:
            new_data = {}
            print('this is some error')
            return new_data

    @staticmethod
    def write_in(args, file):

        for key, value in args.items():
            file.write(('{0}:{1}').format(format(key, '<13'),
                                          textwrap.fill(value, 60, subsequent_indent=' ' * 13)) + '\n')

    def get_news(self):

        with open('news.txt', 'w', encoding='utf-8') as f:
            data = self.get_data()
            for item in reversed(data['data']):
                c_time = item['updatedAt']
                n_time = time.time()
                hour = round((n_time - c_time) / 3600)

                item.update({'hour': str(hour)})
                item.update({'time': str(c_time)})
                new = {key: value for key, value in item.items() if key in self.item_name if int(hour) < 10}
                if new:
                    self.news.append(new)
                self.write_in(new, f)
                f.write('\n\n')
            try:
                self.news = self.news[0:7]
            except:
                self.news = self.news
            color = ['#fd1900', '#fb6205', '#fdf001', '#00d521', '#00bcf0', '#000dfc', '#9e1eff']
            color = (c for c in color)
            for item in self.news:
                item.update({'color': next(color)})
            return self.news


n = GetNews()
n.get_news()
new = n.news
for i in new:
    print(i)
