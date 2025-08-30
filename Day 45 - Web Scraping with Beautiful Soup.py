# from bs4 import BeautifulSoup

# import requests
# import urllib3

# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# response = requests.get("https://news.ycombinator.com/", verify=False)
# yc_webpage_html_data = response.text

# #print(yc_webpage_html_data)

# soup = BeautifulSoup(yc_webpage_html_data,"html.parser")


 



# for i in range(len(article_texts)):
#     article_text = article_texts[i]
#     article_link = article_links[i] if i < len(article_links) else None
#     article_upvote = article_scorepoints[i] if i < len(article_scorepoints) else None
# articles = [a.get_text(strip=True) for a in soup.select('span.titleline a') if ' ' in a.get_text(strip=True)]
# article_links = [a.get("href") for a in soup.select('span.titleline a') if not (a.get("href", "").startswith("from?site="))] # type: ignore
# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all('span', class_='score')]

# print(f"Article Text: {articles}")
# print(f"Article Link: {article_links}")
# print(f"Article Upvote: {article_upvotes}")


# # TODO 1 - Print out the title and the link for the highest number of votes

# Max_votes = max(article_upvotes)
# print("Max Votes: "+str(Max_votes))
# max_index = article_upvotes.index(Max_votes)

# print("Max Index: "+str(max_index))

# print(f"Highest Article Title: {articles[max_index]}")
# print(f"Highest Article Link: {article_links[max_index]}")

# soupTitle = soup.title
# print(soupTitle)
# if soupTitle is not None:
#     print("Title Name: " + str(soupTitle.name))
# else:
#     print("Title Name: None")

# if soup.title is not None:
#     print(soup.title.string)
# else:
#     print("Title string: None")
# print(soup.prettify())

# print(soup.a)

# all_anchor_tags = soup.find_all("a")
# print(all_anchor_tags)

# texts_of_anchor_tags = [tag.getText() for tag in all_anchor_tags]
# print(texts_of_anchor_tags)


# from bs4.element import Tag

# for tag in all_anchor_tags:
#     print(tag.getText())
#     if isinstance(tag, Tag):
#         getLink = tag.get("href")
#         print("Link: " + str(getLink))
#     else:
#         print("Link: None (Not a Tag object)")

# heading = soup.find(name="h1",id="name")

# if heading is not None:
#     print("Heading Text: " + heading.getText())
# else:
#     print("Heading Text: None")


# section_heading = soup.find(name="h3",class_="heading")
# if section_heading is not None:
#     print("Section Heading Text: " + section_heading.getText())
# else:
#     print("Section Heading Text: None")

# company_url = soup.select_one(selector="p a")

# print(company_url)


# headings = soup.select(selector=".heading")
# print(headings)


# with open("beautiful_soup_quiz.html", encoding="utf-8") as quizHtmlFile:
#     quizHtmlContent = quizHtmlFile.read()
#     beautifult_soup = BeautifulSoup(quizHtmlContent,"html.parser")

# all_a_tags_in_quiz = beautifult_soup.find_all("a")

# print(all_a_tags_in_quiz)



"""  Top 100 movies scrapting using Python Project """

import requests
from bs4 import BeautifulSoup

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL, verify=False)
#print(response.text)
soup = BeautifulSoup(response.text, "html.parser")

top_hundred_movie_titles = [movie.getText(strip=True) for movie in soup.find_all("h3", class_="title") if movie is not None]
reverse_top_hundred_movie_titles = top_hundred_movie_titles[::-1]
print(reverse_top_hundred_movie_titles)

with open("movies.txt","w", encoding="utf-8") as file:
    for movie in reverse_top_hundred_movie_titles:
        file.write(movie + "\n")