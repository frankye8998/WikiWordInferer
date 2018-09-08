from find_article import findarticle
import webbrowser

webbrowser.open("data:text/html,<html><body><p>" + findarticle(input("Article: ")).replace("\n","<br>") + "</p></body></html>")
