from find_article import findarticle
import webbrowser

content = "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>".replace("\n","<br>")

title = "<title>Lorem Ipsum</title>"

favicon = '<link rel="shortcut icon" type="image/png" href="https://en.wikipedia.org/static/favicon/wikipedia.ico"/>'

article_title = "<h1>Lorem Ipsum Ur mom Big Dumb</h1><br>"

webbrowser.open('data:text/html,<html><head><style>body{margin: 5%;}h1{font-family: "Times New Roman", Times, Seriff; font-weight: lighter;}</style>' + title + favicon + "</head><body>" + article_title + content + "</body></html>")
