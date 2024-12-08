import os


commands = [
    # "ng build",
    "cp -r dist/news-article-fe/*  /var/www/html",
    "systemctl restart nginx",
]

for index, command in enumerate(commands):
    print(f"executing step {index+1} >>>>> {command}")
    status = os.system(command)
    if status != 0:
        print(f"Failed executing >>> {command}")
        break
    print(f"end step {index+1}")