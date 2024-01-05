from BinaryTree.bst import BinarySearchTree

political_news_bst = BinarySearchTree()
sports_news_bst = BinarySearchTree()

def display_news_on_date(tree, date):
    news = tree.traverse()
    for news_item in news:
        if news_item[1] == date:
            print(news_item)

political_news = [("Political News 1", "2023-10-01"), ("Political News 2", "2023-10-02"),("Political News 3", "2023-10-03"),
    ("Political News 4", "2023-10-04"),
    ("Political News 5", "2023-10-05")]
sports_news = [("Sports News 1", "2023-10-01"), ("Sports News 2", "2023-10-03"),("Sports News 3", "2023-10-02"),
    ("Sports News 4", "2023-10-04"),
    ("Sports News 5", "2023-10-05")]

for news_item in political_news:
    political_news_bst.insert(news_item)

for news_item in sports_news:
    sports_news_bst.insert(news_item)

display_news_on_date(political_news_bst, "2023-10-02")
display_news_on_date(sports_news_bst, "2023-10-01")

def get_news_between_dates(tree, start_date, end_date):
    news = tree.traverse()
    filtered_news = []

    for news_item in news:
        if start_date <= news_item[1] <= end_date:
            filtered_news.append(news_item)

    return filtered_news

political_news_between_dates = get_news_between_dates(political_news_bst, "2023-10-02", "2023-10-04")
print("Political News between '2023-10-02' and '2023-10-04':")
for news_item in political_news_between_dates:
    print(news_item)

sports_news_between_dates = get_news_between_dates(sports_news_bst, "2023-10-02", "2023-10-05")
print("\nSports News between '2023-10-02' and '2023-10-05':")
for news_item in sports_news_between_dates:
    print(news_item)
