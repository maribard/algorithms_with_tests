import api_regres
'''
Let's say we wanted to extract the top N URLs instead of the single top URL. Can you change your code to make N a configurable parameter?

Expected output for N = 15 (number of occurrences is not needed):

('http://www.example.com', 1170)
('http://www.example.com/world', 482)
('http://www.example.com/us', 375)
('http://www.example.com/trends', 286)
('http://www.example.com/travel', 269)
('http://www.example.com/tech', 264)
('http://www.example.com/showbiz', 237)
('http://www.example.com/profile', 220)
('http://www.example.com/photos', 204)
('http://www.example.com/politics', 198)
('http://www.example.com/living', 169)
('http://www.example.com/justice', 164)
('http://www.example.com/opinion', 156)
('http://www.example.com/health', 156)
('http://www.example.com/feedback', 152)
'''

data = api_regres.get("https://public.karat.io/content/q015/urls.txt")

list_with_urls = data.text.split('\n')
dict_with_urls = {}

for url in list_with_urls:
    if url not in dict_with_urls:
        dict_with_urls[url] = 1
    else:
        dict_with_urls[url] += 1

couter = 0
most_common_url = ''

for key, value in dict_with_urls.items():
    if value > couter:
        couter = value
        most_common_url = key

# print(most_common_url, couter)


def show_n_urls(number_of_urls, urls_in_dict):
    sorted_list = dict(sorted(urls_in_dict.items(), key=lambda x: x[1], reverse=True)[:number_of_urls])
    for key, value in sorted_list.items():
        print(key, "->", value)

show_n_urls(15, dict_with_urls)

